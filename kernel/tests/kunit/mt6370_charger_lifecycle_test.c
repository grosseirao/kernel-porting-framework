// SPDX-License-Identifier: GPL-2.0-only
/* Real staged callbacks, PS/workqueues/regmap/IRQ_SIM; all registers in RAM. */
#include <kunit/test.h>
#include <kunit/resource.h>
#include <linux/completion.h>
#include <linux/irq.h>
#include <linux/irq_sim.h>
#include <linux/kthread.h>
#include <linux/of.h>
#include <linux/platform_device.h>

/* Only the platform identity is substituted; bus/PS/probe/work are real. */
static bool readonly_machine;
static int synthetic_machine_match(const char *name)
{
	return readonly_machine && !strcmp(name, "lge,mmh55lm-memory-draft");
}
#define of_machine_is_compatible(name) synthetic_machine_match(name)

#undef module_platform_driver
#define module_platform_driver(driver)
#include "../../../drivers/power/supply/mt6370-charger.c"
#undef of_machine_is_compatible

struct lifecycle_fixture {
	struct mt6370_priv priv;
	struct device *root;
	void *group;
	struct irq_domain *domain;
	unsigned int mapped[MT6370_IRQ_MAX];
	u8 regs[0x200];
	atomic_t reads, writes;
	bool async_initialized, block_write;
	struct completion write_entered, write_release, stop_started, stop_done;
	struct task_struct *setter, *stopper;
	int setter_result;
	struct platform_device *readonly_pdev;
	void *readonly_group;
	int read_error;
	int write_error;
	bool ignore_write, fail_after_write;
	struct power_supply *guard_supply;
	int sensor_temp, sensor_uv, sensor_present, sensor_error;
};

static int ram_read(void *context, unsigned int reg, unsigned int *value)
{
	struct lifecycle_fixture *f = context;
	if (reg >= ARRAY_SIZE(f->regs))
		return -EINVAL;
	atomic_inc(&f->reads);
	if (READ_ONCE(f->read_error))
		return READ_ONCE(f->read_error);
	*value = f->regs[reg];
	return 0;
}

static int ram_write(void *context, unsigned int reg, unsigned int value)
{
	struct lifecycle_fixture *f = context;
	if (reg >= ARRAY_SIZE(f->regs))
		return -EINVAL;
	if (READ_ONCE(f->block_write) && reg == MT6370_REG_CHG_CTRL7) {
		complete(&f->write_entered);
		if (!wait_for_completion_timeout(&f->write_release, 5 * HZ))
			return -ETIMEDOUT;
	}
	atomic_inc(&f->writes);
	if (f->write_error)
		return f->write_error;
	if (f->ignore_write)
		return 0;
	f->regs[reg] = value;
	if (f->fail_after_write)
		WRITE_ONCE(f->read_error, -EIO);
	return 0;
}

static const struct regmap_bus ram_bus = {.reg_read = ram_read, .reg_write = ram_write};
static const struct regmap_config ram_config = {
	.reg_bits = 16, .val_bits = 8, .max_register = 0x1ff,
	.cache_type = REGCACHE_NONE,
};

static void release_lifecycle_fixture(void *data)
{
	struct lifecycle_fixture *f = data;
	unsigned int i;
	complete_all(&f->write_release);
	if (f->setter)
		kthread_stop(f->setter);
	if (f->stopper)
		kthread_stop(f->stopper);
	if (f->readonly_pdev) {
		if (f->readonly_group)
			devres_release_group(&f->readonly_pdev->dev, f->readonly_group);
		platform_device_unregister(f->readonly_pdev);
	}
	if (f->guard_supply)
		power_supply_unregister(f->guard_supply);
	if (f->async_initialized)
		mt6370_chg_quiesce(&f->priv);
	for (i = 0; i < f->priv.irqs_requested; i++)
		free_irq(f->priv.irq_nums[i], &f->priv);
	for (i = 0; i < MT6370_IRQ_MAX; i++)
		if (f->mapped[i])
			irq_dispose_mapping(f->mapped[i]);
	if (f->domain)
		irq_domain_remove_sim(f->domain);
	devres_release_group(f->root, f->group);
	root_device_unregister(f->root);
	k40s_readonly = false;
	k40s_inhibit_only = false;
	k40s_thermal_guard = false;
	k40s_guard_battery = NULL;
	readonly_machine = false;
}

static int create_lifecycle_fixture(struct kunit *test)
{
	static const irq_handler_t handlers[] = {
		mt6370_attach_i_handler, mt6370_uvp_d_evt_handler, mt6370_mivr_handler,
	};
	struct lifecycle_fixture *f;
	unsigned int i;
	int ret;
	f = kunit_kzalloc(test, sizeof(*f), GFP_KERNEL);
	if (!f)
		return -ENOMEM;
	test->priv = f;
	init_completion(&f->write_entered);
	init_completion(&f->write_release);
	init_completion(&f->stop_started);
	init_completion(&f->stop_done);
	f->root = root_device_register("portkit-mt6370-root");
	if (IS_ERR(f->root))
		return PTR_ERR(f->root);
	f->group = devres_open_group(f->root, NULL, GFP_KERNEL);
	if (!f->group) {
		root_device_unregister(f->root);
		return -ENOMEM;
	}
	ret = kunit_add_action_or_reset(test, release_lifecycle_fixture, f);
	if (ret)
		return ret;
	f->priv.dev = f->root;
	f->priv.regmap = devm_regmap_init(f->root, &ram_bus, f, &ram_config);
	if (IS_ERR(f->priv.regmap))
		return PTR_ERR(f->priv.regmap);
	ret = mt6370_chg_init_rmap_fields(&f->priv);
	if (ret)
		return ret;
	ret = devm_mutex_init(f->root, &f->priv.attach_lock);
	if (ret)
		return ret;
	f->priv.wq = create_singlethread_workqueue("portkit-mt6370");
	if (!f->priv.wq)
		return -ENOMEM;
	ret = devm_add_action_or_reset(f->root, mt6370_chg_destroy_wq, f->priv.wq);
	if (ret)
		return ret;
	ret = devm_work_autocancel(f->root, &f->priv.bc12_work, mt6370_chg_bc12_work_func);
	if (ret)
		return ret;
	ret = devm_delayed_work_autocancel(f->root, &f->priv.mivr_dwork,
					 mt6370_chg_mivr_dwork_func);
	if (ret)
		return ret;
	f->async_initialized = true;
	ret = mt6370_chg_init_psy(&f->priv);
	if (ret)
		return ret;
	f->domain = irq_domain_create_sim(NULL, MT6370_IRQ_MAX);
	if (IS_ERR(f->domain)) {
		ret = PTR_ERR(f->domain);
		f->domain = NULL;
		return ret;
	}
	for (i = 0; i < MT6370_IRQ_MAX; i++) {
		f->mapped[i] = irq_create_mapping(f->domain, i);
		if (!f->mapped[i])
			return -ENOMEM;
		f->priv.irq_nums[i] = f->mapped[i];
		ret = request_threaded_irq(f->mapped[i], NULL, handlers[i], IRQF_ONESHOT,
					   "portkit-mt6370", &f->priv);
		if (ret)
			return ret;
		f->priv.irqs_requested++;
	}
	return 0;
}

static void mark_ready(struct lifecycle_fixture *f)
{
	mutex_lock(&f->priv.attach_lock);
	f->priv.ready = true;
	mutex_unlock(&f->priv.attach_lock);
}

static void unready_callbacks_do_not_access_regmap(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	union power_supply_propval out = {.intval = 123456}, in = {.intval = 900000};
	int reads = atomic_read(&f->reads), writes = atomic_read(&f->writes);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(f->priv.psy,
		POWER_SUPPLY_PROP_CONSTANT_CHARGE_CURRENT, &out), -EAGAIN);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	KUNIT_EXPECT_EQ(test, power_supply_set_property(f->priv.psy,
		POWER_SUPPLY_PROP_CONSTANT_CHARGE_CURRENT, &in), -EAGAIN);
	mt6370_chg_pwr_rdy_check(&f->priv);
	mt6370_mivr_handler(f->priv.irq_nums[MT6370_IRQ_MIVR], &f->priv);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->reads), reads);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), writes);
	KUNIT_EXPECT_FALSE(test, delayed_work_pending(&f->priv.mivr_dwork));
	mark_ready(f);
	in.intval = 1;
	KUNIT_ASSERT_EQ(test, power_supply_set_property(f->priv.psy, POWER_SUPPLY_PROP_ONLINE, &in), 0);
	flush_work(&f->priv.bc12_work);
	f->regs[MT6370_REG_CHG_STAT] = 1 << 6;
	KUNIT_ASSERT_EQ(test, power_supply_get_property(f->priv.psy, POWER_SUPPLY_PROP_STATUS, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, POWER_SUPPLY_STATUS_CHARGING);
}

static void quiesce_blocks_callbacks_and_requeue(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	union power_supply_propval out = {.intval = 123456}, in = {.intval = 1};
	unsigned int i;
	int reads, writes;
	mark_ready(f);
	KUNIT_ASSERT_EQ(test, power_supply_set_property(f->priv.psy, POWER_SUPPLY_PROP_ONLINE, &in), 0);
	mt6370_chg_quiesce(&f->priv);
	reads = atomic_read(&f->reads);
	writes = atomic_read(&f->writes);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(f->priv.psy, POWER_SUPPLY_PROP_ONLINE, &out), -ESHUTDOWN);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	KUNIT_EXPECT_EQ(test, power_supply_set_property(f->priv.psy, POWER_SUPPLY_PROP_ONLINE, &in), -ESHUTDOWN);
	mt6370_attach_i_handler(0, &f->priv);
	mt6370_uvp_d_evt_handler(0, &f->priv);
	mt6370_mivr_handler(0, &f->priv);
	mt6370_chg_bc12_work_func(&f->priv.bc12_work);
	mt6370_chg_mivr_dwork_func(&f->priv.mivr_dwork.work);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->reads), reads);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), writes);
	KUNIT_EXPECT_FALSE(test, work_pending(&f->priv.bc12_work));
	KUNIT_EXPECT_FALSE(test, delayed_work_pending(&f->priv.mivr_dwork));
	mt6370_chg_quiesce(&f->priv);
	for (i = 0; i < f->priv.irqs_requested; i++) {
		enable_irq(f->priv.irq_nums[i]);
		KUNIT_EXPECT_FALSE(test, irqd_irq_disabled(irq_get_irq_data(f->priv.irq_nums[i])));
		disable_irq(f->priv.irq_nums[i]);
	}
}

static void pending_mivr_disable_is_balanced(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	unsigned int irq = f->priv.irq_nums[MT6370_IRQ_MIVR];
	mark_ready(f);
	mt6370_mivr_handler(irq, &f->priv);
	mod_delayed_work(system_wq, &f->priv.mivr_dwork, 60 * HZ);
	KUNIT_ASSERT_TRUE(test, delayed_work_pending(&f->priv.mivr_dwork));
	KUNIT_ASSERT_EQ(test, atomic_read(&f->priv.mivr_irq_disabled), 1);
	mt6370_chg_quiesce(&f->priv);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->priv.mivr_irq_disabled), 0);
	KUNIT_EXPECT_FALSE(test, delayed_work_pending(&f->priv.mivr_dwork));
	enable_irq(irq); /* Balance only quiesce's disable, not a leaked handler disable. */
	KUNIT_EXPECT_FALSE(test, irqd_irq_disabled(irq_get_irq_data(irq)));
	disable_irq(irq);
}

static void partial_irq_initialization_quiesces(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	unsigned int i = MT6370_IRQ_MIVR;
	free_irq(f->priv.irq_nums[i], &f->priv);
	irq_dispose_mapping(f->mapped[i]);
	f->mapped[i] = 0;
	f->priv.irqs_requested--;
	mt6370_chg_quiesce(&f->priv);
	KUNIT_EXPECT_TRUE(test, f->priv.stopping);
	KUNIT_EXPECT_FALSE(test, f->priv.ready);
	KUNIT_EXPECT_FALSE(test, delayed_work_pending(&f->priv.mivr_dwork));
}

static int setter_thread(void *data)
{
	struct lifecycle_fixture *f = data;
	union power_supply_propval value = {.intval = 900000};
	f->setter_result = power_supply_set_property(f->priv.psy,
		POWER_SUPPLY_PROP_CONSTANT_CHARGE_CURRENT, &value);
	/* The fixture owns kthread_stop; never leave it an expired task pointer. */
	set_current_state(TASK_INTERRUPTIBLE);
	while (!kthread_should_stop()) {
		schedule();
		set_current_state(TASK_INTERRUPTIBLE);
	}
	__set_current_state(TASK_RUNNING);
	return 0;
}

static int stopper_thread(void *data)
{
	struct lifecycle_fixture *f = data;
	complete(&f->stop_started);
	mt6370_chg_quiesce(&f->priv);
	complete(&f->stop_done);
	set_current_state(TASK_INTERRUPTIBLE);
	while (!kthread_should_stop()) {
		schedule();
		set_current_state(TASK_INTERRUPTIBLE);
	}
	__set_current_state(TASK_RUNNING);
	return 0;
}

static void inflight_setter_finishes_before_quiesce(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	mark_ready(f);
	WRITE_ONCE(f->block_write, true);
	f->setter = kthread_run(setter_thread, f, "kpf-setter");
	if (IS_ERR(f->setter)) {
		f->setter = NULL;
		KUNIT_FAIL(test, "setter creation failed");
		return;
	}
	KUNIT_ASSERT_NE(test, wait_for_completion_timeout(&f->write_entered, HZ), 0UL);
	f->stopper = kthread_run(stopper_thread, f, "kpf-stopper");
	if (IS_ERR(f->stopper)) {
		f->stopper = NULL;
		KUNIT_FAIL(test, "stopper creation failed");
		return;
	}
	KUNIT_ASSERT_NE(test, wait_for_completion_timeout(&f->stop_started, HZ), 0UL);
	KUNIT_EXPECT_EQ(test, wait_for_completion_timeout(&f->stop_done, msecs_to_jiffies(10)), 0UL);
	complete(&f->write_release);
	KUNIT_ASSERT_NE(test, wait_for_completion_timeout(&f->stop_done, HZ), 0UL);
	kthread_stop(f->setter);
	f->setter = NULL;
	kthread_stop(f->stopper);
	f->stopper = NULL;
	KUNIT_EXPECT_EQ(test, f->setter_result, 0);
	KUNIT_EXPECT_TRUE(test, f->priv.stopping);
}

static struct kunit_case lifecycle_cases[] = {
	KUNIT_CASE(unready_callbacks_do_not_access_regmap),
	KUNIT_CASE(quiesce_blocks_callbacks_and_requeue),
	KUNIT_CASE(pending_mivr_disable_is_balanced),
	KUNIT_CASE(partial_irq_initialization_quiesces),
	KUNIT_CASE(inflight_setter_finishes_before_quiesce),
	{}
};
static struct kunit_suite lifecycle_suite = {
	.name = "mt6370-charger-lifecycle-offline",
	.init = create_lifecycle_fixture,
	.test_cases = lifecycle_cases,
};

static int create_readonly_fixture(struct kunit *test)
{
	struct lifecycle_fixture *f;
	struct platform_device_info info = {.name = "portkit-mt6370-readonly", .id = PLATFORM_DEVID_NONE};
	int ret;
	f = kunit_kzalloc(test, sizeof(*f), GFP_KERNEL);
	if (!f)
		return -ENOMEM;
	test->priv = f;
	init_completion(&f->write_release);
	f->root = root_device_register("portkit-mt6370-ro-parent");
	if (IS_ERR(f->root))
		return PTR_ERR(f->root);
	f->group = devres_open_group(f->root, NULL, GFP_KERNEL);
	if (!f->group) {
		root_device_unregister(f->root);
		return -ENOMEM;
	}
	ret = kunit_add_action_or_reset(test, release_lifecycle_fixture, f);
	if (ret)
		return ret;
	if (IS_ERR(devm_regmap_init(f->root, &ram_bus, f, &ram_config)))
		return -ENOMEM;
	info.parent = f->root;
	f->readonly_pdev = platform_device_register_full(&info);
	if (IS_ERR(f->readonly_pdev)) {
		ret = PTR_ERR(f->readonly_pdev);
		f->readonly_pdev = NULL;
		return ret;
	}
	f->readonly_group = devres_open_group(&f->readonly_pdev->dev, NULL, GFP_KERNEL);
	if (!f->readonly_group)
		return -ENOMEM;
	f->regs[MT6370_REG_DEV_INFO] = 0xf4;
	f->regs[MT6370_REG_CHG_CTRL2] = 0x09;
	f->regs[MT6370_REG_CHG_CTRL3] = 0x21;
	f->regs[MT6370_REG_CHG_CTRL4] = 0x6a;
	f->regs[MT6370_REG_CHG_CTRL6] = 0x0a;
	f->regs[MT6370_REG_CHG_CTRL7] = 0x4c;
	f->regs[MT6370_REG_CHG_CTRL8] = 0x01;
	f->regs[MT6370_REG_CHG_CTRL9] = 0x10;
	f->regs[MT6370_REG_CHG_STAT] = 0x40;
	k40s_readonly = true;
	readonly_machine = true;
	return 0;
}

static void readonly_machine_chip_and_bus_gates(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	int attempt;
	for (attempt = 0; attempt < 3; attempt++) {
		if (attempt) {
			f->readonly_group = devres_open_group(&f->readonly_pdev->dev, NULL, GFP_KERNEL);
			KUNIT_ASSERT_NOT_NULL(test, f->readonly_group);
		}
		readonly_machine = attempt != 0;
		f->regs[MT6370_REG_DEV_INFO] = attempt == 1 ? 0xe4 : 0xf4;
		f->read_error = attempt == 2 ? -EIO : 0;
		KUNIT_EXPECT_EQ(test, mt6370_chg_probe(f->readonly_pdev),
			attempt == 0 ? -EPERM : attempt == 1 ? -ENODEV : -EIO);
		KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), 0);
		devres_release_group(&f->readonly_pdev->dev, f->readonly_group);
		f->readonly_group = NULL;
		platform_set_drvdata(f->readonly_pdev, NULL);
	}
}

static void readonly_real_probe_and_getters_never_write(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	union power_supply_propval out, in = {.intval = 0};
	u8 before[sizeof(f->regs)];
	unsigned int i;
	memcpy(before, f->regs, sizeof(before));
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	KUNIT_EXPECT_TRUE(test, priv->lab_readonly);
	KUNIT_EXPECT_PTR_EQ(test, priv->iio_adcs, NULL);
	KUNIT_EXPECT_PTR_EQ(test, priv->rdev, NULL);
	KUNIT_EXPECT_EQ(test, priv->irqs_requested, 0U);
	for (i = 0; i < priv->psy->desc->num_properties; i++) {
		KUNIT_EXPECT_EQ(test, mt6370_chg_property_is_writeable(priv->psy, mt6370_chg_properties[i]), 0);
		KUNIT_EXPECT_EQ(test, power_supply_get_property(priv->psy, mt6370_chg_properties[i], &out), 0);
		KUNIT_EXPECT_EQ(test, power_supply_set_property(priv->psy, mt6370_chg_properties[i], &in), -EPERM);
	}
	KUNIT_ASSERT_EQ(test, power_supply_get_property(priv->psy, POWER_SUPPLY_PROP_CONSTANT_CHARGE_VOLTAGE, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 4430000);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(priv->psy, POWER_SUPPLY_PROP_CONSTANT_CHARGE_CURRENT, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 2000000);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(priv->psy, POWER_SUPPLY_PROP_INPUT_CURRENT_LIMIT, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 500000);
	mt6370_chg_pwr_rdy_check(priv);
	mt6370_attach_i_handler(0, priv);
	mt6370_uvp_d_evt_handler(0, priv);
	mt6370_mivr_handler(0, priv);
	mt6370_chg_bc12_work_func(&priv->bc12_work);
	mt6370_chg_mivr_dwork_func(&priv->mivr_dwork.work);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), 0);
	KUNIT_EXPECT_MEMEQ(test, before, f->regs, sizeof(before));
	KUNIT_EXPECT_FALSE(test, work_pending(&priv->bc12_work));
	KUNIT_EXPECT_FALSE(test, delayed_work_pending(&priv->mivr_dwork));
}

static void readonly_bus_error_preserves_output(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	union power_supply_propval out = {.intval = 123456};
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	flush_delayed_work(&priv->psy->deferred_register_work);
	flush_work(&priv->psy->changed_work);
	WRITE_ONCE(f->read_error, -EIO);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(priv->psy, POWER_SUPPLY_PROP_CONSTANT_CHARGE_VOLTAGE, &out), -EIO);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), 0);
}

static void readonly_inherited_ichg_selectors(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	union power_supply_propval out;
	unsigned int selector, normal = 123456;
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	flush_delayed_work(&priv->psy->deferred_register_work);
	flush_work(&priv->psy->changed_work);
	for (selector = 0; selector < 64; selector++) {
		f->regs[MT6370_REG_CHG_CTRL7] = selector << 2;
		out.intval = 123456;
		KUNIT_EXPECT_EQ(test, power_supply_get_property(priv->psy,
			POWER_SUPPLY_PROP_CONSTANT_CHARGE_CURRENT, &out),
			selector <= 49 ? 0 : -EINVAL);
		KUNIT_EXPECT_EQ(test, out.intval,
			selector <= 49 ? (int)(100000 + selector * 100000) : 123456);
	}
	f->regs[MT6370_REG_CHG_CTRL7] = 0;
	KUNIT_EXPECT_EQ(test, mt6370_chg_field_get(priv, F_ICHG, &normal), -EINVAL);
	KUNIT_EXPECT_EQ(test, normal, 123456U);
	WRITE_ONCE(f->read_error, -EIO);
	out.intval = 123456;
	KUNIT_EXPECT_EQ(test, power_supply_get_property(priv->psy,
		POWER_SUPPLY_PROP_CONSTANT_CHARGE_CURRENT, &out), -EIO);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), 0);
}

static struct kunit_case readonly_cases[] = {
	KUNIT_CASE(readonly_machine_chip_and_bus_gates),
	KUNIT_CASE(readonly_real_probe_and_getters_never_write),
	KUNIT_CASE(readonly_bus_error_preserves_output),
	KUNIT_CASE(readonly_inherited_ichg_selectors),
	{}
};
static struct kunit_suite readonly_suite = {
	.name = "mt6370-charger-readonly-offline",
	.init = create_readonly_fixture,
	.test_cases = readonly_cases,
};
static int create_inhibit_fixture(struct kunit *test)
{
	int ret = create_readonly_fixture(test);
	if (ret)
		return ret;
	k40s_readonly = false;
	k40s_inhibit_only = true;
	return 0;
}

static void inhibit_probe_mask_api_and_remove(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	union power_supply_propval out, in;
	u8 before[sizeof(f->regs)];
	unsigned int i;
	memcpy(before, f->regs, sizeof(before));
	before[MT6370_REG_CHG_CTRL2] &= ~BIT(0);
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	KUNIT_EXPECT_TRUE(test, priv->lab_inhibit_only);
	KUNIT_EXPECT_FALSE(test, priv->lab_readonly);
	KUNIT_EXPECT_EQ(test, priv->irqs_requested, 0U);
	KUNIT_EXPECT_PTR_EQ(test, priv->iio_adcs, NULL);
	KUNIT_EXPECT_PTR_EQ(test, priv->rdev, NULL);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), 1);
	KUNIT_EXPECT_MEMEQ(test, before, f->regs, sizeof(before));
	for (i = 0; i < priv->psy->desc->num_properties; i++) {
		enum power_supply_property psp = priv->psy->desc->properties[i];
		in.intval = 0;
		KUNIT_EXPECT_EQ(test, power_supply_set_property(priv->psy, psp, &in), -EPERM);
		KUNIT_EXPECT_EQ(test, mt6370_chg_property_is_writeable(priv->psy, psp),
			psp == POWER_SUPPLY_PROP_CHARGE_BEHAVIOUR);
	}
	in.intval = POWER_SUPPLY_CHARGE_BEHAVIOUR_INHIBIT_CHARGE;
	KUNIT_EXPECT_EQ(test, power_supply_set_property(priv->psy,
		POWER_SUPPLY_PROP_CHARGE_BEHAVIOUR, &in), 0);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(priv->psy,
		POWER_SUPPLY_PROP_CHARGE_BEHAVIOUR, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, POWER_SUPPLY_CHARGE_BEHAVIOUR_INHIBIT_CHARGE);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), 1);
	devres_release_group(&f->readonly_pdev->dev, f->readonly_group);
	f->readonly_group = NULL;
	platform_set_drvdata(f->readonly_pdev, NULL);
	KUNIT_EXPECT_MEMEQ(test, before, f->regs, sizeof(before));
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), 1);
}

static void inhibit_probe_io_and_readback_failures(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	unsigned int attempt;
	for (attempt = 0; attempt < 3; attempt++) {
		if (attempt) {
			f->readonly_group = devres_open_group(&f->readonly_pdev->dev, NULL, GFP_KERNEL);
			KUNIT_ASSERT_NOT_NULL(test, f->readonly_group);
		}
		f->regs[MT6370_REG_CHG_CTRL2] = 0x09;
		f->read_error = 0;
		f->write_error = attempt == 0 ? -EIO : 0;
		f->fail_after_write = attempt == 1;
		f->ignore_write = attempt == 2;
		KUNIT_EXPECT_EQ(test, mt6370_chg_probe(f->readonly_pdev), -EIO);
		priv = platform_get_drvdata(f->readonly_pdev);
		KUNIT_EXPECT_PTR_EQ(test, priv->psy, NULL);
		KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2], attempt == 1 ? 0x08 : 0x09);
		devres_release_group(&f->readonly_pdev->dev, f->readonly_group);
		f->readonly_group = NULL;
		platform_set_drvdata(f->readonly_pdev, NULL);
	}
}

static void inhibit_conflicts_with_readonly(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	k40s_readonly = true;
	KUNIT_EXPECT_EQ(test, mt6370_chg_probe(f->readonly_pdev), -EINVAL);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->reads), 0);
	KUNIT_EXPECT_EQ(test, atomic_read(&f->writes), 0);
}

static struct kunit_case inhibit_cases[] = {
	KUNIT_CASE(inhibit_probe_mask_api_and_remove),
	KUNIT_CASE(inhibit_probe_io_and_readback_failures),
	KUNIT_CASE(inhibit_conflicts_with_readonly),
	{}
};
static struct kunit_suite inhibit_suite = {
	.name = "mt6370-charger-inhibit-offline",
	.init = create_inhibit_fixture,
	.test_cases = inhibit_cases,
};
static int guard_sensor_get(struct power_supply *psy, enum power_supply_property psp,
			    union power_supply_propval *val)
{
	struct lifecycle_fixture *f = power_supply_get_drvdata(psy);
	if (f->sensor_error)
		return f->sensor_error;
	switch (psp) {
	case POWER_SUPPLY_PROP_PRESENT: val->intval = f->sensor_present; return 0;
	case POWER_SUPPLY_PROP_TEMP: val->intval = f->sensor_temp; return 0;
	case POWER_SUPPLY_PROP_VOLTAGE_NOW: val->intval = f->sensor_uv; return 0;
	default: return -EINVAL;
	}
}

static enum power_supply_property guard_sensor_props[] = {
	POWER_SUPPLY_PROP_PRESENT, POWER_SUPPLY_PROP_TEMP, POWER_SUPPLY_PROP_VOLTAGE_NOW,
};
static const struct power_supply_desc guard_sensor_desc = {
	.name = "portkit-guard-battery",
	.type = POWER_SUPPLY_TYPE_BATTERY,
	.properties = guard_sensor_props,
	.num_properties = ARRAY_SIZE(guard_sensor_props),
	.get_property = guard_sensor_get,
};

static int create_guard_fixture(struct kunit *test)
{
	struct lifecycle_fixture *f;
	struct power_supply_config cfg = {};
	int ret = create_readonly_fixture(test);
	if (ret)
		return ret;
	f = test->priv;
	k40s_readonly = false;
	k40s_thermal_guard = true;
	k40s_guard_battery = "portkit-guard-battery";
	f->sensor_temp = 330;
	f->sensor_uv = 4390000;
	f->sensor_present = 1;
	f->regs[MT6370_REG_CHG_CTRL7] = 0x10; /*500mA*/
	f->regs[MT6370_REG_CHG_CTRL4] = 0x64; /*4.40V*/
	f->regs[MT6370_REG_CHG_CTRL6] = 0x0c; /*4.50V*/
	cfg.drv_data = f;
	f->guard_supply = power_supply_register(f->root, &guard_sensor_desc, &cfg);
	if (IS_ERR(f->guard_supply)) {
		ret = PTR_ERR(f->guard_supply);
		f->guard_supply = NULL;
		return ret;
	}
	flush_delayed_work(&f->guard_supply->deferred_register_work);
	flush_work(&f->guard_supply->changed_work);
	return 0;
}

static int guard_request_auto(struct mt6370_priv *priv)
{
	union power_supply_propval val = {.intval = POWER_SUPPLY_CHARGE_BEHAVIOUR_AUTO};
	int ret = power_supply_set_property(priv->psy, POWER_SUPPLY_PROP_CHARGE_BEHAVIOUR, &val);
	cancel_delayed_work_sync(&priv->guard_work);
	return ret;
}

static void guard_real_probe_auto_and_remove(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	u8 before[sizeof(f->regs)];
	memcpy(before, f->regs, sizeof(before));
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	KUNIT_EXPECT_FALSE(test, priv->guard_auto);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2] & BIT(0), 0);
	KUNIT_ASSERT_EQ(test, guard_request_auto(priv), 0);
	KUNIT_EXPECT_TRUE(test, priv->guard_auto);
	KUNIT_EXPECT_TRUE(test, priv->guard_charging);
	KUNIT_EXPECT_MEMEQ(test, before, f->regs, sizeof(before));
	devres_release_group(&f->readonly_pdev->dev, f->readonly_group);
	f->readonly_group = NULL;
	platform_set_drvdata(f->readonly_pdev, NULL);
	before[MT6370_REG_CHG_CTRL2] &= ~BIT(0);
	KUNIT_EXPECT_MEMEQ(test, before, f->regs, sizeof(before));
}

static void guard_temperature_voltage_and_hysteresis(struct kunit *test)
{
	struct mt6370_priv priv = {};
	KUNIT_EXPECT_FALSE(test, mt6370_chg_guard_allowed(&priv, 29, 4000000));
	KUNIT_EXPECT_TRUE(test, mt6370_chg_guard_allowed(&priv, 30, 4000000));
	KUNIT_EXPECT_TRUE(test, mt6370_chg_guard_allowed(&priv, 430, 4390000));
	KUNIT_EXPECT_FALSE(test, mt6370_chg_guard_allowed(&priv, 431, 4390000));
	priv.guard_charging = true;
	KUNIT_EXPECT_TRUE(test, mt6370_chg_guard_allowed(&priv, 449, 4390000));
	KUNIT_EXPECT_FALSE(test, mt6370_chg_guard_allowed(&priv, 450, 4390000));
	KUNIT_EXPECT_FALSE(test, mt6370_chg_guard_allowed(&priv, -1, 4000000));
	KUNIT_EXPECT_FALSE(test, mt6370_chg_guard_allowed(&priv, 330, 3299999));
	KUNIT_EXPECT_FALSE(test, mt6370_chg_guard_allowed(&priv, 90, 4400001));
	KUNIT_EXPECT_FALSE(test, mt6370_chg_guard_allowed(&priv, 90, 4300000));
	KUNIT_EXPECT_TRUE(test, mt6370_chg_guard_allowed(&priv, 90, 4200000));
}

static void guard_sensor_error_latches_and_stops(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	KUNIT_ASSERT_EQ(test, guard_request_auto(priv), 0);
	f->sensor_error = -ETIME;
	mt6370_chg_guard_work(&priv->guard_work.work);
	KUNIT_EXPECT_TRUE(test, priv->guard_fault);
	KUNIT_EXPECT_FALSE(test, priv->guard_auto);
	KUNIT_EXPECT_FALSE(test, priv->guard_charging);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2] & BIT(0), 0);
	KUNIT_EXPECT_FALSE(test, delayed_work_pending(&priv->guard_work));
	f->sensor_error = 0;
	KUNIT_EXPECT_EQ(test, guard_request_auto(priv), -EPERM);
}

static void guard_limits_mismatch_never_enables(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	const struct { unsigned int reg; u8 invalid; } cases[] = {
		{ MT6370_REG_CHG_CTRL7, 0x14 }, /*600mA*/
		{ MT6370_REG_CHG_CTRL3, 0x25 }, /*550mA*/
		{ MT6370_REG_CHG_CTRL4, 0x66 }, /*4.41V*/
		{ MT6370_REG_CHG_CTRL6, 0x0a }, /*4.40V MIVR*/
		{ MT6370_REG_CHG_CTRL2, 0x04 }, /*wrong limit selection*/
	};
	unsigned int i;
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	for (i = 0; i < ARRAY_SIZE(cases); i++) {
		u8 previous = f->regs[cases[i].reg];
		f->regs[cases[i].reg] = cases[i].invalid;
		KUNIT_EXPECT_EQ(test, mt6370_chg_guard_limits(priv), -EPERM);
		f->regs[cases[i].reg] = previous;
	}
	f->regs[MT6370_REG_CHG_CTRL7] = 0x14; /*600mA, outside envelope*/
	KUNIT_EXPECT_EQ(test, guard_request_auto(priv), -EPERM);
	KUNIT_EXPECT_TRUE(test, priv->guard_fault);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2] & BIT(0), 0);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL7], 0x14);
}

static void guard_suspend_resume_requires_new_auto(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	KUNIT_ASSERT_EQ(test, guard_request_auto(priv), 0);
	KUNIT_ASSERT_EQ(test, mt6370_chg_guard_suspend(&f->readonly_pdev->dev), 0);
	KUNIT_EXPECT_TRUE(test, priv->guard_paused);
	KUNIT_EXPECT_FALSE(test, priv->guard_auto);
	KUNIT_EXPECT_EQ(test, guard_request_auto(priv), -EBUSY);
	KUNIT_ASSERT_EQ(test, mt6370_chg_guard_resume(&f->readonly_pdev->dev), 0);
	KUNIT_EXPECT_FALSE(test, priv->guard_charging);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2] & BIT(0), 0);
	KUNIT_EXPECT_EQ(test, guard_request_auto(priv), 0);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2] & BIT(0), 1);
}

static void guard_failed_enable_and_suspend_unconfirmed(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	f->ignore_write = true;
	KUNIT_EXPECT_EQ(test, guard_request_auto(priv), -EIO);
	KUNIT_EXPECT_TRUE(test, priv->guard_fault);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2] & BIT(0), 0);
	/* An independent fixture bus failure must abort, never approve sleep. */
	f->read_error = -EIO;
	KUNIT_EXPECT_EQ(test, mt6370_chg_guard_suspend(&f->readonly_pdev->dev), -EIO);
}

static void guard_missing_battery_never_enables(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	k40s_guard_battery = "no-such-kpf-battery";
	KUNIT_EXPECT_EQ(test, mt6370_chg_probe(f->readonly_pdev), -ENODEV);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2] & BIT(0), 0);
}

static void guard_battery_absent_never_enables(struct kunit *test)
{
	struct lifecycle_fixture *f = test->priv;
	struct mt6370_priv *priv;
	KUNIT_ASSERT_EQ(test, mt6370_chg_probe(f->readonly_pdev), 0);
	priv = platform_get_drvdata(f->readonly_pdev);
	f->sensor_present = 0;
	KUNIT_EXPECT_EQ(test, guard_request_auto(priv), -ENODEV);
	KUNIT_EXPECT_TRUE(test, priv->guard_fault);
	KUNIT_EXPECT_EQ(test, f->regs[MT6370_REG_CHG_CTRL2] & BIT(0), 0);
}

static struct kunit_case guard_cases[] = {
	KUNIT_CASE(guard_real_probe_auto_and_remove),
	KUNIT_CASE(guard_temperature_voltage_and_hysteresis),
	KUNIT_CASE(guard_sensor_error_latches_and_stops),
	KUNIT_CASE(guard_limits_mismatch_never_enables),
	KUNIT_CASE(guard_suspend_resume_requires_new_auto),
	KUNIT_CASE(guard_failed_enable_and_suspend_unconfirmed),
	KUNIT_CASE(guard_missing_battery_never_enables),
	KUNIT_CASE(guard_battery_absent_never_enables),
	{}
};
static struct kunit_suite guard_suite = {
	.name = "mt6370-charger-guard-offline",
	.init = create_guard_fixture,
	.test_cases = guard_cases,
};
kunit_test_suites(&lifecycle_suite, &readonly_suite, &inhibit_suite, &guard_suite);

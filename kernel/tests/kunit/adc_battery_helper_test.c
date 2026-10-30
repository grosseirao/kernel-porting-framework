// SPDX-License-Identifier: GPL-2.0-only
/* Synthetic UML fixture: real core/workqueue/devres, no hardware transport.
 * The included upstream helper retains GPL-2.0+; no algorithm is copied here.
 * CONFIG_ADC_BATTERY_HELPER must be off to avoid a second compiled instance.
 */
#include <kunit/test.h>
#include <kunit/resource.h>
#include <linux/completion.h>
#include <linux/device.h>
#include <linux/kthread.h>

#include "../../../drivers/power/supply/adc-battery-helper.c"

struct helper_fixture {
	struct adc_battery_helper helper;
	struct device *dev;
	struct power_supply *psy;
	struct power_supply_battery_info info;
	struct power_supply_battery_ocv_table ocv[2];
	void *group;
	atomic_t reads, error, reader_errors, reader_successes;
	struct completion reader_started;
};

static int synthetic_acquisition(struct power_supply *psy, int *uv, int *ua)
{
	struct helper_fixture *fixture = container_of(power_supply_get_drvdata(psy),
						     struct helper_fixture, helper);
	int error = atomic_read(&fixture->error);

	atomic_inc(&fixture->reads);
	if (error)
		return error;
	*uv = 3700000;
	*ua = 0;
	return 0;
}

static const struct power_supply_desc synthetic_desc = {
	.name = "portkit-adc-helper",
	.type = POWER_SUPPLY_TYPE_BATTERY,
	.properties = adc_battery_helper_properties,
	.num_properties = ADC_HELPER_NUM_PROPERTIES,
	.get_property = adc_battery_helper_get_property,
	.external_power_changed = adc_battery_helper_external_power_changed,
	.no_thermal = true,
};

static void release_fixture(void *data)
{
	struct helper_fixture *fixture = data;

	devres_release_group(fixture->dev, fixture->group);
	root_device_unregister(fixture->dev);
}

static int create_fixture(struct kunit *test)
{
	struct helper_fixture *fixture;
	struct power_supply_config config = {};
	int ret;

	fixture = kunit_kzalloc(test, sizeof(*fixture), GFP_KERNEL);
	if (!fixture)
		return -ENOMEM;
	test->priv = fixture;
	fixture->dev = root_device_register("portkit-adc-helper-root");
	if (IS_ERR(fixture->dev))
		return PTR_ERR(fixture->dev);
	fixture->group = devres_open_group(fixture->dev, NULL, GFP_KERNEL);
	if (!fixture->group) {
		root_device_unregister(fixture->dev);
		return -ENOMEM;
	}
	ret = kunit_add_action_or_reset(test, release_fixture, fixture);
	if (ret)
		return ret;
	config.drv_data = &fixture->helper;
	fixture->psy = devm_power_supply_register(fixture->dev, &synthetic_desc, &config);
	if (IS_ERR(fixture->psy))
		return PTR_ERR(fixture->psy);
	fixture->ocv[0] = (struct power_supply_battery_ocv_table){4200000, 100};
	fixture->ocv[1] = (struct power_supply_battery_ocv_table){3200000, 0};
	fixture->info.constant_charge_voltage_max_uv = 4200000;
	fixture->info.factory_internal_resistance_uohm = 150000;
	fixture->info.ocv_table[0] = fixture->ocv;
	fixture->info.ocv_table_size[0] = ARRAY_SIZE(fixture->ocv);
	fixture->info.ocv_temp[0] = 25;
	/* In-memory metadata only, not a DT node or a real battery profile. */
	fixture->psy->battery_info = &fixture->info;
	init_completion(&fixture->reader_started);
	return 0;
}

static int initialize_helper(struct helper_fixture *fixture)
{
	return adc_battery_helper_init(&fixture->helper, fixture->psy,
				       synthetic_acquisition, NULL);
}

static void run_worker(struct helper_fixture *fixture)
{
	mod_delayed_work(system_percpu_wq, &fixture->helper.work, 0);
	flush_delayed_work(&fixture->helper.work);
}

static void preinit_and_estimate(struct kunit *test)
{
	struct helper_fixture *fixture = test->priv;
	union power_supply_propval out = {.intval = 123456};

	KUNIT_EXPECT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), -EAGAIN);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	adc_battery_helper_external_power_changed(fixture->psy);
	KUNIT_EXPECT_EQ(test, atomic_read(&fixture->reads), 0);
	KUNIT_ASSERT_EQ(test, initialize_helper(fixture), 0);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 50);
	KUNIT_EXPECT_FALSE(test, fixture->helper.supplied);
}

static void worker_error_expiry_recovery(struct kunit *test)
{
	struct helper_fixture *fixture = test->priv;
	union power_supply_propval out = {.intval = 123456};

	KUNIT_ASSERT_EQ(test, initialize_helper(fixture), 0);
	atomic_set(&fixture->error, -EIO);
	run_worker(fixture);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), -EIO);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	atomic_set(&fixture->error, 0);
	run_worker(fixture);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 50);
	mutex_lock(&fixture->helper.lock);
	fixture->helper.estimate_boottime_ns = ktime_get_boottime_ns() - 60000000001ULL;
	mutex_unlock(&fixture->helper.lock);
	out.intval = 123456;
	KUNIT_EXPECT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), -ETIME);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	run_worker(fixture);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
}

static int reader_thread(void *data)
{
	struct helper_fixture *fixture = data;
	union power_supply_propval out;
	int ret;

	while (!kthread_should_stop()) {
		ret = power_supply_get_property(fixture->psy, POWER_SUPPLY_PROP_CAPACITY, &out);
		if (ret && ret != -ESHUTDOWN)
			atomic_inc(&fixture->reader_errors);
		if (!ret)
			atomic_inc(&fixture->reader_successes);
		/* The parent must observe an actual read, not just thread startup. */
		complete(&fixture->reader_started);
		cond_resched();
	}
	return 0;
}

static void stop_reader(void *data)
{
	kthread_stop(data);
}

static void quiesce_with_reader(struct kunit *test)
{
	struct helper_fixture *fixture = test->priv;
	struct task_struct *task;
	union power_supply_propval out = {.intval = 123456};
	int reads;

	KUNIT_ASSERT_EQ(test, initialize_helper(fixture), 0);
	task = kthread_run(reader_thread, fixture, "portkit-adc-reader");
	KUNIT_ASSERT_FALSE(test, IS_ERR(task));
	KUNIT_ASSERT_EQ(test, kunit_add_action_or_reset(test, stop_reader, task), 0);
	KUNIT_ASSERT_NE(test, wait_for_completion_timeout(&fixture->reader_started,
		msecs_to_jiffies(2000)), 0UL);
	KUNIT_EXPECT_GT(test, atomic_read(&fixture->reader_successes), 0);
	adc_battery_helper_quiesce(&fixture->helper);
	reads = atomic_read(&fixture->reads);
	adc_battery_helper_external_power_changed(fixture->psy);
	KUNIT_EXPECT_FALSE(test, delayed_work_pending(&fixture->helper.work));
	KUNIT_EXPECT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), -ESHUTDOWN);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	kunit_remove_action(test, stop_reader, task);
	KUNIT_EXPECT_EQ(test, kthread_stop(task), 0);
	KUNIT_EXPECT_EQ(test, atomic_read(&fixture->reads), reads);
	KUNIT_EXPECT_EQ(test, atomic_read(&fixture->reader_errors), 0);
}

static void missing_metadata_keeps_gate_closed(struct kunit *test)
{
	struct helper_fixture *fixture = test->priv;
	union power_supply_propval out = {.intval = 123456};

	fixture->psy->battery_info = NULL;
	KUNIT_EXPECT_EQ(test, initialize_helper(fixture), -ENODEV);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), -EAGAIN);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	KUNIT_EXPECT_EQ(test, atomic_read(&fixture->reads), 0);
}

static void initial_error_is_not_zero_capacity(struct kunit *test)
{
	struct helper_fixture *fixture = test->priv;
	union power_supply_propval out = {.intval = 123456};

	atomic_set(&fixture->error, -EIO);
	KUNIT_ASSERT_EQ(test, initialize_helper(fixture), 0);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), -EIO);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	atomic_set(&fixture->error, 0);
	run_worker(fixture);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(fixture->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 50);
}

static struct kunit_case helper_cases[] = {
	KUNIT_CASE(preinit_and_estimate),
	KUNIT_CASE(worker_error_expiry_recovery),
	KUNIT_CASE(quiesce_with_reader),
	KUNIT_CASE(missing_metadata_keeps_gate_closed),
	KUNIT_CASE(initial_error_is_not_zero_capacity),
	{}
};

static struct kunit_suite helper_suite = {
	.name = "adc-battery-helper-offline",
	.init = create_fixture,
	.test_cases = helper_cases,
};
kunit_test_suite(helper_suite);

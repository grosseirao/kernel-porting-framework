// SPDX-License-Identifier: GPL-2.0-only
/* Upstream helpers and RAM regmap. Never registers the platform driver. */
#include <kunit/test.h>
#include <kunit/resource.h>
#include <kunit/clk.h>
#include <linux/platform_device.h>
#undef builtin_platform_driver
#define builtin_platform_driver(driver)
#include "../../../drivers/pmdomain/mediatek/mtk-pm-domains.c"

/* Exercise the descriptor compiled into the driver, not a parallel copy. */
#define conn_bus_data scpsys_domain_data_mt6765[MT6765_POWER_DOMAIN_CONN]

struct bus_fixture {
	struct device *dev;
	struct regmap *map, *maps[1];
	struct scpsys *scp;
	struct scpsys_domain pd;
	u32 regs[0x340 / 4];
	u32 write_reg[64], write_value[64];
	unsigned int reads, writes, fail_write, fail_read;
	int read_error;
	bool follow_power, keep_ack_on;
};

static int bus_ram_read(void *context, unsigned int reg, unsigned int *value)
{
	struct bus_fixture *f = context;
	f->reads++;
	if (f->read_error && (!f->fail_read || f->fail_read == f->reads))
		return f->read_error;
	if (reg % 4 || reg >= sizeof(f->regs))
		return -EINVAL;
	*value = f->regs[reg / 4];
	return 0;
}

static int bus_ram_write(void *context, unsigned int reg, unsigned int value)
{
	struct bus_fixture *f = context;
	if (f->writes >= ARRAY_SIZE(f->write_reg))
		return -EOVERFLOW;
	f->write_reg[f->writes] = reg;
	f->write_value[f->writes++] = value;
	if (f->fail_write == f->writes)
		return -EIO;
	f->regs[reg / 4] = value;
	if (f->follow_power && reg == 0x32c) {
		u32 requests = value & (PWR_ON_BIT | PWR_ON_2ND_BIT);
		if (requests == (PWR_ON_BIT | PWR_ON_2ND_BIT))
			f->regs[0x180 / 4] = f->regs[0x184 / 4] = BIT(1);
		else if (!requests && !f->keep_ack_on)
			f->regs[0x180 / 4] = f->regs[0x184 / 4] = 0;
	}
	return 0;
}

static const struct regmap_bus bus_ram_ops = {.reg_read = bus_ram_read, .reg_write = bus_ram_write};
static const struct regmap_config bus_ram_config = {
	.reg_bits = 32, .val_bits = 32, .reg_stride = 4, .max_register = 0x33c,
	.cache_type = REGCACHE_NONE,
};

static void bus_fixture_release(void *data)
{
	struct bus_fixture *f = data;
	regmap_exit(f->map);
	root_device_unregister(f->dev);
}

static int bus_fixture_init(struct kunit *test)
{
	struct bus_fixture *f = kunit_kzalloc(test, sizeof(*f), GFP_KERNEL);
	if (!f)
		return -ENOMEM;
	test->priv = f;
	f->scp = kunit_kzalloc(test, sizeof(*f->scp), GFP_KERNEL);
	if (!f->scp)
		return -ENOMEM;
	f->dev = root_device_register("kpf-connsys-bus-ram");
	if (IS_ERR(f->dev))
		return PTR_ERR(f->dev);
	f->map = regmap_init(f->dev, &bus_ram_ops, f, &bus_ram_config);
	if (IS_ERR(f->map)) {
		int ret = PTR_ERR(f->map);
		root_device_unregister(f->dev);
		return ret;
	}
	f->maps[0] = f->map;
	f->scp->dev = f->dev;
	f->scp->bus_prot = f->maps;
	f->pd.scpsys = f->scp;
	f->pd.data = &conn_bus_data;
	f->regs[0x228 / 4] = BIT(13) | BIT(14) | BIT(16);
	f->regs[0x258 / 4] = 0; /* Active-low ACK of SET in bank1. */
	return kunit_add_action_or_reset(test, bus_fixture_release, f);
}

static void conn_assert_and_release_trace(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	KUNIT_ASSERT_EQ(test, scpsys_bus_protect_enable(&f->pd), 0);
	KUNIT_ASSERT_EQ(test, f->writes, 3U);
	KUNIT_EXPECT_EQ(test, f->write_reg[0], 0x2a0U);
	KUNIT_EXPECT_EQ(test, f->write_value[0], BIT(13));
	KUNIT_EXPECT_EQ(test, f->write_reg[1], 0x2a8U); /* SET, not CLR */
	KUNIT_EXPECT_EQ(test, f->write_value[1], BIT(18));
	KUNIT_EXPECT_EQ(test, f->write_value[2], BIT(14) | BIT(16));
	f->writes = f->reads = 0;
	KUNIT_ASSERT_EQ(test, scpsys_bus_protect_disable(&f->pd), 0);
	KUNIT_ASSERT_EQ(test, f->writes, 3U);
	KUNIT_EXPECT_EQ(test, f->write_reg[0], 0x2a4U);
	KUNIT_EXPECT_EQ(test, f->write_value[0], BIT(14) | BIT(16));
	KUNIT_EXPECT_EQ(test, f->write_reg[1], 0x2a4U);
	KUNIT_EXPECT_EQ(test, f->write_value[1], BIT(13));
	KUNIT_EXPECT_EQ(test, f->write_reg[2], 0x2acU);
	KUNIT_EXPECT_EQ(test, f->write_value[2], BIT(18));
	KUNIT_EXPECT_EQ(test, f->reads, 0U); /* Existing IGNORE_CLR_ACK. */
}

static void default_reverse_and_high_ack_preserved(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	struct scpsys_domain_data defaults = conn_bus_data;
	struct scpsys_bus_prot_data high = conn_bus_data.bp_cfg[1];
	defaults.bp_clr_order = NULL;
	f->pd.data = &defaults;
	KUNIT_ASSERT_EQ(test, scpsys_bus_protect_disable(&f->pd), 0);
	KUNIT_EXPECT_EQ(test, f->write_value[0], BIT(14) | BIT(16));
	KUNIT_EXPECT_EQ(test, f->write_value[1], BIT(18));
	KUNIT_EXPECT_EQ(test, f->write_value[2], BIT(13));
	high.flags = 0;
	f->regs[0x258 / 4] = BIT(18);
	KUNIT_EXPECT_EQ(test, scpsys_bus_protect_set(&f->pd, &high), 0);
}

static void invalid_order_rejected_before_io(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	struct scpsys_domain_data bad = conn_bus_data;
	const u8 duplicate[SPM_MAX_BUS_PROT_DATA] = {2, 0, 1, 3, 4, 5, 2};
	const u8 out_of_range[SPM_MAX_BUS_PROT_DATA] = {2, 0, 1, 3, 4, 5, 7};
	f->pd.data = &bad;
	bad.bp_clr_order = duplicate;
	KUNIT_EXPECT_EQ(test, scpsys_bus_protect_disable(&f->pd), -EINVAL);
	bad.bp_clr_order = out_of_range;
	KUNIT_EXPECT_EQ(test, scpsys_bus_protect_disable(&f->pd), -EINVAL);
	KUNIT_EXPECT_EQ(test, f->writes, 0U);
	KUNIT_EXPECT_EQ(test, f->reads, 0U);
}

static void write_errors_not_hidden_by_ack_flags(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	f->fail_write = 1;
	KUNIT_EXPECT_EQ(test, scpsys_bus_protect_enable(&f->pd), -EIO);
	KUNIT_EXPECT_EQ(test, f->writes, 1U);
	KUNIT_EXPECT_EQ(test, f->reads, 0U);
	f->writes = 0;
	KUNIT_EXPECT_EQ(test, scpsys_bus_protect_disable(&f->pd), -EIO);
	KUNIT_EXPECT_EQ(test, f->writes, 1U);
	KUNIT_EXPECT_EQ(test, f->reads, 0U);
}

static void read_error_stops_the_sequence(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	f->read_error = -EIO;
	KUNIT_EXPECT_EQ(test, scpsys_bus_protect_enable(&f->pd), -EIO);
	KUNIT_EXPECT_EQ(test, f->writes, 1U);
	KUNIT_EXPECT_EQ(test, f->reads, 1U);
}

static void wrong_low_ack_times_out_without_next_step(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	f->regs[0x258 / 4] = BIT(18);
	KUNIT_EXPECT_EQ(test, scpsys_bus_protect_enable(&f->pd), -ETIMEDOUT);
	KUNIT_EXPECT_EQ(test, f->writes, 2U);
	KUNIT_EXPECT_GT(test, f->reads, 2U);
}

static const struct scpsys_domain_data conn_status_data = {
	.sta_mask = BIT(1), .pwr_sta_offs = 0x180, .pwr_sta2nd_offs = 0x184,
};

static void both_status_banks_must_agree(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	const struct scpsys_domain_data maskless = {};
	f->scp->base = f->map;
	f->pd.data = &conn_status_data;
	for (int first = 0; first < 2; first++) {
		for (int second = 0; second < 2; second++) {
			f->regs[0x180 / 4] = BIT(10) | (first ? BIT(1) : 0);
			f->regs[0x184 / 4] = BIT(11) | (second ? BIT(1) : 0);
			KUNIT_EXPECT_EQ(test, scpsys_domain_state(&f->pd),
				first == second ? first : 2);
		}
	}
	KUNIT_EXPECT_EQ(test, f->writes, 0U);
	f->pd.data = &maskless;
	f->reads = 0;
	KUNIT_EXPECT_EQ(test, scpsys_domain_state(&f->pd), -EINVAL);
	KUNIT_EXPECT_EQ(test, f->reads, 0U);
}

static void status_read_errors_never_mean_success(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	f->scp->base = f->map;
	f->pd.data = &conn_status_data;
	f->regs[0x180 / 4] = f->regs[0x184 / 4] = BIT(1);
	for (int target = 1; target <= 2; target++) {
		f->reads = 0;
		f->fail_read = target;
		f->read_error = -EIO;
		KUNIT_EXPECT_EQ(test, scpsys_wait_domain_state(&f->pd, true), -EIO);
		KUNIT_EXPECT_EQ(test, f->reads, (unsigned int)target);
	}
	f->reads = 0;
	f->fail_read = 1;
	f->read_error = -EAGAIN;
	KUNIT_EXPECT_EQ(test, scpsys_wait_domain_state(&f->pd, true), -EAGAIN);
	KUNIT_EXPECT_EQ(test, f->reads, 1U); /* Real bus EAGAIN is not retried. */
	KUNIT_EXPECT_EQ(test, f->writes, 0U);
}

static void mixed_off_ack_times_out_and_good_states_pass(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	f->scp->base = f->map;
	f->pd.data = &conn_status_data;
	f->regs[0x180 / 4] = 0;
	f->regs[0x184 / 4] = BIT(1);
	KUNIT_EXPECT_EQ(test, scpsys_wait_domain_state(&f->pd, false), -ETIMEDOUT);
	f->regs[0x184 / 4] = 0;
	KUNIT_EXPECT_EQ(test, scpsys_wait_domain_state(&f->pd, false), 0);
	f->regs[0x180 / 4] = f->regs[0x184 / 4] = BIT(1);
	KUNIT_EXPECT_EQ(test, scpsys_wait_domain_state(&f->pd, true), 0);
	KUNIT_EXPECT_EQ(test, f->writes, 0U);
}

static const struct scpsys_domain_data conn_off_data = {
	.ctl_offs = 0x32c, .pwr_off_primary_first = true,
};

static void off_order_matches_lg_and_default(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	struct scpsys_domain_data data = conn_off_data;
	u32 initial = BIT(20) | PWR_RST_B_BIT | PWR_ON_BIT | PWR_ON_2ND_BIT;
	f->scp->base = f->map;
	f->pd.data = &data;
	for (int primary = 0; primary < 2; primary++) {
		u32 expected = initial;
		data.pwr_off_primary_first = primary;
		f->regs[0x32c / 4] = initial;
		f->writes = f->reads = 0;
		KUNIT_ASSERT_EQ(test, scpsys_ctl_pwrseq_off(&f->pd), 0);
		KUNIT_ASSERT_EQ(test, f->writes, 5U);
		for (int i = 0; i < 5; i++)
			KUNIT_EXPECT_EQ(test, f->write_reg[i], 0x32cU);
		expected |= PWR_ISO_BIT;
		KUNIT_EXPECT_EQ(test, f->write_value[0], expected);
		expected |= PWR_CLK_DIS_BIT;
		KUNIT_EXPECT_EQ(test, f->write_value[1], expected);
		expected &= ~PWR_RST_B_BIT;
		KUNIT_EXPECT_EQ(test, f->write_value[2], expected);
		expected &= ~(primary ? PWR_ON_BIT : PWR_ON_2ND_BIT);
		KUNIT_EXPECT_EQ(test, f->write_value[3], expected);
		expected &= ~(PWR_ON_BIT | PWR_ON_2ND_BIT);
		KUNIT_EXPECT_EQ(test, f->write_value[4], expected);
		KUNIT_EXPECT_EQ(test, f->regs[0x32c / 4], expected);
	}
}

static void off_io_error_stops_before_next_request(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	f->scp->base = f->map;
	f->pd.data = &conn_off_data;
	for (int read_failure = 0; read_failure < 2; read_failure++) {
		for (int target = 1; target <= 5; target++) {
			f->regs[0x32c / 4] = PWR_RST_B_BIT | PWR_ON_BIT | PWR_ON_2ND_BIT;
			f->reads = f->writes = 0;
			f->fail_read = read_failure ? target : 0;
			f->read_error = read_failure ? -EIO : 0;
			f->fail_write = read_failure ? 0 : target;
			KUNIT_EXPECT_EQ(test, scpsys_ctl_pwrseq_off(&f->pd), -EIO);
			KUNIT_EXPECT_EQ(test, f->reads, (unsigned int)target);
			KUNIT_EXPECT_EQ(test, f->writes, (unsigned int)(target - read_failure));
		}
	}
}

static void setup_strict_conn(struct bus_fixture *f, struct scpsys_domain_data *data)
{
	f->pd.data = data;
	f->scp->base = f->map;
	f->follow_power = true;
	f->regs[0x32c / 4] = PWR_ISO_BIT | PWR_CLK_DIS_BIT;
}

struct conn_ram_clock {
	struct clk_bulk_data bulk;
	struct clk_hw *hw;
};

static void unregister_ram_clock(void *hw)
{
	clk_hw_unregister_fixed_rate(hw);
}

static void release_ram_clock_reference(void *arg)
{
	struct conn_ram_clock *clock = arg;
	/* Test teardown only; production recovery remains reset, not forced release. */
	while (__clk_get_enable_count(clock->bulk.clk))
		clk_disable_unprepare(clock->bulk.clk);
}

static struct conn_ram_clock *new_ram_clock(struct kunit *test, const char *name)
{
	struct conn_ram_clock *clock = kunit_kzalloc(test, sizeof(*clock), GFP_KERNEL);
	struct clk_hw *hw;
	if (!clock)
		return NULL;
	hw = clk_hw_register_fixed_rate(NULL, name, NULL, 0, 1000000);
	if (IS_ERR(hw))
		return NULL;
	clock->hw = hw;
	if (kunit_add_action_or_reset(test, unregister_ram_clock, hw))
		return NULL;
	clock->bulk.clk = clk_hw_get_clk_kunit(test, hw, NULL);
	if (IS_ERR(clock->bulk.clk))
		return NULL;
	if (kunit_add_action_or_reset(test, release_ram_clock_reference, clock))
		return NULL;
	return clock;
}

static void strict_on_off_callbacks(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	struct scpsys_domain_data data = conn_bus_data;
	struct conn_ram_clock *main = new_ram_clock(test, "connsys-main");
	struct conn_ram_clock *subsys = new_ram_clock(test, "connsys-subsys");
	KUNIT_ASSERT_NOT_NULL(test, main);
	KUNIT_ASSERT_NOT_NULL(test, subsys);
	setup_strict_conn(f, &data);
	f->pd.clks = &main->bulk;
	f->pd.num_clks = 1;
	f->pd.subsys_clks = &subsys->bulk;
	f->pd.num_subsys_clks = 1;
	KUNIT_ASSERT_EQ(test, scpsys_power_on(&f->pd.genpd), 0);
	KUNIT_EXPECT_EQ(test, __clk_get_enable_count(main->bulk.clk), 1U);
	KUNIT_EXPECT_EQ(test, __clk_get_enable_count(subsys->bulk.clk), 1U);
	KUNIT_EXPECT_TRUE(test, clk_hw_is_prepared(main->hw));
	KUNIT_EXPECT_TRUE(test, clk_hw_is_prepared(subsys->hw));
	KUNIT_EXPECT_EQ(test, scpsys_domain_state(&f->pd), 1);
	KUNIT_EXPECT_EQ(test, f->regs[0x32c / 4],
		(u32)(PWR_RST_B_BIT | PWR_ON_BIT | PWR_ON_2ND_BIT));
	KUNIT_ASSERT_EQ(test, scpsys_power_off(&f->pd.genpd), 0);
	KUNIT_EXPECT_EQ(test, __clk_get_enable_count(main->bulk.clk), 0U);
	KUNIT_EXPECT_EQ(test, __clk_get_enable_count(subsys->bulk.clk), 0U);
	KUNIT_EXPECT_FALSE(test, clk_hw_is_prepared(main->hw));
	KUNIT_EXPECT_FALSE(test, clk_hw_is_prepared(subsys->hw));
	KUNIT_EXPECT_EQ(test, scpsys_domain_state(&f->pd), 0);
	KUNIT_EXPECT_EQ(test, f->regs[0x32c / 4], (u32)(PWR_ISO_BIT | PWR_CLK_DIS_BIT));
	KUNIT_EXPECT_FALSE(test, f->pd.recovery_required);
}

static void strict_failed_release_restores_off(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	struct scpsys_domain_data data = conn_bus_data;
	setup_strict_conn(f, &data);
	/* Fail first power request, then first bus release after fully ON. */
	for (int target = 4; target <= 9; target += 5) {
		f->writes = f->reads = 0;
		f->fail_write = target;
		KUNIT_EXPECT_EQ(test, scpsys_power_on(&f->pd.genpd), -EIO);
		KUNIT_EXPECT_EQ(test, scpsys_domain_state(&f->pd), 0);
		KUNIT_EXPECT_FALSE(test, f->pd.recovery_required);
		KUNIT_EXPECT_EQ(test, f->regs[0x32c / 4], (u32)(PWR_ISO_BIT | PWR_CLK_DIS_BIT));
		f->fail_write = 0;
		KUNIT_ASSERT_EQ(test, scpsys_power_on(&f->pd.genpd), 0);
		KUNIT_ASSERT_EQ(test, scpsys_power_off(&f->pd.genpd), 0);
	}
}

static void strict_failed_rollback_blocks_until_reset(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	struct scpsys_domain_data data = conn_bus_data;
	struct conn_ram_clock *main = new_ram_clock(test, "connsys-main");
	struct conn_ram_clock *subsys = new_ram_clock(test, "connsys-subsys");
	unsigned int reads, writes;
	KUNIT_ASSERT_NOT_NULL(test, main);
	KUNIT_ASSERT_NOT_NULL(test, subsys);
	setup_strict_conn(f, &data);
	f->pd.clks = &main->bulk;
	f->pd.num_clks = 1;
	f->pd.subsys_clks = &subsys->bulk;
	f->pd.num_subsys_clks = 1;
	f->fail_write = 9;
	f->keep_ack_on = true;
	KUNIT_EXPECT_EQ(test, scpsys_power_on(&f->pd.genpd), -EIO);
	KUNIT_EXPECT_TRUE(test, f->pd.recovery_required);
	KUNIT_EXPECT_EQ(test, __clk_get_enable_count(main->bulk.clk), 1U);
	KUNIT_EXPECT_EQ(test, __clk_get_enable_count(subsys->bulk.clk), 1U);
	reads = f->reads;
	writes = f->writes;
	KUNIT_EXPECT_EQ(test, scpsys_power_on(&f->pd.genpd), -EIO);
	KUNIT_EXPECT_EQ(test, scpsys_power_off(&f->pd.genpd), -EIO);
	KUNIT_EXPECT_EQ(test, f->reads, reads);
	KUNIT_EXPECT_EQ(test, f->writes, writes);
	KUNIT_EXPECT_EQ(test, __clk_get_enable_count(main->bulk.clk), 1U);
	KUNIT_EXPECT_EQ(test, __clk_get_enable_count(subsys->bulk.clk), 1U);
}

static void strict_handoff_rejects_unknown_states(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	struct scpsys_domain_data data = conn_bus_data;
	setup_strict_conn(f, &data);
	f->regs[0x180 / 4] = BIT(1);
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), -EBUSY);
	f->regs[0x184 / 4] = BIT(1);
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), -EBUSY);
	f->read_error = -EIO;
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), -EIO);
	f->read_error = 0;
	f->regs[0x180 / 4] = f->regs[0x184 / 4] = 0;
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), 0);
	f->regs[0x32c / 4] |= PWR_ON_BIT;
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), -EBUSY);
	f->regs[0x32c / 4] = PWR_ISO_BIT | PWR_CLK_DIS_BIT;
	f->read_error = -EIO;
	f->fail_read = 3;
	f->reads = 0;
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), -EIO);
	f->read_error = 0;
	data.rtff_type = SCPSYS_RTFF_TYPE_GENERIC;
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), -EINVAL);
	data.rtff_type = SCPSYS_RTFF_NONE;
	data.sram_pdn_bits = BIT(8);
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), -EINVAL);
	data.sram_pdn_bits = 0;
	data.caps = 0;
	KUNIT_EXPECT_EQ(test, scpsys_strict_off_handoff(&f->pd), -EINVAL);
	KUNIT_EXPECT_EQ(test, f->writes, 0U);
}

static void on_io_errors_propagate(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	struct scpsys_domain_data data = conn_bus_data;
	setup_strict_conn(f, &data);
	/* The helper alone does not roll back: its caller must do so. */
	for (int target = 1; target <= 5; target++) {
		f->regs[0x32c / 4] = PWR_ISO_BIT | PWR_CLK_DIS_BIT;
		f->writes = f->reads = 0;
		f->fail_write = target;
		KUNIT_EXPECT_EQ(test, scpsys_ctl_pwrseq_on(&f->pd), -EIO);
		KUNIT_EXPECT_EQ(test, f->writes, (unsigned int)target);
	}
}

static void missing_access_controller_rejected_before_io(struct kunit *test)
{
	struct bus_fixture *f = test->priv;
	f->scp->soc_data = &mt6765_scpsys_data;
	KUNIT_ASSERT_TRUE(test, mt6765_scpsys_data.require_access_controllers);
	/* No OF node/phandle: the required getter must reject before allocation/I/O. */
	KUNIT_EXPECT_EQ(test, scpsys_get_bus_protection(f->dev, f->scp), -EINVAL);
	KUNIT_EXPECT_EQ(test, f->reads, 0U);
	KUNIT_EXPECT_EQ(test, f->writes, 0U);
}

static struct kunit_case connsys_cases[] = {
	KUNIT_CASE(missing_access_controller_rejected_before_io),
	KUNIT_CASE(strict_on_off_callbacks),
	KUNIT_CASE(strict_failed_release_restores_off),
	KUNIT_CASE(strict_failed_rollback_blocks_until_reset),
	KUNIT_CASE(strict_handoff_rejects_unknown_states),
	KUNIT_CASE(on_io_errors_propagate),
	KUNIT_CASE(off_order_matches_lg_and_default),
	KUNIT_CASE(off_io_error_stops_before_next_request),
	KUNIT_CASE(conn_assert_and_release_trace),
	KUNIT_CASE(default_reverse_and_high_ack_preserved),
	KUNIT_CASE(invalid_order_rejected_before_io),
	KUNIT_CASE(write_errors_not_hidden_by_ack_flags),
	KUNIT_CASE(read_error_stops_the_sequence),
	KUNIT_CASE(wrong_low_ack_times_out_without_next_step),
	KUNIT_CASE(both_status_banks_must_agree),
	KUNIT_CASE(status_read_errors_never_mean_success),
	KUNIT_CASE(mixed_off_ack_times_out_and_good_states_pass),
	{}
};
static struct kunit_suite connsys_suite = {
	.name = "mt6765-connsys-bus-offline",
	.init = bus_fixture_init,
	.test_cases = connsys_cases,
};
kunit_test_suite(connsys_suite);

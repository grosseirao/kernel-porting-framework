// SPDX-License-Identifier: GPL-2.0-only
/* Real consumer, helper, IIO/core and software-node metadata; RAM only.
 * The helper is linked by adc_battery_helper_test.c, not duplicated here.
 */
#include <kunit/test.h>
#include <kunit/resource.h>
#include <linux/delay.h>
#include <linux/iio/driver.h>
#include <linux/iio/iio.h>
#include <linux/iio/machine.h>
#include <linux/platform_device.h>
#include <linux/property.h>

/* No platform bus autoprobes: tests call the actual probe explicitly. */
#undef module_platform_driver
#define module_platform_driver(driver)
#include "../../../drivers/power/supply/generic-adc-battery.c"

struct consumer_fixture {
	struct device *root;
	struct platform_device *pdev;
	struct iio_dev *iio;
	atomic_t reads, error, temp_millicelsius, temp_error;
	atomic_t supplier_status, supplier_error;
	bool battery_registered;
	bool consumer_registered;
};

static const u32 synthetic_ocv[] = {4200000, 100, 3200000, 0};
static const u32 synthetic_ocv_hot[] = {4400000, 100, 3400000, 0};
static const u32 synthetic_temperatures[] = {25, 50};
static const struct property_entry synthetic_battery_properties[] = {
	PROPERTY_ENTRY_STRING("compatible", "simple-battery"),
	PROPERTY_ENTRY_U32("constant-charge-voltage-max-microvolt", 4200000),
	PROPERTY_ENTRY_U32("factory-internal-resistance-micro-ohms", 150000),
	PROPERTY_ENTRY_U32_ARRAY("ocv-capacity-celsius", synthetic_temperatures),
	PROPERTY_ENTRY_U32_ARRAY("ocv-capacity-table-0", synthetic_ocv),
	PROPERTY_ENTRY_U32_ARRAY("ocv-capacity-table-1", synthetic_ocv_hot),
	{}
};
static const struct software_node synthetic_battery_node = {
	.name = "portkit-synthetic-battery",
	.properties = synthetic_battery_properties,
};
static const struct property_entry synthetic_consumer_properties[] = {
	PROPERTY_ENTRY_REF("monitored-battery", &synthetic_battery_node),
	{}
};
static const struct software_node synthetic_consumer_node = {
	.name = "portkit-synthetic-consumer",
	.properties = synthetic_consumer_properties,
};

static const struct iio_chan_spec synthetic_channels[] = {
	{ .type = IIO_VOLTAGE, .indexed = 1, .channel = 0,
	  .datasheet_name = "v", .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED) },
	{ .type = IIO_CURRENT, .indexed = 1, .channel = 1,
	  .datasheet_name = "i", .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED) },
	{ .type = IIO_TEMP, .indexed = 1, .channel = 2,
	  .datasheet_name = "t", .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED) },
};
static const struct iio_map synthetic_maps[] = {
	IIO_MAP("v", "portkit-adc-consumer", "voltage"),
	IIO_MAP("i", "portkit-adc-consumer", "current"),
	IIO_MAP("t", "portkit-adc-consumer", "temperature"),
	{}
};

static int synthetic_iio_read(struct iio_dev *iio, const struct iio_chan_spec *chan,
			      int *val, int *val2, long mask)
{
	struct consumer_fixture *fixture = *(struct consumer_fixture **)iio_priv(iio);
	int error = atomic_read(&fixture->error);

	atomic_inc(&fixture->reads);
	if (error)
		return error;
	if (mask != IIO_CHAN_INFO_PROCESSED)
		return -EINVAL;
	if (chan->type == IIO_TEMP) {
		if (atomic_read(&fixture->temp_error))
			return atomic_read(&fixture->temp_error);
		*val = atomic_read(&fixture->temp_millicelsius);
		return IIO_VAL_INT;
	}
	*val = chan->type == IIO_VOLTAGE ? 3700000 : 0;
	*val2 = 1000;
	return IIO_VAL_FRACTIONAL;
}
static const struct iio_info synthetic_iio_info = { .read_raw = synthetic_iio_read };

static void release_consumer_fixture(void *data)
{
	struct consumer_fixture *fixture = data;

	if (fixture->pdev) {
		/* Parent was already registered before receiving the primary node.
		 * Only the power_supply child owns a sysfs notification/reference.
		 * Detach before parent device_del can notify_remove a second time.
		 */
		device_set_node(&fixture->pdev->dev, NULL);
		platform_device_unregister(fixture->pdev);
	}
	if (fixture->consumer_registered)
		software_node_unregister(&synthetic_consumer_node);
	if (fixture->battery_registered)
		software_node_unregister(&synthetic_battery_node);
	root_device_unregister(fixture->root);
	estimate_capacity = false;
	paired_input = false;
	status_from_supplier = false;
}

static int create_consumer_fixture(struct kunit *test)
{
	struct consumer_fixture *fixture;
	int ret;

	fixture = kunit_kzalloc(test, sizeof(*fixture), GFP_KERNEL);
	if (!fixture)
		return -ENOMEM;
	test->priv = fixture;
	atomic_set(&fixture->temp_millicelsius, 32000);
	fixture->root = root_device_register("portkit-adc-consumer-root");
	if (IS_ERR(fixture->root))
		return PTR_ERR(fixture->root);
	ret = kunit_add_action_or_reset(test, release_consumer_fixture, fixture);
	if (ret)
		return ret;
	fixture->iio = devm_iio_device_alloc(fixture->root, sizeof(fixture));
	if (!fixture->iio)
		return -ENOMEM;
	*(struct consumer_fixture **)iio_priv(fixture->iio) = fixture;
	fixture->iio->name = "portkit-ram-adc";
	fixture->iio->info = &synthetic_iio_info;
	fixture->iio->channels = synthetic_channels;
	fixture->iio->num_channels = ARRAY_SIZE(synthetic_channels);
	fixture->iio->modes = INDIO_DIRECT_MODE;
	ret = devm_iio_device_register(fixture->root, fixture->iio);
	if (ret)
		return ret;
	ret = devm_iio_map_array_register(fixture->root, fixture->iio, synthetic_maps);
	if (ret)
		return ret;
	fixture->pdev = platform_device_register_simple("portkit-adc-consumer",
						       PLATFORM_DEVID_NONE, NULL, 0);
	if (IS_ERR(fixture->pdev)) {
		ret = PTR_ERR(fixture->pdev);
		fixture->pdev = NULL;
		return ret;
	}
	estimate_capacity = true;
	paired_input = true;
	return 0;
}

static int add_synthetic_metadata(struct consumer_fixture *fixture)
{
	int ret = software_node_register(&synthetic_battery_node);

	if (ret)
		return ret;
	fixture->battery_registered = true;
	ret = software_node_register(&synthetic_consumer_node);
	if (ret)
		return ret;
	fixture->consumer_registered = true;
	/* Do not share a managed node between parent and child, whose names
	 * intentionally match in the real generic-adc-battery driver.
	 */
	device_set_node(&fixture->pdev->dev,
			software_node_fwnode(&synthetic_consumer_node));
	return 0;
}

static void consumer_metadata_and_measurements(struct kunit *test)
{
	struct consumer_fixture *fixture = test->priv;
	struct gab *gab;
	union power_supply_propval out;

	KUNIT_ASSERT_EQ(test, add_synthetic_metadata(fixture), 0);
	KUNIT_ASSERT_EQ(test, gab_probe(fixture->pdev), 0);
	gab = platform_get_drvdata(fixture->pdev);
	KUNIT_ASSERT_TRUE(test, gab->helper.initialized);
	KUNIT_EXPECT_EQ(test, gab->psy_desc.num_properties, 8);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 50);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_VOLTAGE_NOW, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 3700000);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_TEMP, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 320);
}

static void consumer_missing_metadata(struct kunit *test)
{
	struct consumer_fixture *fixture = test->priv;
	void *group = devres_open_group(&fixture->pdev->dev, NULL, GFP_KERNEL);

	KUNIT_ASSERT_NOT_NULL(test, group);
	KUNIT_EXPECT_EQ(test, gab_probe(fixture->pdev), -ENODEV);
	KUNIT_EXPECT_EQ(test, atomic_read(&fixture->reads), 0);
	devres_release_group(&fixture->pdev->dev, group);
}

static void consumer_acquisition_error_recovery(struct kunit *test)
{
	struct consumer_fixture *fixture = test->priv;
	struct gab *gab;
	union power_supply_propval out = {.intval = 123456};

	KUNIT_ASSERT_EQ(test, add_synthetic_metadata(fixture), 0);
	atomic_set(&fixture->error, -EIO);
	KUNIT_ASSERT_EQ(test, gab_probe(fixture->pdev), 0);
	gab = platform_get_drvdata(fixture->pdev);
	KUNIT_EXPECT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), -EIO);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	atomic_set(&fixture->error, 0);
	mod_delayed_work(system_percpu_wq, &gab->helper.work, 0);
	flush_delayed_work(&gab->helper.work);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 50);
}

static void consumer_temperature_table_and_error(struct kunit *test)
{
	struct consumer_fixture *fixture = test->priv;
	struct gab *gab;
	union power_supply_propval out = {.intval = 123456};

	KUNIT_ASSERT_EQ(test, add_synthetic_metadata(fixture), 0);
	KUNIT_ASSERT_EQ(test, gab_probe(fixture->pdev), 0);
	gab = platform_get_drvdata(fixture->pdev);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 50);
	atomic_set(&fixture->temp_millicelsius, 50000);
	mod_delayed_work(system_percpu_wq, &gab->helper.work, 0);
	flush_delayed_work(&gab->helper.work);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 30);
	atomic_set(&fixture->temp_error, -EIO);
	mod_delayed_work(system_percpu_wq, &gab->helper.work, 0);
	flush_delayed_work(&gab->helper.work);
	out.intval = 123456;
	KUNIT_EXPECT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), -EIO);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	atomic_set(&fixture->temp_error, 0);
	mod_delayed_work(system_percpu_wq, &gab->helper.work, 0);
	flush_delayed_work(&gab->helper.work);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 30);
}

static const enum power_supply_property synthetic_supplier_props[] = {
	POWER_SUPPLY_PROP_ONLINE, POWER_SUPPLY_PROP_STATUS,
};

static int synthetic_supplier_get(struct power_supply *psy,
		enum power_supply_property prop, union power_supply_propval *out)
{
	struct consumer_fixture *fixture = power_supply_get_drvdata(psy);

	if (prop == POWER_SUPPLY_PROP_ONLINE) {
		out->intval = 1;
		return 0;
	}
	if (prop != POWER_SUPPLY_PROP_STATUS)
		return -EINVAL;
	if (atomic_read(&fixture->supplier_error))
		return atomic_read(&fixture->supplier_error);
	out->intval = atomic_read(&fixture->supplier_status);
	return 0;
}

static const struct power_supply_desc synthetic_supplier_desc = {
	.name = "portkit-measured-status",
	.type = POWER_SUPPLY_TYPE_MAINS,
	.properties = synthetic_supplier_props,
	.num_properties = ARRAY_SIZE(synthetic_supplier_props),
	.get_property = synthetic_supplier_get,
};

static void consumer_measured_supplier_status(struct kunit *test)
{
	struct consumer_fixture *fixture = test->priv;
	static char *supplied_to[] = {"portkit-adc-consumer"};
	struct power_supply_config config = {
		.drv_data = fixture, .supplied_to = supplied_to,
		.num_supplicants = ARRAY_SIZE(supplied_to),
	};
	struct power_supply *supplier;
	struct gab *gab;
	union power_supply_propval out = {.intval = 123456};
	int status, polls;

	status_from_supplier = true;
	atomic_set(&fixture->supplier_status, POWER_SUPPLY_STATUS_NOT_CHARGING);
	supplier = devm_power_supply_register(fixture->root, &synthetic_supplier_desc, &config);
	KUNIT_ASSERT_FALSE(test, IS_ERR(supplier));
	KUNIT_ASSERT_EQ(test, add_synthetic_metadata(fixture), 0);
	KUNIT_ASSERT_EQ(test, gab_probe(fixture->pdev), 0);
	gab = platform_get_drvdata(fixture->pdev);
	KUNIT_ASSERT_TRUE(test, gab->helper.initialized);
	for (status = POWER_SUPPLY_STATUS_UNKNOWN; status <= POWER_SUPPLY_STATUS_FULL; status++) {
		atomic_set(&fixture->supplier_status, status);
		KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
			POWER_SUPPLY_PROP_STATUS, &out), 0);
		KUNIT_EXPECT_EQ(test, out.intval, status);
	}
	atomic_set(&fixture->supplier_error, -EIO);
	out.intval = 123456;
	KUNIT_EXPECT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_STATUS, &out), -ENODEV);
	KUNIT_EXPECT_EQ(test, out.intval, 123456);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 50);
	atomic_set(&fixture->supplier_error, 0);
	polls = gab->helper.poll_count;
	gab_ext_power_changed(gab->psy);
	flush_delayed_work(&gab->helper.work);
	KUNIT_EXPECT_GT(test, gab->helper.poll_count, polls);
	KUNIT_ASSERT_EQ(test, gab_suspend(&fixture->pdev->dev), 0);
	KUNIT_ASSERT_EQ(test, gab_resume(&fixture->pdev->dev), 0);
	KUNIT_ASSERT_EQ(test, power_supply_get_property(gab->psy,
		POWER_SUPPLY_PROP_CAPACITY, &out), 0);
	KUNIT_EXPECT_EQ(test, out.intval, 50);
}

static void consumer_pm_and_devres_cancel(struct kunit *test)
{
	struct consumer_fixture *fixture = test->priv;
	struct gab *gab;
	void *group;
	int before;

	KUNIT_ASSERT_EQ(test, add_synthetic_metadata(fixture), 0);
	group = devres_open_group(&fixture->pdev->dev, NULL, GFP_KERNEL);
	KUNIT_ASSERT_NOT_NULL(test, group);
	KUNIT_ASSERT_EQ(test, gab_probe(fixture->pdev), 0);
	gab = platform_get_drvdata(fixture->pdev);
	/* Core registration/uevent work may legitimately read V/I/T. Drain it
	 * before asserting that the suspended helper no longer acquires data.
	 */
	flush_delayed_work(&gab->psy->deferred_register_work);
	flush_work(&gab->psy->changed_work);
	KUNIT_ASSERT_EQ(test, gab_suspend(&fixture->pdev->dev), 0);
	before = atomic_read(&fixture->reads);
	msleep(20);
	KUNIT_EXPECT_EQ(test, atomic_read(&fixture->reads), before);
	KUNIT_ASSERT_EQ(test, gab_resume(&fixture->pdev->dev), 0);
	KUNIT_EXPECT_GT(test, atomic_read(&fixture->reads), before);
	flush_work(&gab->psy->changed_work);
	devres_release_group(&fixture->pdev->dev, group);
	/* gab has been freed: never dereference it after releasing the group. */
	before = atomic_read(&fixture->reads);
	msleep(20);
	KUNIT_EXPECT_EQ(test, atomic_read(&fixture->reads), before);
}

static struct kunit_case consumer_cases[] = {
	KUNIT_CASE(consumer_metadata_and_measurements),
	KUNIT_CASE(consumer_missing_metadata),
	KUNIT_CASE(consumer_acquisition_error_recovery),
	KUNIT_CASE(consumer_pm_and_devres_cancel),
	KUNIT_CASE(consumer_temperature_table_and_error),
	KUNIT_CASE(consumer_measured_supplier_status),
	{}
};
static struct kunit_suite consumer_suite = {
	.name = "generic-adc-helper-consumer-offline",
	.init = create_consumer_fixture,
	.test_cases = consumer_cases,
};
kunit_test_suite(consumer_suite);

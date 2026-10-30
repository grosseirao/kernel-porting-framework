// SPDX-License-Identifier: GPL-2.0-only
/* Pure LG-derived divider encoding; no device, MMIO, DMA or clock provider. */
#include <kunit/test.h>
#include <linux/module.h>
#include "mt6765-i2c-timing.h"

static void divider_vectors(struct kunit *test)
{
	unsigned int step, sample;

	KUNIT_ASSERT_EQ(test, mt6765_i2c_calculate_speed(5200000, 100000, &step, &sample), 0);
	KUNIT_EXPECT_EQ(test, step, 26U);
	KUNIT_EXPECT_EQ(test, sample, 0U);
	KUNIT_ASSERT_EQ(test, mt6765_i2c_calculate_speed(5200000, 444444, &step, &sample), 0);
	KUNIT_EXPECT_EQ(test, step, 6U);
	KUNIT_EXPECT_EQ(test, sample, 0U);
	KUNIT_ASSERT_EQ(test, mt6765_i2c_calculate_speed(27300000, 444444, &step, &sample), 0);
	KUNIT_EXPECT_EQ(test, step, 7U);
	KUNIT_EXPECT_EQ(test, sample, 3U);
}

static void divider_encoding_and_donor_khz_bound(struct kunit *test)
{
	static const unsigned int sources[] = {5200000, 26000000, 27300000, 104000000};
	unsigned int i, target;

	for (i = 0; i < ARRAY_SIZE(sources); i++) {
		for (target = 1000; target <= 444444; target += 997) {
			unsigned int step = 123, sample = 234, divisor;
			int ret = mt6765_i2c_calculate_speed(sources[i], target, &step, &sample);

			if (ret) {
				KUNIT_EXPECT_EQ(test, step, 123U);
				KUNIT_EXPECT_EQ(test, sample, 234U);
				continue;
			}
			KUNIT_ASSERT_LT(test, sample, 8U);
			KUNIT_ASSERT_LE(test, step, target > 400000 ? 8U : 64U);
			divisor = (sample + 1) * (step + (sample != 0));
			KUNIT_ASSERT_GT(test, divisor, 0U);
			KUNIT_EXPECT_LE(test, (sources[i] / 1000) / (2 * divisor), target / 1000);
		}
	}
}

static void invalid_dividers_preserve_outputs(struct kunit *test)
{
	unsigned int step = 123, sample = 234;

	KUNIT_EXPECT_EQ(test, mt6765_i2c_calculate_speed(1, 100000, &step, &sample), -EINVAL);
	KUNIT_EXPECT_EQ(test, mt6765_i2c_calculate_speed(26000000, 0, &step, &sample), -EINVAL);
	KUNIT_EXPECT_EQ(test, mt6765_i2c_calculate_speed(26000000, 3400001, &step, &sample), -EINVAL);
	KUNIT_EXPECT_EQ(test, mt6765_i2c_calculate_speed(26000000, 100000, NULL, &sample), -EINVAL);
	KUNIT_EXPECT_EQ(test, mt6765_i2c_calculate_speed(26000000, 100000, &step, NULL), -EINVAL);
	KUNIT_EXPECT_EQ(test, mt6765_i2c_calculate_speed(1000000000, 1000, &step, &sample), -ERANGE);
	KUNIT_EXPECT_EQ(test, step, 123U);
	KUNIT_EXPECT_EQ(test, sample, 234U);
}

static struct kunit_case mt6765_timing_cases[] = {
	KUNIT_CASE(divider_vectors),
	KUNIT_CASE(divider_encoding_and_donor_khz_bound),
	KUNIT_CASE(invalid_dividers_preserve_outputs),
	{}
};
static struct kunit_suite mt6765_timing_suite = {
	.name = "mt6765-i2c-timing-offline",
	.test_cases = mt6765_timing_cases,
};
kunit_test_suite(mt6765_timing_suite);
MODULE_LICENSE("GPL");

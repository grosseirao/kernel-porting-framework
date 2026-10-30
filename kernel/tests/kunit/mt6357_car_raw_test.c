// SPDX-License-Identifier: GPL-2.0-only
/* Pure chip layout: no acquisition, calibration, power_supply or MMIO. */
#include <kunit/test.h>
#include <linux/errno.h>
#include <linux/module.h>
#include "mt6357-car-raw.h"

static void all_car_payloads(struct kunit *test)
{
	unsigned int payload;

	for (payload = 0; payload < (1U << 21); payload++) {
		unsigned int count = payload & 0xfffffU, sign = payload >> 20;
		bool special = count == 0 || count == 0xfffffU;
		struct mt6357_car_raw raw;

		KUNIT_ASSERT_EQ(test, mt6357_car_decode_raw(
			((count & 31) << 11) | (payload & 0x7ff),
			(count >> 5) | (sign << 15), &raw), 0);
		KUNIT_EXPECT_EQ(test, raw.count, count);
		KUNIT_EXPECT_EQ(test, raw.sign, sign);
		KUNIT_EXPECT_EQ(test, raw.zero_special, special);
		KUNIT_EXPECT_EQ(test, raw.magnitude,
			special ? 0U : (sign ? 0xfffffU - count : count));
	}
}

static void ignored_bits_and_sentinels(struct kunit *test)
{
	unsigned int ignored, sign, terminal;

	for (sign = 0; sign < 2; sign++) {
		for (terminal = 0; terminal < 2; terminal++) {
			unsigned int count = terminal ? 0xfffffU : 0;

			for (ignored = 0; ignored < 2048; ignored++) {
				struct mt6357_car_raw raw;

				KUNIT_ASSERT_EQ(test, mt6357_car_decode_raw(
					((count & 31) << 11) | ignored,
					(count >> 5) | (sign << 15), &raw), 0);
				KUNIT_EXPECT_EQ(test, raw.count, count);
				KUNIT_EXPECT_EQ(test, raw.sign, sign);
				KUNIT_EXPECT_TRUE(test, raw.zero_special);
				KUNIT_EXPECT_EQ(test, raw.magnitude, 0U);
			}
		}
	}
}

static void invalid_inputs_preserve_output(struct kunit *test)
{
	struct mt6357_car_raw raw = {123, 1, 456, true};

	KUNIT_EXPECT_EQ(test, mt6357_car_decode_raw(65536, 0, &raw), -ERANGE);
	KUNIT_EXPECT_EQ(test, mt6357_car_decode_raw(0, 65536, &raw), -ERANGE);
	KUNIT_EXPECT_EQ(test, mt6357_car_decode_raw(~0U, ~0U, &raw), -ERANGE);
	KUNIT_EXPECT_EQ(test, mt6357_car_decode_raw(0, 0, NULL), -EINVAL);
	KUNIT_EXPECT_EQ(test, raw.count, 123U);
	KUNIT_EXPECT_EQ(test, raw.sign, 1U);
	KUNIT_EXPECT_EQ(test, raw.magnitude, 456U);
	KUNIT_EXPECT_TRUE(test, raw.zero_special);
}

static struct kunit_case mt6357_car_cases[] = {
	KUNIT_CASE(all_car_payloads),
	KUNIT_CASE(ignored_bits_and_sentinels),
	KUNIT_CASE(invalid_inputs_preserve_output),
	{}
};
static struct kunit_suite mt6357_car_suite = {
	.name = "mt6357-car-raw-offline",
	.test_cases = mt6357_car_cases,
};
kunit_test_suite(mt6357_car_suite);
MODULE_LICENSE("GPL");

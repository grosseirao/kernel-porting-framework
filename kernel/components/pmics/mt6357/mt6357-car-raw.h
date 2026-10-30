/* SPDX-License-Identifier: GPL-2.0-only */
#ifndef PORTKIT_MT6357_CAR_RAW_H
#define PORTKIT_MT6357_CAR_RAW_H
/* MT6357 CAR_CON0/CAR_CON1 layout, derived from the reviewed LG routine.
 * Pure decoding only. Caller provides bool and errno definitions.
 * No calibration, physical units, latch, I/O, reset, capacity or SOC policy.
 */
struct mt6357_car_raw {
	unsigned int count, sign, magnitude;
	bool zero_special;
};

static inline int mt6357_car_decode_raw(unsigned int low, unsigned int high,
		struct mt6357_car_raw *out)
{
	struct mt6357_car_raw next = {};

	if (!out)
		return -EINVAL;
	if (low > 65535 || high > 65535)
		return -ERANGE;
	next.count = (low >> 11) | ((high & 0x7fff) << 5);
	next.sign = high >> 15;
	next.zero_special = !next.count || next.count == 0xfffff;
	if (!next.zero_special)
		next.magnitude = next.sign ? 0xfffff - next.count : next.count;
	*out = next;
	return 0;
}
#endif

/* SPDX-License-Identifier: GPL-2.0-only */
/* Reuses reviewed READ1/CLEAR8/IDLE0 latch protocol. Unlike the original
 * LG coulomb routine's 0x1f05 mask, never touches reset/reserved fields.
 * Only CAR_CON0/1 are read, under the latch; no counter reset or enable.
 */
#ifndef PORTKIT_MT6357_CAR_LATCH_H
#define PORTKIT_MT6357_CAR_LATCH_H

/* Caller supplies regmap/errno/string/bool APIs and holds PMIC exclusion.
 * Poll timing is the reviewed envelope, not a configurable chip capability.
 */
struct mt6357_car_sample {
	unsigned int low, high, con0_before, con1_before;
	int cleanup_error;
};
static inline int mt6357_car_once(struct regmap *map, struct mt6357_car_sample *s,
				   bool (*allow_latch)(unsigned int, unsigned int))
{
	unsigned int value, low = 0, high = 0;
	int ret, err;
	if (!map || !s || !allow_latch) return -EINVAL;
	memset(s, 0, sizeof(*s));
	ret = regmap_read(map, 0x0d08, &s->con0_before);
	if (ret) return ret;
	ret = regmap_read(map, 0x0d0a, &s->con1_before);
	if (ret) return ret;
	/* Chip idle/on guard; board may impose stricter restrictions. */
	if (!(s->con0_before & 1) || (s->con1_before & 0x800f) ||
	    !allow_latch(s->con0_before, s->con1_before)) return -EBUSY;
	ret = regmap_update_bits(map, 0x0d0a, 0x000f, 0x0001);
	if (ret) goto cleanup;
	ret = regmap_read_poll_timeout(map, 0x0d0a, value, value & 0x8000, 100, 32000);
	if (ret) goto cleanup;
	ret = regmap_read(map, 0x0d12, &low);
	if (ret) goto cleanup;
	ret = regmap_read(map, 0x0d14, &high);
cleanup:
	s->cleanup_error = regmap_update_bits(map, 0x0d0a, 0x000f, 0x0008);
	err = regmap_read_poll_timeout(map, 0x0d0a, value, !(value & 0x8000), 100, 32000);
	if (!s->cleanup_error) s->cleanup_error = err;
	err = regmap_update_bits(map, 0x0d0a, 0x000f, 0x0000);
	if (!s->cleanup_error) s->cleanup_error = err;
	err = regmap_read(map, 0x0d0a, &value);
	if (!err && value != s->con1_before) err = -EIO;
	if (!s->cleanup_error) s->cleanup_error = err;
	err = regmap_read(map, 0x0d08, &value);
	if (!err && value != s->con0_before) err = -EIO;
	if (!s->cleanup_error) s->cleanup_error = err;
	if (ret) return ret;
	if (s->cleanup_error) return s->cleanup_error;
	if (low > 65535 || high > 65535) return -ERANGE;
	s->low = low; s->high = high;
	return 0;
}
#endif


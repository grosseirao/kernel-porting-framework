/* SPDX-License-Identifier: GPL-2.0-only */
/* Copyright (c) 2014 MediaTek Inc.
 * Adapted from LG i2c-mtk.c:mtk_i2c_calculate_speed (LMX430HM kernel 4.9).
 * Pure IP-specific encoding only; caller owns clocks, MMIO and board policy.
 */
#ifndef MT6765_I2C_TIMING_H
#define MT6765_I2C_TIMING_H

#include <linux/errno.h>

static inline int mt6765_i2c_calculate_speed(unsigned int source_hz,
		unsigned int target_hz, unsigned int *step, unsigned int *sample)
{
	unsigned int khz = target_hz / 1000, hclk = source_hz / 1000;
	unsigned int sample_count, step_count, product, minimum, best;
	unsigned int selected_sample = 8, selected_step;
	unsigned int max_step = target_hz > 400000 ? 8 : 64;

	/* The donor assumes nonzero kHz and can divide by zero otherwise. */
	if (!step || !sample || !khz || hclk < 2 || target_hz > 3400000)
		return -EINVAL;
	selected_step = max_step;
	minimum = ((hclk >> 1) + khz - 1) / khz;
	best = 8 * max_step;
	for (sample_count = 1; sample_count <= 8; sample_count++) {
		step_count = (minimum + sample_count - 1) / sample_count;
		product = step_count * sample_count;
		if (step_count > max_step)
			continue;
		if (product < best) {
			best = product;
			selected_sample = sample_count;
			selected_step = step_count;
			if (best == minimum)
				break;
		}
	}
	if (hclk / (2 * selected_sample * selected_step) > khz)
		return -ERANGE;
	/* MT6765 cnt_constraint: step is NOT decremented when sample==1. */
	*sample = selected_sample - 1;
	*step = selected_step - (selected_sample != 1);
	return 0;
}

#endif

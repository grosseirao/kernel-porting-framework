/* SPDX-License-Identifier: GPL-2.0-only */
#ifndef _MT6765_EARLY_CLOCK_H
#define _MT6765_EARLY_CLOCK_H
#include <linux/init.h>
struct device_node;
/* Experimental caller must authorize the board/state/recovery before calling.
 * Native CCF owns the resulting critical clock forever, including late errors.
 */
int __init mt6765_prepare_armpll_early(struct device_node *node);
#endif

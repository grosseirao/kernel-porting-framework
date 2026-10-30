/* SPDX-License-Identifier: GPL-2.0-only */
#ifndef __SOC_MEDIATEK_MT6765_PM_DOMAINS_H
#define __SOC_MEDIATEK_MT6765_PM_DOMAINS_H

#include "mtk-pm-domains.h"
#include <dt-bindings/power/mt6765-power.h>

/* LG clk-mt6765-pg.c: spm_mtcmos_ctrl_conn_bus_prot/conn_pwr.
 * Only CONN is described here. Other MT6765 domain IDs remain unsupported.
 * Generic SPM_CONN_PWR_CON/SPM_PWR_STATUS offsets are NOT valid on this SoC.
 */
static const u8 mt6765_conn_release_order[SPM_MAX_BUS_PROT_DATA] = {
	2, 0, 1, 3, 4, 5, 6,
};

static const struct scpsys_domain_data scpsys_domain_data_mt6765[] = {
	[MT6765_POWER_DOMAIN_CONN] = {
		.name = "conn",
		.sta_mask = BIT(1),
		.ctl_offs = 0x32c,
		.pwr_sta_offs = 0x180,
		.pwr_sta2nd_offs = 0x184,
		.caps = MTK_SCPD_KEEP_DEFAULT_OFF,
		.bp_cfg = {
			BUS_PROT_WR_IGN(INFRA, BIT(13), 0x2a0, 0x2a4, 0x228),
			_BUS_PROT(INFRA, BIT(18), 0x2a8, 0x2ac, BIT(18), 0x258,
				  BUS_PROT_IGNORE_CLR_ACK | BUS_PROT_SET_ACK_LOW),
			BUS_PROT_WR_IGN(INFRA, BIT(14) | BIT(16), 0x2a0, 0x2a4, 0x228),
		},
		.bp_clr_order = mt6765_conn_release_order,
		.pwr_off_primary_first = true,
		.strict_power_lifecycle = true,
	},
};

static enum scpsys_bus_prot_block mt6765_bus_prot_blocks[] = {
	BUS_PROT_BLOCK_INFRA,
};

static const struct scpsys_soc_data mt6765_scpsys_data = {
	.domains_data = scpsys_domain_data_mt6765,
	.num_domains = ARRAY_SIZE(scpsys_domain_data_mt6765),
	.bus_prot_blocks = mt6765_bus_prot_blocks,
	.num_bus_prot_blocks = ARRAY_SIZE(mt6765_bus_prot_blocks),
	.require_access_controllers = true,
};

#endif /* __SOC_MEDIATEK_MT6765_PM_DOMAINS_H */

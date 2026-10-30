# SPDX-License-Identifier: GPL-2.0-only
TEST_PROGS := portkit.sh
ifneq ($(wildcard ../lib.mk),)
include ../lib.mk
else
.PHONY: all run_tests
all:
	@echo 'Standalone host interface selftest; use make run_tests'
run_tests:
	@sh ./portkit.sh
endif

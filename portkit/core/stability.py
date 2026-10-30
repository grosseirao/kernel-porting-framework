# SPDX-License-Identifier: MIT
"""Offline interpretation of bounded stability reports, without device access.

Policy values describe a capture's expected protocol, not safe operating limits
or permission to run a test. Board-specific execution stays outside this module.
"""
import re


def stability_findings(text, *, prefix, cpus, total_seconds,
                       watchdog_min, watchdog_max):
    """Decode an existing report using an explicit, validated board policy.

    Only recognized events are exported. Unknown lines are not evidence of pass;
    raw capture contents (which may contain private data) are never returned.
    """
    if not isinstance(prefix, str) or not re.fullmatch(r'[A-Z][A-Z0-9_-]{0,63}', prefix):
        raise ValueError('Invalid stability marker prefix')
    if (not isinstance(cpus, (list, tuple)) or not cpus or
            any(type(cpu) is not int or not 0 <= cpu < 64 for cpu in cpus) or
            len(set(cpus)) != len(cpus)):
        raise ValueError('Expected distinct CPU identifiers in range 0..63')
    if (any(type(value) is not int or not 1 <= value <= 86400
            for value in (total_seconds, watchdog_min, watchdog_max)) or
            watchdog_min > watchdog_max):
        raise ValueError('Invalid expected duration or watchdog report range')
    pattern = re.compile(re.escape(prefix) + r': ([a-z_]+) value=(-?\d+)\s*$')
    events = []
    allowed = {'watchdog_timeout', 'start_seconds', 'phase', 'alive_seconds',
               'worker_pass_cpu', 'worker_fail_cpu', 'worker_fail_status',
               'pass_seconds', 'failed_seconds', 'stop_feeding_wait_reset'}
    for number, line in enumerate(text.splitlines(), 1):
        match = pattern.search(line)
        if match and match[1] in allowed:
            if len(events) >= 256:
                raise ValueError('Too many stability events')
            events.append(dict(kind=match[1], value=int(match[2]), line=number))
    values = lambda kind: [e['value'] for e in events if e['kind'] == kind]
    timeouts = values('watchdog_timeout')
    passed = (values('start_seconds') == [total_seconds] and values('phase') == [0, 1, 2]
              and sorted(values('worker_pass_cpu')) == sorted(cpus)
              and values('pass_seconds') == [total_seconds] and not values('failed_seconds')
              and not values('worker_fail_cpu') and len(timeouts) == 1
              and watchdog_min <= timeouts[0] <= watchdog_max
              and values('stop_feeding_wait_reset') == timeouts
              and events[-2]['kind'] == 'pass_seconds'
              and events[-1]['kind'] == 'stop_feeding_wait_reset')
    return {'events': events, 'complete_bounded_test_reported_pass': passed,
            'not_sustained_or_thermal_qualification': True,
            'physical_watchdog_reset_not_proven_by_finish_marker': True}

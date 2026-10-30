# SPDX-License-Identifier: MIT
"""Filtered SMP capture events; no hardware diagnostics or boot correlation."""
import re

from .cpulist import parse_cpu_list


def smp_findings(text, *, prefix, online_prefix, max_cpus, arm_cpu_up_timeout_inference):
    """Interpret explicit log markers, never infer topology or hardware state."""
    for value in (prefix, online_prefix):
        if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}', value):
            raise ValueError('Explicit literal SMP log prefixes required')
    if type(max_cpus) is not int or not 1 <= max_cpus <= 4096:
        raise ValueError('Invalid supported CPU count')
    if type(arm_cpu_up_timeout_inference) is not bool:
        raise ValueError('Explicit ARM timeout inference policy required')
    cpus = {}
    events, releases, online = [], [], []
    for number, line in enumerate(text.splitlines(), 1):
        release = re.search(r'Linux version (\S+)', line)
        if release:
            releases.append(release[1])  # Never export compiler/user/hostname text.
        marker = re.search(re.escape(online_prefix) + r': cpus online ([0-9,-]+)\s*$', line)
        if marker:
            online.append({'line': number, 'cpus': parse_cpu_list(marker[1], max_cpus=max_cpus)})
        event = None
        match = re.search(re.escape(prefix) + r': request cpu=(\d+) mpidr=0x([0-9a-fA-F]+) entry=0x([0-9a-fA-F]+)', line)
        if match:
            event = {'cpu': int(match[1]), 'kind': 'cpu_on_request',
                     'mpidr': int(match[2], 16), 'linux_entry': int(match[3], 16)}
        match = re.search(re.escape(prefix) + r': return cpu=(\d+) result=(-?\d+)', line)
        if match:
            event = {'cpu': int(match[1]), 'kind': 'cpu_on_linux_api_return', 'result': int(match[2])}
        match = re.search(re.escape(prefix) + r': entered_c cpu=(\d+)', line)
        if match:
            event = {'cpu': int(match[1]), 'kind': 'entered_secondary_c_after_cpu_init'}
        match = re.search(r'CPU(\d+): failed to come online', line)
        if match:
            event = {'cpu': int(match[1]), 'kind': 'online_timeout'}
        match = re.search(r'CPU(\d+): failed to boot: (-?\d+)', line)
        if match:
            event = {'cpu': int(match[1]), 'kind': 'boot_error', 'result': int(match[2])}
        match = re.search(r'GICv3: CPU(\d+): found redistributor .*region \d+:0x([0-9a-fA-F]+)', line)
        if match:
            event = {'cpu': int(match[1]), 'kind': 'gic_redistributor_found', 'address': int(match[2], 16)}
        if event:
            if not 0 <= event['cpu'] < max_cpus or len(events) >= 4096:
                raise ValueError('Too many events or CPU outside supported range')
            event['line'] = number
            events.append(event)
            cpus.setdefault(str(event['cpu']), []).append(event)
    inferences = []
    for cpu, records in cpus.items():
        if (arm_cpu_up_timeout_inference and any(r['kind'] == 'online_timeout' for r in records)
                and not any(r['kind'] == 'cpu_on_linux_api_return' for r in records)):
            inferences.append({'cpu': int(cpu), 'kind': 'cpu_on_success_inferred_not_directly_measured',
                               'basis': 'ARM __cpu_up prints online timeout only after smp_boot_secondary returned zero',
                               'does_not_prove': 'firmware power-on completion or secondary assembly/C entry'})
    return {'kernel_releases': releases, 'online_markers': online, 'events': events,
            'inferences': inferences, 'multiple_boots_possible': len(releases) > 1,
            'repeated_cpu_on_requests': any(sum(r['kind'] == 'cpu_on_request' for r in records) > 1
                                            for records in cpus.values())}

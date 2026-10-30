# Kernel Porting Framework (KPF)

Reusable offline host tooling for kernel porting. The Python package is
`portkit`; device ports have independent Git repositories under `ports/`,
ignored by KPF and not submodules. See [port setup](ports/README.md).

## Ownership

- `portkit/`: reusable library, explicit workspace APIs and packaged CLIs.
- `components/` and `kernel/components/`: shared definitions, provenance and
  chip/IP sources, preserving per-file licenses and upstream framework boundaries.
- `tools/tests/toolkit/`: independent framework regression tests.
- `ports/<device>/`: independent device workspace, with its own source history,
  profile, integration patches, workflows, tests, evidence and private configuration.

The initial LG K40S consumer is in `ports/lg-k40s/` locally. Cloning KPF does
not fetch it. No repository URL is assumed or remote configured. Its reviewed
local wheel is pinned by SHA-256; it must also work outside this directory.
Useful mechanisms developed in ports belong back in KPF, not copied libraries.

## Offline validation

With the already prepared Python environment and optional host dependencies:

```sh
python tools/test-offline.py
```

This fixed suite runs only independent toolkit tests, with the existing
transport guard. Device integration tests are run separately in their explicit
consumer workspace. Test catalog classification is not proof of execution.

`pyproject.toml` builds the library and ten generic analysis/validation commands,
not device data or laboratory workflows. Packaged commands require an explicit
absolute `--workspace`; board-driven commands also require `--board`. No implicit
parent-checkout lookup or device discovery is performed.

## Configuration and safety

Runtime/SSH configuration belongs to the consumer's ignored `.env`, using the
existing strict literal loader. External roots and toolchains are explicit
inputs, not personal-path defaults. Keys, images and private evidence are not
framework sources. Do not execute dotenv as shell or relax recovery protections.

The first functional target remains Linux 6.18 with internal Wi-Fi/Bluetooth on
LG K40S; offline preparation does not prove that delivery and does not authorize
phone access, charging, flashing or permanent installation.

Migration status and preserved legacy originals are described in
[current state](docs/current-state.md). Source code for old device workflows
remains locally preserved during recovery handover, but is no longer KPF's
versioned interface. The port owns its canonical sources. No files were erased,
no commits or remotes were created, and private configuration was not copied.


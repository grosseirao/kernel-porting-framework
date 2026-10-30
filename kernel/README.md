# Shared kernel inputs

KPF keeps chip/IP sources under `kernel/components/` and reusable test sources
under `kernel/tests/`. These are not a parallel driver framework: prefer the
appropriate upstream Linux subsystem and preserve each file's origin/license.

Board integration, profiles, diagnostics, electrical policy and KUnit assembly
belong to the independent device port. The initial consumer is `ports/lg-k40s/`
locally; it is not fetched by cloning KPF. Existing local legacy files are
preserved during recovery handover but are not KPF's versioned source interface.

Consumers select shared inputs using an explicit absolute KPF root, never a
parent-directory search. Their source manifests keep logical names and hashes;
shared resolution does not authorize hardware probing, deployment or flashing.
See [port ownership](../ports/README.md).

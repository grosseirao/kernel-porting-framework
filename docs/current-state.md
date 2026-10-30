# Current KPF state

Updated 2026-10-29. KPF keeps its name and repository. Device work has independent
Git history under `ports/<device>/`, ignored by the parent, without submodules.
See [ownership and setup](../ports/README.md). The LG K40S workspace exists locally;
cloning the framework does not obtain it.

## Framework boundary

The framework owns `portkit/`, shared `components/`, chip/IP sources in
`kernel/components/`, reusable kernel tests, independent Python tests and generic
offline commands. Device profiles, modules, integration patches, initramfs,
workflows, integration tests and evidence belong to the consumer.

The distribution is `kpf-portkit` 0.1.2. The K40S consumer pins a reviewed local
wheel by SHA-256 and has no copied `portkit`, catalog or shared chip sources.
Catalog/headers use an explicit absolute KPF inputs root. Source fixtures use
the existing named test-source map with a `kpf` root; runtime/SSH still use the
strict literal dotenv loader. No implicit lookup of the parent checkout exists.

## Verification so far

- All 35 kernel profiles and fingerprints matched with separate shared inputs.
- Complete device composition matched without shared copies in the consumer.
- Battery staging bytes/order, make argv/kwargs and report bytes matched the
  preserved previous builder; compiler calls in this fixture were intercepted.
- KUnit fixture staging/prepared manifest matched with separated roots;
  changed shared sources, invalid roots and unsafe generated configs were refused.
- The affected suite ran 88 cases: 85 passed; two private early/memory evidence
  cases and one private LG donor comparison were skipped, without weakening gates.
- The same result held for an external temporary consumer containing 1275
  byte-verified source files, with spaces in its path, cwd outside the workspace
  and the isolated wheel. No kernel/module build or physical operation occurred.

Catalogs and test counts are supporting evidence, not phone validation. The port
retains all its previous test IDs; independent toolkit tests live only in KPF.
The framework's fixed runner now selects those independent tests only, rather
than silently discovering the local legacy integration sources.

## Source handover in progress

1209 device-source candidates all had replacements in the port. Twelve differences
were the reviewed requirement/documentation and test-source resolution changes.
The current original bytes of all candidates plus README and two test manifests
were preserved under ignored `work/migration-preserved-device/` before changing
Git ownership. No original source or recovery asset was deleted.

The consumer's 17 duplicate shared files were separately hash-verified and moved
to its ignored `work/migration-preserved-shared/`; their canonical originals
remain in KPF. The initial external device copy is also preserved unchanged.

Legacy files/configuration/images still on disk are not a fallback source for
new consumer execution. Do not run a relocated recovery workflow against guessed
paths or auto-copy keys/backups/configuration. Recovery handover requires the
same explicit inputs, hashes, operation ordering and existing authorizations.

The detailed device work journal, including historical functional evidence,
is preserved in the independent consumer's `docs/current-state.md`. It is not
part of a clone of KPF. No new radio functionality has been claimed here.

## Git handover verification

The parent index no longer contains the selected device sources. All existing
legacy originals remain on disk and in the ignored preservation area; this is
an index handover, not deletion. Device baseline evidence and board-specific DT
fixtures stay with the port, including their original bytes and hashes.

The independent consumer index contains 1276 source files. Its source-only
checker passed, including exclusion probes for keys/private roots/binaries.
The parent fixed suite passed 35 independent tests both in place and in the
final 107-file export of the Git index, with no caches or legacy device files.
The real consumer composition was identical using that clean export as its
explicit shared root. A preliminary snapshot exposed 12 accidentally re-included
Python cache files; the ignore-rule precedence was corrected and those caches
were removed from the index, not from disk. The final source-only checker passed
all 107 parent entries; no exclusion or validator was relaxed.
No test was removed from the device suite to make the framework suite pass.
Its full 1090-case catalog is kept separately; the framework catalog lists 35.

The initial import's whitespace warnings concern preserved historical files
and unified patches; their pinned bytes were not normalized or repinned. This
does not imply a clean whitespace audit of the entire historical import.

## Acceptance of source repository separation

Final audit confirmed independent Git roots, no gitlinks/submodules or consumer
remotes, only ports/README.md tracked under ports by KPF, and no copied library,
catalog, shared headers, private configuration or artifacts in the consumer index.
Its 1276 indexed sources include device profiles, kernel integration, patches,
initramfs, workflows, recovery sources, tests, manifests and documentation.
The exact 0.1.2 wheel SHA-256 in its requirement matches the local artifact and
every Python source in the artifact matches current KPF code.

1238 archived originals still matched the legacy files on disk byte for byte
in the final audit; the initial external device copy remains preserved. The
legacy files are ignored local preservation, not a fallback interface for KPF
or a reason to copy private inputs into a new workspace automatically.

Source separation is accepted offline. Changes are staged in the respective
repositories but not committed. No Git identity, remote or publication was
configured. Recovery assets/configuration were not moved; no device operation
or new functional result is claimed. The independent port continues the Linux
6.18 Wi-Fi/Bluetooth work with existing safety requirements and authorizations.

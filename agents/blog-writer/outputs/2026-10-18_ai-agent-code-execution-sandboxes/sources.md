# Sources — AI Agent Code Execution Sandboxes: E2B vs Modal vs Daytona

## Primary (verified live via WebFetch, 2026-10-18)

1. **E2B official docs** — https://docs.e2b.dev/
   - `pip install e2b`, `npm i e2b`
   - `Sandbox.create()` reads `E2B_API_KEY` from env
   - `sandbox.commands.run(...)` executes shell commands
   - Sandbox described as "a Linux VM created on demand that can be paused and resumed"
   - Templates define the starting environment; paused sandboxes keep filesystem + memory

2. **E2B lifecycle docs** — https://docs.e2b.dev/sandbox/lifecycle
   - Max runtime: 1 hour on Hobby plan, 24 hours on Pro plan
   - Custom timeout: `Sandbox.create(timeout=60)` (seconds)
   - `get_info()` shows `lifecycle: { onTimeout: 'kill', autoResume: false }` — timeout behavior is configurable
   - No default-timeout number stated on this page (max runtimes given instead)

3. **E2B infra repo (official, open-source backend)** — https://github.com/e2b-dev/infra
   - Direct quote: "One Firecracker microVM per sandbox, in its own cgroup and network namespace"
   - Per-sandbox nftables egress firewall with domain allow/deny lists
   - Components: control-plane API, per-node orchestrator driving Firecracker, in-VM agent (`envd`), edge router, template builder
   - Self-hosted option called "Embed" for single-machine deployments

4. **Modal official docs — Sandbox guide** — https://modal.com/docs/guide/sandbox
   - Two runtimes selectable via `runtime=` param: `"gvisor"` (default choice made by Modal if unset) and `"vm"` (full Linux kernel, needed for nested Docker / FUSE)
   - Nested virtualization only on Team/Enterprise plans
   - Default sandbox lifetime: 5 minutes; `timeout=` extends up to 24 hours; beyond that, docs recommend a Filesystem Snapshot + restore
   - `idle_timeout=` kills an idle sandbox; "idle" excludes running commands, open stdin, or an open Tunnel TCP connection
   - Creation: `modal.Sandbox.create(app=app, image=..., runtime="gvisor", timeout=600)`; needs `modal.App.lookup(name, create_if_missing=True)` outside a Modal container
   - Commands: `sb.exec("python", "-c", "...", timeout=3)`, read via `.stdout.read()`
   - GPU Sandboxes supported only on the gVisor runtime, not the VM runtime
   - Async variants use `.aio` suffix

5. **Daytona GitHub repo (official)** — https://github.com/daytonaio/daytona
   - Repo is archived / read-only on GitHub as of 2026
   - README states core development moved to a private codebase; repo gets no further updates, fixes, or releases
   - Code remains public, free to use/fork under its existing license, "without support or warranty"
   - Self-description: "secure and elastic infrastructure runtime for AI-generated code execution and agent workflows"

6. **Fly.io — Firecracker vs gVisor** — https://fly.io/learn/firecracker-vs-gvisor.md
   - Firecracker: hardware-virtualized microVM, each sandbox gets its own guest kernel (KVM-based)
   - gVisor: userspace kernel written in Go that intercepts syscalls from a normal container; no separate guest kernel
   - Framed as two different isolation strategies defending against different failure modes at different performance cost

## Secondary / contextual (not used for unverifiable numbers)
- Various 2026 vendor-comparison blogs (dev.to, superagent.sh, helix.ml, morphllm.com) were used only to find *that* the Daytona open-source story and the Firecracker/gVisor split were worth checking — every specific claim actually used in the article was re-verified against the primary sources above before writing.
- Latency/cold-start numbers reported by third parties (e.g. "150ms E2B", "500ms–1s Modal") were **not used** in the article — they varied between sources and the official docs don't publish a single comparable number, so repeating them would risk an unverifiable statistic.

## Not used / explicitly avoided
- No specific Daytona isolation-technology claim is made in the article (its own current docs/README don't give the implementation detail the way E2B's and Modal's do) — the article only cites what's confirmed: archived repo, private core, "runtime" positioning.

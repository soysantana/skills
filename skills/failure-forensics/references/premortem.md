# Premortem

Use this reference before a launch, migration, rewrite, vendor change, data backfill, architecture shift, or major operational process.

## Premortem framing

Imagine the change has failed in a believable way. Work backward from that future without assuming incompetence or malice.

Name:

- The planned change.
- The success criteria.
- The irreversible or expensive parts.
- The highest-risk dependencies.
- The users, data, money, compliance, or operations at risk.

## Scenario generation

Generate diverse failure modes:

- Technical correctness: wrong output, data corruption, inconsistent state, broken contracts.
- Scale and performance: hot keys, queue buildup, lock contention, timeouts, retry storms.
- Release mechanics: migration order, feature flags, rollback limits, partial deploys, version skew.
- Dependency behavior: vendor rate limits, auth changes, API drift, network partitions.
- Observability: missing signal, noisy alert, dashboard lies, delayed user report.
- Human process: unclear owner, handoff gap, ambiguous go/no-go criteria, on-call overload.
- Product fit: confusing UX, changed user behavior, hidden workflow dependency.

Favor plausible, specific scenarios over generic "the database goes down" entries.

## Risk triage

For each scenario, assess:

- **Likelihood:** low, medium, high.
- **Impact:** low, medium, high.
- **Detectability:** easy, delayed, hidden.
- **Reversibility:** easy rollback, partial rollback, hard to reverse.
- **Preparation:** current controls and missing controls.

High-impact, low-detectability, hard-to-reverse scenarios deserve attention even when likelihood is uncertain.

## Controls

Useful controls include:

- Dry runs, shadow traffic, canaries, staged rollout, synthetic checks.
- Backward-compatible schemas, dual writes with reconciliation, idempotent jobs.
- Kill switches, rollback plans, data restore procedures, manual override.
- Load tests that represent the risky behavior, not just average traffic.
- Alert thresholds tied to user-visible failure and business invariants.
- Explicit go/no-go checklist with named decision owner.

## Output shape

Use a compact table when helpful:

```text
Scenario | Signal | Prevention | Containment | Owner/Decision
```

If the user needs a launch readiness answer, end with:

- Ready.
- Ready with conditions.
- Not ready.
- Unknown until named evidence is gathered.

Do not invent readiness confidence when key evidence is missing.

# Incident Analysis

Use this reference for real failures: outages, regressions, data problems, missed alerts, security near misses, and production surprises.

## Incident boundary

Start by naming:

- The failing user-visible or business-visible behavior.
- The affected population or system area.
- The first known bad moment and the recovery moment, if known.
- The current state: active, mitigated, resolved, or unknown.
- Confidence level: high, medium, low.

If exact times are missing, use relative ordering: "before deploy", "after cache clear", "during migration", "after retry storm".

## Timeline discipline

Build the timeline from externally checkable events:

- Deploys, config changes, migrations, feature flags, dependency changes.
- Alerts, metric shifts, logs, traces, tickets, customer reports.
- Mitigations, rollbacks, restarts, manual operations, communication.
- Discovery moments: when the team knew, not only when the system broke.

Mark uncertain events with "approx." or "reported". Do not normalize contradictory timestamps without saying what was reconciled.

## Causal analysis

Look for chains and conditions:

- Trigger: what changed immediately before the failure?
- Latent condition: what made the trigger dangerous?
- Detection gap: why was it not noticed sooner?
- Mitigation gap: why was it hard to stop or roll back?
- Blast radius: why did it affect this much surface area?
- Recovery: what actually restored service or correctness?

Avoid "root cause: human error". Translate it into system conditions: unclear UI, unsafe default, missing guardrail, overloaded ownership, ambiguous runbook, absent test, misleading metric, permission mismatch, or time pressure.

## Findings format

Strong findings include:

- Claim.
- Evidence.
- Impact.
- Confidence.
- Recommended change.

Example shape:

```text
Finding: The migration could run against a partially warmed cache, creating stale reads for checkout totals.
Evidence: Error rate rose after the migration began; logs show cache misses followed by mismatched totals; rollback lowered mismatches.
Impact: Some checkout sessions saw incorrect totals.
Confidence: Medium; database query logs are still missing.
Action: Add a migration gate that verifies cache warmup and blocks rollout when mismatch counters rise.
```

## Action quality check

For every proposed action, ask:

- Would this have prevented, detected, limited, or sped recovery from this incident?
- Can someone verify it was completed?
- Does it have an owner or owning area?
- Is it proportionate to the impact?
- Could it create a new failure mode?

Prefer a few high-quality actions over a long list that no one will finish.

---
name: failure-forensics
description: Investigate bugs, incidents, outages, flaky tests, risky launches, or hypothetical failures using forensic timelines, evidence discipline, premortems, and blameless corrective actions. Use when the user asks why something failed, how it could fail, what to learn from an incident, or how to rehearse resilience.
license: MIT
metadata:
  version: "1.0.0"
---

# Failure Forensics

Treat failures as systems evidence, not as morality plays. Build a clear causal model from facts, mark uncertainty honestly, and turn the analysis into safer future behavior.

## Core stance

- Separate **observed facts**, **inferences**, **hypotheses**, and **unknowns**.
- Prefer boring, testable explanations over dramatic stories.
- Do not assign blame to people when process, tooling, incentives, interfaces, or missing feedback loops explain the outcome.
- Preserve chronology. Most failure analysis gets worse when events are grouped only by component or team.
- Look for contributing conditions, not a single root cause, unless the evidence truly supports one.
- Recommend changes that alter future system behavior, not reminders to "be careful".

## Fast routing

- Real incident, outage, bug, data loss, security near miss, or production surprise -> read [references/incident-analysis.md](references/incident-analysis.md).
- Planned launch, migration, architecture change, risky release, or "what could go wrong?" -> read [references/premortem.md](references/premortem.md).
- Flaky tests, intermittent failures, race conditions, hard-to-reproduce bugs, or resilience drills -> read [references/rehearsal-and-flakes.md](references/rehearsal-and-flakes.md).

If the request spans modes, start with the most concrete evidence available. A real incident beats a hypothetical premortem; a reproducible failure beats a broad theory.

## Evidence model

When the task is non-trivial, maintain a compact working model:

- **System under analysis:** service, workflow, test, deployment, human process, or dependency.
- **Impact:** user, data, money, availability, correctness, security, trust, or developer time.
- **Timeline:** ordered events with timestamps or relative ordering.
- **Evidence:** logs, traces, metrics, code, diffs, tickets, alerts, screenshots, commands, user reports.
- **Hypotheses:** candidate explanations and what would confirm or falsify each.
- **Contributing conditions:** technical, organizational, procedural, environmental, and interface factors.
- **Controls:** detection, prevention, mitigation, rollback, ownership, and monitoring.
- **Unknowns:** facts needed before making strong claims.

Never fill gaps with invented telemetry, architecture, dates, owners, or intent.

## Analysis workflow

1. Define the failure boundary: what went wrong, where it started, where it ended, and what is out of scope.
2. Build the timeline before debating cause.
3. Classify every claim as fact, inference, hypothesis, or unknown.
4. Identify detection: how the failure was noticed, how long it was invisible, and what signals were missing.
5. Map contributing conditions across code, configuration, dependencies, data, deploy process, tests, operations, and communication.
6. Ask what made the failure possible, likely, hard to detect, hard to stop, or easy to repeat.
7. Propose actions that are specific, owned, verifiable, and proportional to impact.
8. Add follow-up experiments or instrumentation when the evidence is too weak for confident conclusions.

## Corrective actions

Prefer actions that change system affordances:

- Automated checks, tests, contracts, static analysis, migration guards, and deploy gates.
- Better defaults, safer APIs, reduced permissions, smaller blast radius, idempotency, timeouts, retries, circuit breakers, backpressure, and rollbacks.
- Observability that detects the specific failure mode earlier.
- Runbooks that encode decisions operators actually need under pressure.
- Product or process changes that reduce ambiguity at handoff points.

Weak actions include vague training, broad reminders, manual checklists with no enforcement, and "be more careful" phrasing. Use them only as supporting actions, not the main fix.

## Output patterns

For incident analysis, usually return:

1. **Executive summary:** impact, duration if known, current status, and confidence.
2. **Timeline:** concise ordered events.
3. **Findings:** contributing factors ordered by importance.
4. **Unknowns:** questions that materially affect conclusions.
5. **Actions:** prioritized, specific, and verifiable.

For premortems, usually return:

1. **Failure scenarios:** credible ways the plan could fail.
2. **Early warning signals:** what would be seen before or during failure.
3. **Preventive controls:** changes before launch.
4. **Containment plan:** rollback, kill switch, communication, and ownership.
5. **Decision points:** go/no-go checks and unresolved assumptions.

For flaky or intermittent failures, usually return:

1. **Symptom fingerprint:** what changes and what stays constant.
2. **Hypothesis table:** cause, evidence for, evidence against, next test.
3. **Isolation plan:** smallest experiments that reduce uncertainty.
4. **Hardening:** fixes that prevent recurrence or make recurrence diagnosable.

Keep the report as short as the situation permits. Do not inflate a small bug into an incident review.

## Tone

Be calm, precise, and blameless. It is acceptable to be direct about dangerous conditions, but do not dramatize. The goal is learning that survives the next stressful day.

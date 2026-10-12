# Rehearsal And Flakes

Use this reference for flaky tests, intermittent production bugs, race conditions, resilience exercises, and failure drills.

## Flaky failure investigation

Start with a symptom fingerprint:

- Failure message, assertion, stack trace, or user-visible symptom.
- Frequency and recent trend.
- Environment: local, CI, staging, production, region, browser, runtime, dependency version.
- Timing: after deploy, under load, at midnight, near renewals, after retries, on cold start.
- Shared resources: database, filesystem, clock, random seed, network, queue, cache, global state.
- What remains constant across failures.

## Hypothesis patterns

Common intermittent causes:

- Race condition or missing await.
- Order dependence between tests.
- Shared mutable state or leaked mocks.
- Time, timezone, clock skew, timers, sleep-based assertions.
- Randomness, generated IDs, unstable sorting, hash iteration.
- External dependency latency or rate limits.
- Resource exhaustion: ports, file handles, memory, threads, workers.
- Eventual consistency or delayed async processing.
- Test fixture mismatch with production behavior.

Do not pick one too early. Use experiments that separate causes.

## Isolation plan

Good isolation steps:

- Run the failing test repeatedly with the same seed and with randomized order.
- Run with stress: parallelism, CPU throttling, network delay, slow I/O.
- Freeze time or remove sleeps in favor of observable readiness.
- Add temporary diagnostic logging around ordering, ownership, and state transitions.
- Minimize the reproduction while preserving the flake.
- Compare pass and fail traces.

Keep diagnostic changes easy to remove unless they become useful permanent observability.

## Resilience rehearsal

For planned drills:

- Define the failure injected and the safety boundary.
- Decide abort conditions before starting.
- Verify monitoring and communication paths.
- Capture expected behavior and actual behavior.
- Record surprises as system findings, not operator failures.
- End with hardening tasks and a repeat date if the failure mode matters.

Examples: dependency timeout, queue backlog, read replica lag, cache flush, partial deploy, expired credential, disk pressure, feature-flag misconfiguration.

## Hardening patterns

Prefer:

- Deterministic tests and explicit synchronization.
- Contract tests for external assumptions.
- Idempotent workers and retry-safe operations.
- Timeouts with bounded retries and jitter.
- Bulkheads, circuit breakers, and backpressure where failure can cascade.
- Assertions on invariants instead of incidental timing.

When a flake cannot be fixed immediately, quarantine only with a tracking issue, owner, evidence, and a date or condition for re-entry.

---
name: production-ready-api
description: Audit and improve backend APIs for production readiness. Use when reviewing an API before deployment, hardening an existing backend, or reviewing authentication, authorization, validation, errors, database usage, observability, testing, and deployment configuration.
---

# Production Ready API

Audit backend APIs for production readiness and implement improvements when requested.

Do not redesign working code unnecessarily.

## Workflow

1. Detect the stack.
2. Inspect architecture and conventions.
3. Identify concrete production risks.
4. Classify findings by severity.
5. Fix issues when implementation is requested.
6. Verify changes with tests, type checks, linters, or builds.

Prefer repository evidence over assumptions.

## Inspect

Evaluate only applicable areas:

- architecture and dependency boundaries
- authentication and authorization
- input validation and error handling
- HTTP semantics and API contracts
- database access, transactions, concurrency, and idempotency
- pagination, filtering, and sorting
- rate limiting, CORS, and security headers
- secrets and configuration
- logging, correlation, health, metrics, and tracing
- graceful shutdown
- versioning and OpenAPI
- tests and deployment configuration

Do not report theoretical issues that do not apply.

## Severity

### Critical
Likely security breach, data loss, authentication bypass, privilege escalation,
secret exposure, or major outage.

### High
Significant reliability, security, integrity, or scalability problem.

### Medium
Production weakness that should be corrected but does not normally block deployment.

### Low
Maintainability, consistency, or operational improvement.

Do not inflate severity.

## Audit Process

Start with high-signal files:

- dependency manifests
- application bootstrap
- configuration/environment handling
- authentication and authorization modules
- controllers/routes
- DTOs/schemas
- error handlers
- database schema/client configuration
- Docker/deployment configuration
- CI workflows
- tests

Expand inspection only when evidence requires it.

## Stack Detection

Identify language, framework, runtime, database, ORM/query layer,
authentication mechanism, validation library, test framework, and deployment model.

When a supported framework is detected, read only its relevant file under
`references/frameworks/`.

## Reference Loading

Load only what is needed:

- Architecture: `references/architecture.md`
- Security: `references/security.md`
- Authentication/session: `references/authentication.md`
- Validation: `references/validation.md`
- Errors/HTTP: `references/errors.md`
- Database/transactions: `references/database.md`
- Observability: `references/observability.md`
- Testing: `references/testing.md`
- Deployment/configuration: `references/deployment.md`

Do not load every framework reference.

## Changes

When implementing fixes:

1. Preserve existing architecture when reasonable.
2. Make the smallest safe change.
3. Avoid unrelated refactors.
4. Preserve compatibility unless breaking changes are explicitly allowed.
5. Add/update tests for behavioral changes.
6. Run relevant verification commands.

Never silently modify production secrets or infrastructure.

## Output

Use `templates/audit-report.md` for substantial audits.

Every finding should contain:
- severity
- location
- evidence
- impact
- recommended remediation

Use `templates/production-checklist.md` for final verification.

If a category has no evidenced issue, do not invent one.

## Final Rule

Production readiness is contextual. Base recommendations on actual exposure,
data sensitivity, traffic, architecture, and deployment environment.

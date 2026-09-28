---
name: clean-architecture
description: Design, implement, review, or refactor software using Clean Architecture principles associated with Robert C. Martin. Use for architecture boundaries, dependency direction, entities/domain models, application use cases, ports/interfaces, adapters, controllers, presenters, repositories, infrastructure isolation, framework independence, testability, or deciding where code belongs. Applies across languages and frameworks.
license: MIT
metadata:
  version: "1.0.0"
---

# Clean Architecture

Apply Clean Architecture as a decision framework, not as a rigid folder template.

## Core rule

Source-code dependencies must point toward higher-level policy.

Prefer this conceptual direction:

`frameworks/drivers -> adapters -> application/use-cases -> domain/entities`

Inner layers must not depend on outer implementation details.

## Workflow

1. Identify the business capability and invariants before choosing framework structure.
2. Separate business rules from transport, persistence, UI, and vendor concerns.
3. Define use cases around application behavior and explicit input/output boundaries.
4. Put interfaces/ports at the boundary owned by the policy that needs them.
5. Implement external concerns as adapters behind those boundaries.
6. Pass simple domain/application data across boundaries; do not leak framework objects inward.
7. Keep composition and dependency injection at the outer edge.
8. Test inner policies without requiring databases, HTTP servers, UI frameworks, or external services.
9. Refactor only where a boundary provides meaningful isolation; avoid ceremonial layers.

## Decision rules

- Business invariant -> domain.
- Application-specific orchestration -> use case/application layer.
- Translation between external and internal representations -> adapter.
- Database, HTTP framework, filesystem, queue, SDK, UI -> infrastructure/framework edge.
- If an inner module imports an outer technology, invert that dependency through a boundary when the dependency matters architecturally.
- Do not create an interface merely because an implementation exists. Create one when it protects a policy boundary, enables substitution, or isolates volatility.
- Do not force CRUD-only code through excessive abstractions when no useful boundary exists.

## When reviewing code

Report concrete violations before proposing restructuring. For each issue state:

1. current dependency,
2. why the direction or responsibility is problematic,
3. target boundary,
4. smallest useful change.

Distinguish architectural violations from preferences. Do not call a folder name or naming convention a Clean Architecture requirement.

## When generating code

Follow the project's existing language and conventions unless they violate an important boundary. Prefer the smallest architecture that preserves dependency direction. Avoid placeholder abstractions, duplicate DTOs with no boundary purpose, generic repository layers by default, and framework annotations in domain code when they couple domain policy to infrastructure.

For detailed decisions, load only the relevant reference:

- Layer responsibilities and dependency direction: `references/layers.md`
- Boundaries, ports, DTOs, repositories, and dependency inversion: `references/boundaries.md`
- Project/package organization: `references/structure.md`
- Testing strategy: `references/testing.md`
- Review/refactoring checklist and common mistakes: `references/review.md`
- Framework examples and mapping guidance: `references/framework-mapping.md`

## Output expectations

When architecture is requested, show dependencies explicitly using a compact tree or Mermaid diagram when useful. Explain trade-offs. Preserve domain terminology from the user's project. Do not introduce infrastructure into inner layers for convenience.

When reviewing an existing project, inspect its actual structure before recommending a rewrite. Prefer incremental boundary corrections over wholesale restructuring.
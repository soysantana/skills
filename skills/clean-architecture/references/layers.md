# Layer Responsibilities

Use layers conceptually. A project does not need these exact directory names.

## Domain / Entities

Contains enterprise or core business policy: entities, value objects, invariants, domain behavior, and domain-specific rules.

Should remain independent of databases, web frameworks, UI libraries, serialization libraries, queues, and vendor SDKs where practical.

## Application / Use Cases

Contains application-specific policy and orchestration. Coordinates domain behavior and boundary interfaces to accomplish user/system goals.

Typical contents:
- use cases / application services
- input models or commands
- output models where a boundary requires them
- ports needed by application policy

Avoid HTTP request/response objects, ORM models, UI state, and concrete infrastructure clients.

## Interface Adapters

Translate between external representations and application/domain representations.

Examples:
- controllers
- presenters
- repository implementations/mappers
- gateways
- transport DTO mapping

Adapters know both sides of a boundary so inner policy does not need to.

## Frameworks and Drivers

Contains volatile implementation details and delivery mechanisms:
- web frameworks
- database engines and ORM configuration
- UI frameworks
- message brokers
- filesystem
- external SDKs
- application bootstrap/composition

These are replaceable details, not the center of the architecture.

## Dependency direction

Compile-time/source dependencies should point inward toward policy. Runtime control flow may cross boundaries in either direction through interfaces and inversion of control.

# Architecture and C4

Architecture diagrams are maps of responsibilities, boundaries, and dependencies.

## C4 levels

- **System Context:** people and software systems; one system of interest.
- **Container:** deployable/runnable applications and data stores inside the system.
- **Component:** major components inside one container.
- **Code:** implementation-level structures; use selectively.

Do not mix levels without an explicit reason. A database table next to a whole external enterprise system is usually an abstraction mismatch.

## Relationships

For important edges, capture:

`source -> target : purpose [technology/protocol]`

Examples of useful semantics: HTTPS/JSON, AMQP event, SQL, file transfer, OAuth/OIDC. Only state technology that is known or requested.

## Boundaries

Use boundaries to show ownership/trust/deployment distinctions such as organization, system, VPC/network, runtime, or bounded context. Do not add every possible boundary; add boundaries that answer the architecture question.

## Review checks

- Can the viewer identify the system of interest?
- Are external actors/systems truly external?
- Are data stores owned by the correct container/system?
- Are dependencies directional and explain why they exist?
- Are asynchronous channels represented as such when important?
- Are deployment and logical architecture being confused?
- Are security/trust boundaries visible when they are central to the design?

## Large architecture

Prefer a map set:

1. Context.
2. Container.
3. Focused component view for a complex container.
4. One or more sequences for critical scenarios.
5. Deployment view only if runtime topology is part of the question.

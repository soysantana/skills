# Boundaries and Dependency Inversion

## Place interfaces by ownership

Put a boundary interface near the policy that requires the capability when doing so keeps the policy independent of the implementation.

Example:

```text
application/CreateOrder
        |
        v
application/OrderRepository (port)
        ^
        |
infrastructure/PrismaOrderRepository
```

The use case depends on the abstraction; the infrastructure implementation depends on that same inward-facing contract.

## Boundary data

Prefer simple structures that express what the use case needs. Do not pass ORM entities, HTTP request objects, framework contexts, database sessions, or vendor response types into inner policy.

Do not duplicate models mechanically. Separate models when they represent different responsibilities or protect a real boundary.

## Repositories

A repository is useful when persistence must be abstracted from domain/application policy. Model repository operations around application/domain needs rather than mirroring every database operation automatically.

Avoid a universal generic repository if it obscures meaningful queries or forces all aggregates into the same persistence API.

## Controllers

Controllers translate transport input into application input, invoke a use case, and translate results/errors toward the delivery mechanism. Keep business decisions out of controllers.

## Presenters

Use a presenter/output boundary when output transformation is sufficiently complex or when the application must remain independent of presentation concerns. Do not add one solely to satisfy a diagram.

## External services

Wrap payment providers, email services, object storage, AI APIs, queues, and other vendor SDKs behind application-relevant ports when their details would otherwise leak into policy.

# Architecture Review

## High-signal checks

Check whether:
- domain code imports ORM/framework/transport packages;
- use cases accept HTTP/framework-specific objects;
- controllers contain business rules;
- persistence models are treated as domain objects without deliberate justification;
- concrete gateways are instantiated inside use cases;
- external SDK types leak across application boundaries;
- framework decorators/annotations dictate domain behavior;
- dependency injection configuration exists inside policy modules;
- tests require infrastructure to verify basic business rules.

## Common overengineering

Flag cautiously:
- interfaces with no boundary or substitution purpose;
- generic repositories that erase domain language;
- duplicate request/entity/DTO models that contain identical semantics with no isolation benefit;
- presenters for trivial pass-through responses;
- use cases that merely forward CRUD calls;
- deep folder hierarchies containing one trivial class each.

## Refactoring order

Prefer:
1. identify policy that must be protected;
2. isolate framework/vendor types;
3. introduce the narrow boundary;
4. move translation outward;
5. move composition outward;
6. add tests around the protected policy;
7. restructure folders only when it improves comprehension.

## Review severity

Use descriptive severity only when useful:
- Boundary violation: inward policy directly depends on volatile outer detail.
- Responsibility leak: business/application decisions live in an adapter or framework edge.
- Coupling risk: technically valid but makes replacement/testing unnecessarily expensive.
- Ceremony: abstraction adds indirection without protecting a meaningful boundary.

# Spring Boot Production Review

Inspect security configuration, controllers, validation, service boundaries,
transaction annotations, exception advice, persistence configuration, Actuator,
and externalized configuration.

Check:
- Bean Validation at request boundaries
- Spring Security authorization rules
- method/resource-level authorization where required
- `@Transactional` boundaries and propagation assumptions
- global exception mapping
- datasource pool configuration
- Actuator endpoint exposure
- readiness/liveness configuration
- graceful shutdown
- secrets outside source control

Review lazy-loading/N+1 behavior rather than assuming repository abstractions
eliminate query problems.

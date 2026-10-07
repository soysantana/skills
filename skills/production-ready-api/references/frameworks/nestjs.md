# NestJS Production Review

Inspect `main.ts`, modules, controllers, providers, guards, interceptors, pipes,
exception filters, configuration, and ORM integration.

Check applicable global configuration:
- ValidationPipe/runtime validation
- CORS
- security headers
- API prefix/versioning
- shutdown hooks
- exception handling

Prefer DTO-based runtime validation at transport boundaries. TypeScript types
alone do not validate requests.

Use guards/policies or equivalent centralized mechanisms for authorization.
Frontend route visibility is not authorization.

Validate environment configuration during startup and avoid scattered
`process.env` access when a configuration abstraction already exists.

Do not leak raw ORM errors. Review provider scopes before introducing
request-scoped dependencies because they can affect performance.

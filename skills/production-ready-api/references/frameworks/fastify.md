# Fastify Production Review

Inspect server creation, plugins, hooks, schemas, error handlers, logging,
encapsulation boundaries, and shutdown.

Prefer Fastify route schemas for runtime validation/serialization where the
project uses them. Review plugin encapsulation before moving shared state.

Check:
- schema validation and response serialization
- authentication/authorization hooks
- custom error handler
- request IDs/logging
- CORS and security plugins
- body limits
- rate limiting where needed
- graceful `close()` behavior

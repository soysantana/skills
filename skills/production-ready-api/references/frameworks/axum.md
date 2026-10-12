# Axum Production Review

Inspect router construction, extractors, middleware/layers, application state,
authentication/authorization, error types, database pools, tracing, and server
shutdown.

Check:
- typed/runtime extraction and validation
- authorization at protected resources
- shared state thread safety
- bounded request/body handling
- Tower middleware ordering
- timeout behavior
- tracing/correlation
- DB pool sizing
- error-to-response mapping
- graceful shutdown

Avoid holding blocking work on async executor threads; use appropriate blocking
facilities for CPU/blocking operations.

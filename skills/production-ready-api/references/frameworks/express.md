# Express Production Review

Inspect app bootstrap, routers, middleware ordering, authentication,
authorization, error middleware, proxy settings, and shutdown behavior.

Check:
- centralized error middleware
- runtime request validation
- async error propagation
- explicit CORS policy
- security headers where appropriate
- body/request size limits
- trusted proxy configuration
- rate limits for abuse-sensitive routes
- graceful server shutdown

Middleware order is behavior: authentication, parsers, validation, routes,
404 handling, and error handling must be placed intentionally.

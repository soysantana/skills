# Observability

## Logging
Prefer structured logs with useful context such as timestamp, level, service,
environment, request/correlation ID, route, method, status, and duration.

Never log passwords, credentials, access/refresh tokens, or sensitive bodies.

## Correlation
Generate or propagate a request/correlation ID. Include it in errors/logs when
useful for support.

## Health
Liveness answers whether the process is alive. Readiness answers whether the
instance can safely receive traffic. Only include dependency checks that make
operational sense.

## Metrics
Useful signals include request count, error rate, latency distributions,
active requests, queue depth, and DB pool saturation.

## Tracing
Use distributed tracing when cross-service diagnosis justifies it. Preserve
trace context across supported boundaries.

## Shutdown
Handle termination signals, stop accepting new work, allow bounded in-flight
work to finish, and close resources cleanly.

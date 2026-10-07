# Production Checklist

Use:
- `[x]` verified
- `[ ]` missing or requires action
- `[-]` not applicable
- `[?]` not verified with available evidence

## Security
- [?] Authentication controls verified
- [?] Authorization/resource ownership verified
- [?] Runtime input validation verified
- [?] Secrets excluded from source/logs
- [?] CORS policy appropriate
- [?] Abuse-sensitive endpoints protected

## API Contract
- [?] HTTP methods/status semantics consistent
- [?] Error shape consistent
- [?] Collection endpoints bounded
- [?] Retry-sensitive writes handle idempotency where needed

## Database
- [?] Integrity constraints appropriate
- [?] Transaction boundaries safe
- [?] Concurrency risks reviewed
- [?] Important query paths/indexes reviewed
- [?] Connection pool/lifecycle reviewed
- [?] Migration safety reviewed

## Operations
- [?] Structured diagnostics available
- [?] Correlation/request IDs available where useful
- [?] Health/readiness behavior defined
- [?] Graceful shutdown verified
- [?] Required configuration validated at startup

## Verification
- [?] Tests pass
- [?] Type checking/build passes
- [?] Lint/static checks pass
- [?] Deployment configuration reviewed

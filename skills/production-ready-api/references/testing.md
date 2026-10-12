# Production API Testing

Prioritize tests around risk and contracts.

## Unit Tests
Useful for business rules, validation helpers, policy decisions, and isolated
application logic.

## Integration Tests
Verify database behavior, transactions, repositories, authentication,
authorization, and framework wiring where these are production-critical.

## API/Contract Tests
Cover:
- success paths
- invalid input
- unauthenticated access
- unauthorized access
- missing resources
- conflicts
- pagination boundaries
- idempotency/retry behavior when applicable

## Regression Tests
When fixing a production-readiness issue, add a test that fails before the fix
when practical.

## Verification
Use the project's existing test/lint/typecheck/build commands. Do not introduce
a new test stack merely for an audit unless requested.

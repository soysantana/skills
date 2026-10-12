# Database Production Review

## Integrity
Use database-enforced invariants where appropriate: primary keys, foreign keys,
unique constraints, NOT NULL, and checks. Application validation alone may lose
races under concurrency.

## Transactions
Use transactions when multiple state changes must succeed or fail together.
Keep transactions bounded and avoid unnecessary network calls inside them.

## Concurrency
Look for read-then-write races, duplicate creation, overselling/reservation
races, and lost updates. Choose locking, atomic operations, constraints, or
optimistic concurrency according to the workload.

## Queries
Look for N+1 access, unbounded reads, unnecessary columns, repeated queries,
expensive joins, and missing pagination.

## Indexes
Consider indexes based on real filters, joins, ordering, uniqueness, and query
patterns. Composite index order matters. Do not add indexes indiscriminately.

## Connections
Reuse clients correctly, configure pool limits intentionally, close resources
gracefully, and consider aggregate connections across all application instances.

## Migrations
Review destructive changes, backfills, locks, compatibility during rolling
deployments, and rollback/recovery strategy.

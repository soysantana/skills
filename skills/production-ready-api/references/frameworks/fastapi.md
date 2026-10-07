# FastAPI Production Review

Inspect application creation, routers, dependencies, Pydantic models,
authentication dependencies, exception handlers, database sessions, and server
deployment configuration.

Check:
- Pydantic/runtime validation
- authorization beyond authentication dependencies
- sync blocking work inside async endpoints
- DB session lifecycle
- transaction boundaries
- exception mapping
- CORS
- proxy/forwarded-header trust
- worker/process deployment assumptions
- startup/shutdown lifespan resources

Do not assume more workers always improve throughput; database and memory
capacity constrain safe concurrency.

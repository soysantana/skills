# Architecture Review

Use this reference when architecture affects production reliability or change safety.

## Boundaries
Check whether transport, application/business logic, persistence, and external
integrations have understandable boundaries. Framework decorators alone are not
an architectural problem.

## Dependency Direction
Look for concrete harmful coupling:
- domain/application logic importing HTTP-specific details unnecessarily
- controllers containing substantial business transactions
- persistence concerns leaking through the entire application
- circular dependencies masking unclear ownership

## Change Safety
Prefer existing conventions when sound. Recommend restructuring only when it
reduces an evidenced reliability, testability, or maintenance risk.

## Shared State
Identify unsafe process-local state when multiple instances may run.

## External Dependencies
Use timeouts and explicit failure handling for network dependencies. Consider
retries only for operations that are safe to retry. Avoid retry storms.

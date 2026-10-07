# HTTP and Error Handling

## Status Semantics

Use HTTP status codes according to their standard semantics and the project's established API contract.

- `200 OK` — Request completed successfully and returns a response body.
- `201 Created` — A new resource was successfully created.
- `204 No Content` — Request completed successfully with no response body.
- `400 Bad Request` — The request is malformed or structurally invalid.
- `401 Unauthorized` — Authentication credentials are missing, invalid, or expired.
- `403 Forbidden` — The caller is authenticated but not permitted to perform the operation.
- `404 Not Found` — The requested resource does not exist or cannot be found.
- `409 Conflict` — The request conflicts with the current state of the resource or system.
- `422 Unprocessable Content` — The request is structurally valid but semantically invalid, when this distinction is part of the project's API convention.
- `429 Too Many Requests` — The caller has exceeded an applicable rate limit.
- `500 Internal Server Error` — An unexpected server-side failure occurred.
- `503 Service Unavailable` — The service is temporarily unable to process the request.

Do not change an intentional, valid existing API contract merely to enforce a preferred convention. Apply status codes consistently across equivalent operations and failure modes.

## Error Shape

Prefer a stable, machine-readable error contract. Keep fields generic and independent of frameworks, persistence technologies, or transport implementations.

For example:

```json
{
  "code": "RESOURCE_NOT_FOUND",
  "message": "Resource not found",
  "requestId": "..."
}
```

Additional metadata may be included when useful, provided the error contract remains consistent and does not expose implementation details.

For validation failures, structured field-level details may be appropriate:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Request validation failed",
  "requestId": "...",
  "errors": [
    {
      "field": "fieldName",
      "code": "INVALID_VALUE",
      "message": "Invalid value"
    }
  ]
}
```

Error codes should be stable enough for programmatic handling. Human-readable messages may provide context but should not be the client's primary mechanism for identifying error types.

## Error Mapping

Map expected domain and application failures deliberately to appropriate transport-level responses.

Keep domain/application errors independent of HTTP concerns when the architecture separates those responsibilities. Translate them at the system boundary rather than coupling core business logic to HTTP status codes.

Handle unexpected exceptions centrally when supported by the framework or runtime.

Do not expose internal implementation details to clients. Never return raw database or ORM errors, stack traces, internal exception objects, credentials, queries, filesystem paths, or other sensitive diagnostic information.

Log sufficient internal context for diagnostics while returning a safe and stable external error representation.
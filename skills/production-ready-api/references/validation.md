# Input Validation

Validate external data at trust boundaries using runtime validation.

Check:
- required/optional fields
- primitive and structured types
- numeric/string bounds
- enum/allow-list values
- nested objects
- arrays and maximum sizes
- identifiers
- dates and time zones
- uploaded file constraints when applicable

Static types do not validate runtime input.

## Unknown Fields
Choose reject, strip, or explicitly allow based on the API contract. Be alert
to mass-assignment when arbitrary client fields reach persistence models.

## Normalization
Normalize only when semantics are clear. Do not silently transform security-
sensitive identifiers or credentials.

## Validation Errors
Keep errors useful and consistent without exposing internal implementation details.

# Authentication and Sessions

## Passwords
Use a purpose-built password hashing function with an appropriate work factor.
Never store or log plaintext passwords.

## Tokens
Verify signature/integrity, issuer/audience where applicable, expiration, and
the expected token type. Keep access tokens short-lived according to risk.

## Refresh Tokens / Sessions
Where revocation is required:
- store server-side session state or a revocable equivalent
- protect stored refresh credentials (prefer hashes where practical)
- rotate refresh credentials when the design requires it
- detect unsafe reuse when supported by the threat model
- revoke sessions explicitly on logout/security actions

## Cookies
For cookie-based credentials, review Secure, HttpOnly, SameSite, domain/path,
CSRF exposure, and deployment topology.

## Account Recovery
Password reset and verification tokens should be unpredictable, expire, and
normally be single-use.

## Enumeration
Avoid unnecessary account existence disclosure in sensitive recovery/login flows.

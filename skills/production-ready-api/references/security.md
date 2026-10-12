# API Security

## Authentication
Verify credentials are protected, token/session validation enforces expiration
and integrity, and authentication failures do not leak sensitive details.

## Authorization
Authentication is not authorization. Check resource/action boundaries for:
- BOLA/IDOR
- ownership bypass
- role/permission bypass
- administrative actions exposed to ordinary users
- user-controlled identifiers trusted without access checks

Never claim a vulnerability without a concrete path.

## Input
Treat body, query, params, headers, cookies, files, and webhook payloads as
untrusted. Validate type, shape, length, range, and allowed values.

## Secrets
Do not commit credentials, signing secrets, private keys, API keys, or service
account material. Required secrets should fail fast when missing.

## CORS
Avoid permissive origins with credentials. Define trusted browser origins based
on deployment requirements.

## Abuse Controls
Prioritize rate limiting/anti-abuse controls for login, password reset,
registration, OTP, verification, expensive searches, and public writes.

## Output and Logs
Do not expose stack traces, SQL errors, filesystem paths, tokens, passwords, or
sensitive request data.

# ASP.NET Core Production Review

Inspect `Program.cs`, middleware ordering, authentication/authorization,
controllers/minimal APIs, model validation, exception handling, EF Core,
configuration, health checks, and hosting settings.

Check:
- authentication scheme configuration
- authorization policies/resource checks
- forwarded headers/proxy trust
- HTTPS behavior behind proxies
- exception handling/ProblemDetails
- request limits and CORS
- EF Core query/transaction behavior
- health checks
- Data Protection when relevant
- graceful host shutdown

Middleware ordering can change security and routing behavior; verify it
against the application's hosting model.

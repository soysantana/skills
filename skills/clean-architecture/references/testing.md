# Testing Strategy

Test policies at the cheapest boundary that proves them.

## Domain tests

Test invariants and domain behavior directly. No framework, network, or database should be required for ordinary domain tests.

## Use-case tests

Instantiate use cases with fakes/stubs/in-memory implementations of boundary interfaces. Verify application behavior and interaction contracts without booting the full application.

## Adapter tests

Test translation and integration behavior for controllers, persistence adapters, serializers, gateways, and vendor integrations.

## End-to-end tests

Use a smaller set to verify wiring and critical flows across real outer components.

## Architecture tests

When tooling permits, enforce dependency rules automatically, such as preventing domain/application packages from importing infrastructure or framework packages.

A test suite should make replacing an outer detail substantially safer without requiring inner-policy tests to change.

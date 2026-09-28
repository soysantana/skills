# Project Structure

Structure by business capability when possible, with architectural boundaries visible inside or across capabilities.

## Feature-oriented example

```text
src/
  orders/
    domain/
    application/
    adapters/
  customers/
    domain/
    application/
    adapters/
  infrastructure/
  main/
```

## Layer-oriented example

```text
src/
  domain/
  application/
  adapters/
  infrastructure/
  main/
```

Choose based on project size and cohesion. Names are not architecture; dependency direction and responsibility separation are.

## Composition root

Keep object construction, framework bootstrapping, dependency injection bindings, environment configuration, and concrete adapter selection near the outermost layer.

## Practical constraints

- Small applications may combine adjacent layers while preserving dependency direction.
- Avoid one-file-per-pattern ceremony.
- Do not move code simply to make the tree resemble a canonical diagram.
- Prefer cohesive modules with explicit public boundaries.

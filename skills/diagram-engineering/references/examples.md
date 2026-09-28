# Compact Examples

These are patterns, not universal templates.

## Flowchart — validation pipeline

```mermaid
flowchart TD
    A[Receive request] --> B{Schema valid?}
    B -- No --> C[Return validation error]
    B -- Yes --> D[Authorize request]
    D --> E{Authorized?}
    E -- No --> F[Return forbidden]
    E -- Yes --> G[Execute use case]
```

## Sequence — login

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant API
    participant Auth
    User->>UI: Submit credentials
    UI->>API: POST /sessions
    API->>Auth: Verify credentials
    alt valid
        Auth-->>API: Identity
        API-->>UI: Session
    else invalid
        Auth-->>API: Rejected
        API-->>UI: 401 Unauthorized
    end
```

## ERD — users and sessions

```mermaid
erDiagram
    USER ||--o{ SESSION : has
    USER {
      string id PK
      string email UK
    }
    SESSION {
      string id PK
      string user_id FK
      datetime expires_at
      datetime revoked_at
    }
```

## State — order lifecycle

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Paid: payment_confirmed
    Pending --> Cancelled: cancel
    Paid --> Fulfilled: fulfill
    Paid --> Refunded: refund
    Fulfilled --> [*]
    Cancelled --> [*]
    Refunded --> [*]
```

## Architecture — lightweight C4-like view

```mermaid
flowchart LR
    U[Customer] -->|HTTPS| W[Web App]
    W -->|JSON/HTTPS| A[API]
    A -->|SQL| D[(Database)]
    A -->|publish event| Q[[Message Broker]]
    Q --> N[Notification Worker]
```

Use a true C4 notation when explicit C4 semantics are required.

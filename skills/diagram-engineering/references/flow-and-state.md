# Flow, Activity, and State Modeling

## Flowcharts / activity

Model actions and decisions explicitly.

- Start/end should be identifiable when the process has meaningful boundaries.
- Decision labels should be questions or conditions; outgoing branches should state mutually understandable outcomes such as Yes/No or guards.
- Avoid a decision diamond with unlabeled branches.
- Model loops with an explicit condition and visible return path.
- Separate parallel work from mutually exclusive branching.
- Show exceptional/error paths when they change the engineering behavior.
- Prefer verb phrases for actions: `Validate token`, `Persist order`.
- If ownership matters, use lanes/groups rather than prefixes on every action.

## State machines

A state is a durable condition, not an action.

- Name states as conditions/nouns: `Pending`, `Authenticated`, `Closed`.
- Label transitions with `event [guard] / action` when those distinctions matter.
- An action like `Send email` is usually transition behavior, not a state.
- Check reachability: no accidental orphan states.
- Check terminal states and whether exits are valid.
- Check whether the same event from the same state has conflicting guards.
- Model retries/timeouts as events/transitions when they affect lifecycle.

## Common anti-patterns

- Flowchart used to imitate a sequence diagram.
- State diagram where every state is a verb.
- Hidden loop caused by an arrow back to an unlabeled node.
- Mixing business workflow and implementation function calls in one view.

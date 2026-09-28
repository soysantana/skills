# Diagram Quality Rubric

Use this as a checklist, not a numeric score unless the user explicitly requests scoring.

## Semantic integrity

- Every element represents a real concept in scope.
- Every edge has the intended semantic meaning.
- Direction is correct and consistent.
- Cardinality, multiplicity, ordering, guards, protocols, states, and dependencies are shown when material.
- No inferred fact is presented as established.
- Diagram matches supplied code/schema/requirements.

## Purpose and scope

- Title/question makes the purpose clear.
- System/process boundary is explicit where needed.
- External actors/systems are distinguishable from internals.
- One abstraction level dominates each view.
- Details irrelevant to the question are removed.

## Cognitive load

- Major concepts can be identified in seconds.
- Labels are short and domain-specific.
- Edge crossings and backward edges are minimized.
- Repetition is factored into groups/notes where safe.
- Dense regions are split rather than shrunk into unreadability.

## Consistency

- Naming convention is stable.
- Same visual shape means same kind of thing.
- Direction/layout convention is stable.
- Similar relations use similar notation.
- Acronyms are expanded when the audience may not know them.

## Accessibility

- Meaning survives grayscale/color-blind viewing.
- Contrast is sufficient in rendered output.
- Text remains legible at normal viewing size.
- Color supplements labels/shapes; it does not replace them.

## Audit severity

**Critical:** likely to cause a wrong implementation/decision: reversed dependency, impossible state transition, false cardinality, wrong actor/system boundary, incorrect message order.

**Major:** materially ambiguous or incomplete: unlabeled relation with multiple interpretations, missing important branch, mixed abstraction, absent failure path central to the scenario.

**Minor:** readability/maintainability: inconsistent casing, avoidable crossing, verbose labels, cosmetic imbalance.

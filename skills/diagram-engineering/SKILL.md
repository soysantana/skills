---
name: diagram-engineering
description: 'Engineers, audits, improves, and explains software and systems diagrams. Use when creating or reviewing flowcharts, UML/class/sequence/state/activity diagrams, ERDs, C4/architecture diagrams, mindmaps, dependency graphs, Git graphs, Gantt charts, Kanban flows, requirements, timelines, user journeys, Wardley maps, or Mermaid/PlantUML/D2/Graphviz/Structurizr-style diagram-as-code.'
license: MIT
compatibility: 'Portable Agent Skill; optional Python 3.9+ for bundled validators.'
---

# Diagram Engineering

Design diagrams as engineering models, not decoration. Optimize for correctness, audience, scope, traceability, and fast comprehension.

## Core workflow

1. Identify the question the diagram must answer and its audience.
2. Choose the smallest diagram family that answers that question. Do not default to flowcharts.
3. Extract actors, boundaries, entities/components, states/events, relationships, decisions, constraints, and invariants from the available evidence.
4. Mark unknowns. Never invent architecture, cardinality, protocol, state transitions, or ownership to make a diagram look complete.
5. Build a semantic model before styling it.
6. Generate diagram-as-code when the requested/available renderer supports it.
7. Audit correctness and readability independently.
8. Simplify until every retained node/edge helps answer the diagram's question.
9. Return assumptions and material findings with the diagram.

## Select the diagram

Read [references/diagram-selection.md](references/diagram-selection.md) when the diagram type is not explicit or multiple views may be required.

Fast routing:

- Branching process, business logic, algorithm -> flowchart/activity.
- Runtime messages and call order -> sequence.
- Static domain/software structure -> class.
- Data model and cardinality -> ERD.
- Lifecycle and event-driven transitions -> state machine.
- System landscape, containers, components -> C4/architecture.
- Dependencies/topology -> block/dependency graph.
- Planning over time -> Gantt/timeline.
- Work-in-progress -> Kanban.
- Causes of an outcome -> Ishikawa.
- Requirements and traceability -> requirement diagram.
- User experience across steps -> user journey.
- Version-control history -> Git graph.
- Strategic value chain/evolution -> Wardley map.
- Hierarchy -> tree/mindmap; use mindmaps for ideation, trees for explicit hierarchy.
- Quantitative composition/flow -> pie, Sankey, treemap, quadrant, radar only when the data semantics justify them.

## Model before rendering

Write a compact intermediate model when the request is non-trivial:

- **Purpose:** one sentence.
- **Audience:** developer, architect, product, operations, stakeholder, learner, etc.
- **Scope/boundary:** what is inside and outside.
- **Elements:** stable IDs + concise labels.
- **Relations:** source -> relation -> target.
- **Rules:** cardinality, direction, guards, protocols, sync/async, ownership, or state constraints where relevant.
- **Unknowns:** facts not established by evidence.

If source code, schemas, APIs, requirements, logs, or an existing diagram are supplied, treat them as evidence. Prefer evidence over convention.

## Diagram construction rules

- One diagram should answer one primary question.
- Use stable domain terminology from the source.
- Prefer 5-9 major concepts per visual region; split dense models into views.
- Give relationships meaningful labels when direction alone is ambiguous.
- Show boundaries before internals on architecture diagrams.
- Keep abstraction levels consistent within a view.
- Avoid crossing edges when a layout change or subgraph can remove them.
- Do not encode meaning by color alone.
- Avoid decorative icons unless they improve recognition without changing semantics.
- Use notes for exceptional constraints, not paragraphs inside nodes.
- For large systems, create an overview plus focused drill-down diagrams instead of a single "mega diagram".

Read [references/quality-rubric.md](references/quality-rubric.md) before auditing or substantially revising an existing diagram.

## Semantic rules by family

Read only the relevant reference:

- [references/flow-and-state.md](references/flow-and-state.md) — flowchart, activity, state, decision logic.
- [references/uml-and-data.md](references/uml-and-data.md) — class, sequence, ERD, enUML-style modeling.
- [references/architecture-c4.md](references/architecture-c4.md) — architecture, C4, blocks, boundaries, dependencies.
- [references/planning-and-analysis.md](references/planning-and-analysis.md) — Gantt, Kanban, timeline, journey, Ishikawa, requirement, Wardley, quantitative diagrams.
- [references/notation-targets.md](references/notation-targets.md) — Mermaid, PlantUML, D2, Graphviz, Structurizr and renderer constraints.

## Audit mode

When asked to review, audit, improve, or fix a diagram:

1. Reconstruct what the current diagram claims before editing it.
2. Separate **semantic defects** from **presentation defects**.
3. Prioritize findings: critical (misleading/wrong), major (ambiguous/incomplete), minor (readability/consistency).
4. Check the diagram against source evidence when available.
5. Preserve correct information even if notation is imperfect.
6. Propose the smallest changes that fix the defects.
7. If a redesign is materially clearer, provide a revised model/diagram and explain the structural change briefly.

Audit at least: purpose fit, scope, completeness, correctness, relation semantics, direction, cardinality/state/ordering where applicable, abstraction consistency, naming, visual complexity, accessibility, and unsupported assumptions.

## Improve mode

Improve in this order:

1. Correct false semantics.
2. Add missing high-value semantics.
3. Remove irrelevant detail.
4. Split mixed abstraction levels.
5. Reduce crossings and long edge travel.
6. Normalize names and relationship labels.
7. Improve grouping and visual hierarchy.
8. Apply restrained styling last.

Never "improve" a diagram by silently changing its meaning.

## Diagram-as-code output

Use the user's requested syntax. If none is requested:

- Prefer Mermaid for common Markdown-friendly diagrams when it can represent the semantics faithfully.
- Prefer PlantUML for richer UML behavior.
- Prefer Structurizr/C4-compatible notation when architecture modeling requires explicit C4 semantics.
- Prefer Graphviz/D2 for topology/layout-heavy graphs when appropriate.
- If a target cannot faithfully express the model, say so and use a better-supported notation rather than faking semantics.

Keep generated source deterministic: stable IDs, consistent direction, grouped declarations, concise comments only where useful.

For Mermaid output, optionally run:

`python3 scripts/lint_mermaid.py path/to/diagram.mmd`

This is a lightweight structural lint, not a replacement for the official renderer/parser.

## Response contract

For creation requests, normally return:

1. **Diagram** — renderable source or requested artifact.
2. **Assumptions** — only assumptions that affect semantics; omit if none.
3. **Notes** — short explanation of boundaries or notation choices when needed.

For audits, return:

1. **Findings** — ordered by severity and tied to concrete elements.
2. **Revised diagram** — when requested or when a direct correction is useful.
3. **Unresolved questions** — only blockers or material uncertainties.

Do not force a long report for a small diagram.

## Examples

Read [references/examples.md](references/examples.md) only when an example pattern is useful. Reusable starter files are under `assets/examples/`.

## Engineering basis

This skill synthesizes established diagramming and software-design practices rather than reproducing books. See [references/bibliography.md](references/bibliography.md) for the conceptual sources and official notation documentation. Do not quote or reconstruct copyrighted book text beyond brief fair-use excerpts supplied by the user.

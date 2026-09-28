# Planning and Analysis Diagram Rules

## Gantt

- Tasks require meaningful start/end or duration.
- Dependencies should reflect real scheduling constraints.
- Milestones are zero-duration events, not ordinary tasks.
- Do not imply precision the plan does not have.

## Kanban

- Columns represent workflow states, not departments unless that is the actual workflow.
- Make blocked work explicit.
- WIP limits belong to the workflow policy when known.

## Timeline

- Use for ordered events where duration/dependency detail is secondary.
- Keep granularity consistent.

## User journey

- Organize by user goal/stage.
- Distinguish user actions from system/internal actions.
- Sentiment/score should come from evidence or be clearly hypothetical.

## Ishikawa

- Put the observed effect at the head.
- Branches are cause categories; leaves are candidate causes.
- Do not present brainstormed causes as proven root causes.

## Requirements

- Give requirements stable IDs.
- Preserve relation semantics: contains, derives, satisfies, verifies, traces, depends.
- Do not claim traceability without evidence.

## Wardley maps

- Separate value-chain position from evolution/maturity.
- Map user need/value first; technology inventory alone is not a Wardley map.
- Evolution placement is an analytical judgment and should be labeled as such when uncertain.

## Quantitative diagrams

- Sankey: edge width must encode a quantity with consistent units.
- Pie: use for part-to-whole with few categories totaling the whole.
- Treemap: use area for hierarchical part-to-whole.
- Radar: compare multivariate profiles with common scales; avoid pretending polygon area is a precise metric.
- Quadrant: define both axes and thresholds.
- Venn: use only when set intersections are meaningful and exhaustive geometry is not misleading.

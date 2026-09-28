# Diagram Selection

Choose by the question, not by familiarity.

| Question | Primary view | Avoid using it for |
|---|---|---|
| What steps/decisions occur? | Flowchart / activity | Runtime object messaging |
| Who calls whom, and in what order? | Sequence | Static dependency inventory |
| What types and relationships exist? | Class | Database physical design by default |
| How is persisted data related? | ERD | Runtime behavior |
| How can an entity/system change state? | State | General process steps without persistent state |
| What systems/containers/components exist and depend on each other? | C4 / architecture | Detailed algorithms |
| What depends on what? | Dependency/block graph | Temporal ordering unless explicitly encoded |
| What happens when? | Timeline / Gantt | Static structure |
| What work is queued/in progress/done? | Kanban | System architecture |
| Why might an outcome occur? | Ishikawa | Process execution |
| Which requirements relate/satisfy/derive? | Requirement | General brainstorming |
| What does a user experience across stages? | User journey | Internal call sequence |
| How did branches/commits evolve? | Git graph | Deployment topology |
| What is hierarchical? | Tree | Cyclic networks |
| What ideas radiate from a concept? | Mindmap | Precise dependency semantics |
| How does quantity flow? | Sankey | Unweighted process flow |
| How is area/composition distributed? | Treemap/pie | Precise comparison across many values |
| How do dimensions compare? | Radar | Accurate magnitude comparison when bars work better |
| How do two dimensions classify items? | Quadrant | Continuous causal relationships |
| How does strategic value/evolution map? | Wardley | Generic architecture |

## Multi-view rule

Use multiple diagrams when the question spans distinct dimensions. Typical software set:

1. Context/architecture: where the system sits.
2. Container/component: how it is decomposed.
3. Sequence: how one important scenario executes.
4. ERD/class: how important information/domain concepts relate.
5. State/activity: how lifecycle or workflow behaves.

Do not merge these merely to produce one picture.

## Decision heuristics

- If edges mean **next**, use flow/activity.
- If edges mean **message**, use sequence.
- If edges mean **is/has/depends**, use class/architecture.
- If edges mean **foreign-key/cardinality**, use ERD.
- If edges mean **transition triggered by event**, use state.
- If the x-axis is inherently time, consider timeline/Gantt.

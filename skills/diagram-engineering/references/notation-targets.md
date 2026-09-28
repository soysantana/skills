# Notation Targets

Syntax evolves. When exact renderer/version behavior matters, consult the current official documentation for the target tool.

## Mermaid

Good default for Markdown-centric workflows. Common families include flowchart, sequence, class, state, ER, Gantt, Git graph, mindmap, timeline, journey, requirement and other evolving diagram types.

Rules:
- Use stable node IDs separate from display labels.
- Quote/escape labels that contain syntax-significant characters.
- Prefer subgraphs for meaningful grouping, not merely layout hacks.
- Keep syntax within features supported by the user's Mermaid version.
- If an exotic diagram family is version-sensitive, verify current Mermaid support rather than guessing.

## PlantUML

Prefer when richer UML semantics or mature sequence/class/state notation is required. Keep stereotypes and skin parameters restrained; model semantics before styling.

## Structurizr DSL / C4

Prefer when the architecture should be maintained as a model with multiple C4 views. Reuse model elements across views rather than redefining inconsistent copies.

## D2

Useful for readable diagram-as-code and flexible layouts. Use explicit labels and containers; verify target layout engine availability when layout behavior matters.

## Graphviz DOT

Useful for general directed/undirected graphs and layout-heavy dependency maps. Encode semantic grouping with subgraphs/clusters carefully; DOT edges do not inherently mean a particular software relation.

## Renderer principle

Never claim a syntax is valid merely because it looks plausible. If no parser/renderer is available, label syntax-sensitive output as unvalidated.

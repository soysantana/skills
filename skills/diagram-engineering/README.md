# diagram-engineering

An Agent Skill for creating, selecting, auditing, simplifying, and improving engineering diagrams for software and systems work.

It covers flowcharts, UML/class/sequence/state, ERDs, C4/architecture, dependency/block diagrams, Gantt, Git graphs, Ishikawa, Kanban, mindmaps, requirements, Sankey, timelines, trees, user journeys, Venn, Wardley maps, and related diagram-as-code workflows.

## Install from a GitHub repository

After pushing the skill to a public repository, install it with the skills CLI pattern used by skills.sh:

```bash
npx skills add https://github.com/soysantana/skills --skill diagram-engineering
```

If the repository contains only this skill, the installer may also discover it directly from the repository URL.

## What it does

- Selects the right diagram type from the engineering question.
- Creates diagrams from requirements, source code, schemas, APIs, or prose.
- Audits existing diagrams for semantic and readability defects.
- Improves diagrams without silently changing their meaning.
- Supports Mermaid-first output plus PlantUML, D2, Graphviz and C4/Structurizr guidance.
- Uses progressive disclosure: detailed references load only when relevant.

## Repository layout

```text
diagram-engineering/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
├── scripts/
└── assets/examples/
```

## Validate

```bash
python3 scripts/check_skill.py
python3 scripts/lint_mermaid.py assets/examples/software-request-flow.mmd
```

## Example prompts

- "Audit this Mermaid architecture diagram and fix semantic problems."
- "Create the best diagram for this NestJS authentication flow."
- "Turn this Prisma schema into an ERD and flag suspicious cardinalities."
- "Create a C4 context and container view from this architecture description."
- "Simplify this sequence diagram for onboarding a junior developer."
- "Review this state machine for unreachable or ambiguous transitions."

## Design philosophy

The skill is based on established software architecture, UML, domain modeling, C4, information visualization, Kanban, and Wardley Mapping literature. It contains original workflow guidance and does not reproduce copyrighted book content.

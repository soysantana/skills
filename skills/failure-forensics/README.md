# failure-forensics

An Agent Skill for investigating failures with evidence-first timelines, blameless causal analysis, premortems, and concrete corrective actions.

It covers incidents, outages, regressions, flaky tests, hard-to-reproduce bugs, risky launches, migrations, resilience rehearsals, and "what could go wrong?" planning.

## Install from a GitHub repository

After pushing the skill to a public repository, install it with the skills CLI pattern used by skills.sh:

```bash
npx skills add https://github.com/soysantana/skills --skill failure-forensics
```

## What it does

- Separates facts, inferences, hypotheses, and unknowns.
- Builds incident timelines before jumping to cause.
- Finds contributing conditions instead of blaming people.
- Turns postmortems and premortems into verifiable engineering actions.
- Helps isolate flaky tests and intermittent bugs through hypothesis-driven experiments.
- Uses progressive disclosure: detailed references load only when relevant.

## Repository layout

```text
failure-forensics/
├── SKILL.md
├── README.md
└── references/
```

## Example prompts

- "Analyze this outage timeline and write a blameless postmortem."
- "We are migrating billing data next week. Run a premortem."
- "This CI test fails 1 in 40 runs. Build an isolation plan."
- "Review these incident actions and make them stronger."
- "What monitoring would have detected this regression earlier?"

## Design philosophy

The skill is based on blameless postmortem practice, SRE incident review, resilience engineering, chaos engineering, premortems, and practical flaky-test triage. It contains original workflow guidance and avoids inventing facts when evidence is missing.

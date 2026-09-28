# UML and Data Modeling

## Class diagrams

Use class diagrams for domain/static software structure.

- Distinguish inheritance/generalization from association/dependency.
- Use composition only when lifecycle ownership is genuinely strong.
- Show multiplicity where it changes understanding.
- Do not dump every private field/method; include members relevant to the question.
- Separate domain classes from infrastructure classes if mixing them obscures the model.

## Sequence diagrams

Sequence diagrams answer ordering and collaboration questions.

- Participants should have stable roles; order them to reduce crossing.
- Messages should be verbs and correspond to real calls/events when evidence exists.
- Distinguish synchronous request/response from asynchronous messages when material.
- Use `alt/else`, `opt`, `loop`, and parallel fragments for real control structures.
- Include failure/timeout branches when central to the scenario.
- Do not invent return values just to make symmetry.
- Keep one scenario/use case per sequence unless comparison is the purpose.

## Entity-relationship diagrams

ERDs model persisted information and relationship constraints.

- Identify primary keys and foreign keys when physical/logical detail is requested.
- Show optionality and cardinality accurately.
- Resolve many-to-many relationships with associative entities when modeling relational implementation.
- Separate conceptual entities from tables when the distinction matters.
- Do not infer one-to-one from naming alone.
- Avoid duplicating derived fields unless persistence is intentional.

## enUML / text UML targets

When generating a text notation, preserve UML semantics first. Syntax convenience must not turn aggregation into composition, dependency into inheritance, or a message into an association.

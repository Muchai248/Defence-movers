# Agent Instructions

<!-- agent-memory:start -->
## Agent Memory Knowledge Base

Query, context, show and audit default to format 2 in this repository. Explicit `--format-version 1` or `--format-version 2` overrides the default. Recompile after changing the default; canonical claims remain unchanged.

Use the repo-memory skill or instruction file whenever it is available. This section is the repo-level fallback and requirement.

Durable repository knowledge lives in `docs/agent-memory/` and must stay versioned and reviewable. The SQLite cache is user-local global state resolved at runtime by `agent-memory`. Repository-local plan runs and other checkout state live in `.agent-memory/`. Generated state must not be committed.

Memory artifacts:

- `claims/`: atomic behavior, rules, constraints, workflows, risks, decisions, and deprecations.
- `graph/`: relationships between claim IDs, including dependencies, constraints, conflicts, and replacements.
- `indexes/`: watched files, default queries, tags, and claim globs for discoverability.
- `recipes/`: repeatable implementation, debugging, release, or review workflows.
- `plans/`: reusable multi-stage workflow templates; local plan runs stay under `.agent-memory/plans/`.
- `profiles/`: small profile traits that shape retrieval, output, verification, risk lens, or scope.
- `waivers/`: reviewed exceptions for memory coverage checks.

### Agent-Memory-First Workflow

Before non-trivial work:

1. Run `agent-memory sync`.
2. Run `agent-memory context --task "<task>"`.
3. If files are known, run `agent-memory context --changed-files <file1> <file2>`.
4. If working from a diff, run `agent-memory context --git-diff`.
5. Use `agent-memory query`, `agent-memory show`, or `agent-memory system` for precise claims, graph links, recipes, or watched-file context.
6. If context includes matched recipes, follow their required claims, verification, and memory-update prompts.
7. If context includes a plan stage, work that stage unless the user broadens scope.
8. If context includes profile traits, treat them as repo guidance below system, developer, user, and repository instruction-file guidance.

For non-trivial work, cite the relevant claim IDs, system IDs, and verification commands in plans or PR notes.

### Memory-Worthiness Gate

Search existing claims and recipes before creating new memory. Update or deprecate existing memory when it already owns the knowledge.

A new claim should normally satisfy at least four of these five tests:

1. Repository-specific: it is not generic engineering knowledge.
2. Future-relevant: a later task is likely to need it.
3. Durable: it should remain true beyond the current task or implementation moment.
4. Consequential: forgetting it could cause an incorrect change, meaningful risk, or repeated investigation.
5. Evidence-backed: code, tests, configuration, documentation, or another concrete source can verify it.

Choose the narrowest suitable artifact:

- Claim: one durable fact, rule, constraint, decision, risk, or lifecycle invariant.
- Recipe: a repeatable agent procedure with repository-specific steps, ordering, safeguards, or verification.
- Index: discoverability, file ownership, watched paths, routes, jobs, models, or search terms.
- Local plan run: one-off task execution state; do not commit it.
- Waiver: a reviewed, time-boxed exception where watched-file coverage intentionally does not require a memory update.
- No durable memory: formatting-only work, routine refactors, temporary debugging observations, generic best practices, or facts obvious from one local definition.

A claim tells future agents what is true or must remain true. A recipe tells future agents how to perform a recurring task safely. Do not create a claim merely because code changed or coverage reported a gap, and do not create placeholder memory to satisfy coverage.

`agent-memory new claim` and `agent-memory new recipe` create `needs_review` drafts. Claims start with low confidence. Replace every TODO, complete verification, and only then promote an artifact to `current`. Current claims or recipes containing TODO placeholders fail validation.

When claim verification succeeds, record the tested full Git commit object ID in `last_verified_commit`. Do not use a movable ref such as a branch or `HEAD`. Use `confidence: verified` only when that commit is present. Audit warns when supporting files changed after the recorded verification commit.

### Claim Source Policy

`claim_sources.allow` and `claim_sources.deny` in `agent-memory.config.yaml` control which repository files may be referenced by claims and which changed files participate in claim coverage. An empty allow list permits all repository paths; deny patterns always win.

- Allowed claim sources: all repository paths
- Denied claim sources: none

Do not attach claims to denied paths indirectly through `related_files`. If a changed file is policy-excluded, leave it without a claim unless the policy itself should be changed.

After non-trivial work:

1. Update memory in the same change when durable repository knowledge changed.
2. Use `agent-memory templates list`, `agent-memory new claim`, or `agent-memory new recipe` instead of inventing artifact formats.
3. Run `agent-memory validate` and `agent-memory sync` before finishing changes that touch memory.
4. Run `agent-memory audit --git-diff` before finishing when canonical memory files changed.

Update targets:

- Claims for changed behavior, interfaces, system boundaries, auth rules, dependencies, risks, or decisions.
- Graphs for changed triggers, handoffs, constraints, replacements, conflicts, or causal links.
- Indexes for changed route/job/model discoverability, watched files, default queries, or tags.
- Recipes for new or changed repeatable workflows.
- Plan templates for reusable multi-stage workflows; finish or prune local plan runs instead of committing them.
- Profile traits for reusable retrieval/output/verification/risk/scope guidance.
- Waivers for intentional coverage exceptions with a reason and expiration.
<!-- agent-memory:end -->

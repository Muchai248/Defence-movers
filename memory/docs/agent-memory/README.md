# Agent Memory

This repository uses `agent-memory` for durable agent-readable memory.

Canonical memory lives in:

- `claims/**/*.md`
- `graph/**/*.yaml`
- `indexes/**/*.yaml`
- `recipes/**/*.yaml`
- `plans/**/*.yaml`
- `profiles/**/*.yaml`

The SQLite cache is user-local global state resolved by `agent-memory`. Repository-local plan runs live in `.agent-memory/plans/`. Generated state should not be committed.

---
id: memory.memory_repo_located_at_home_sankofaconnectsolutions_memory_agent_memory
type: fact
system: memory
status: needs_review
confidence: medium
severity: normal

title: Memory repo located at /home/sankofaconnectsolutions/memory/agent-memory

claim: >
  The Agent Memory Repo (simple git-based memory) is located at /home/sankofaconnectsolutions/memory/agent-memory.

source_files:
  - agent-memory.config.yaml

related_files: []
symbols: []
routes: []
tags:
  - memory
  - configuration

verification:
  - Directory exists and contains MEMORY.md file

last_verified_commit: null
---

# Memory repo located at /home/sankofaconnectsolutions/memory/agent-memory

## Claim

The Agent Memory Repo (simple git-based memory) is located at /home/sankofaconnectsolutions/memory/agent-memory.

## Why It Matters

This path is needed to reuse memory in future sessions by invoking the agent-memory-repo skill.

## Evidence

- Directory created during session setup
- Contains MEMORY.md with user's name

## Verification

- Directory exists and contains MEMORY.md file

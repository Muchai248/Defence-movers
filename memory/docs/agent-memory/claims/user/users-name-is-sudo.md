---
id: user.users_name_is_sudo
type: fact
system: user
status: needs_review
confidence: medium
severity: normal

title: User's name is sudo

claim: >
  The user prefers to be addressed as "sudo".

source_files:
  - agent-memory/MEMORY.md

related_files: []
symbols: []
routes: []
tags:
  - user
  - preference

verification:
  - User explicitly stated their name is "sudo"

last_verified_commit: null
---

# User's name is sudo

## Claim

The user prefers to be addressed as "sudo".

## Why It Matters

Personalization and addressing the user correctly improves interaction quality.

## Evidence

- Direct user statement during session

## Verification

- User explicitly stated their name is "sudo"

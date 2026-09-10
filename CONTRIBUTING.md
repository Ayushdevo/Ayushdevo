# Contributing

This repository is the source of truth for the public developer profile and its supporting automation.

## Before changing anything

1. Read the relevant documentation in `docs/`.
2. Prefer small, reviewable changes.
3. Do not add generated assets when a reproducible workflow can create them.
4. Keep external services documented and replaceable.

## Profile changes

Profile-facing edits should preserve the existing sections unless there is a clear reason to change the information architecture. Verify Markdown, image URLs, and badges before merging.

## Automation changes

Workflow changes should be deterministic, use least-privilege permissions, and expose failures clearly. Pin actions to stable major versions and avoid storing secrets in the repository.

## Pull requests

Use the repository PR template. Explain the problem, the change, and how it was validated.

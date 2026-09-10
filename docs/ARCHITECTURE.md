# Profile Repository Architecture

The repository has three logical layers:

```text
Profile presentation
        │
        ├── README.md
        └── generated visual assets

Repository governance
        │
        ├── .github/
        ├── CODEOWNERS
        ├── CONTRIBUTING.md
        └── SECURITY.md

Profile data and automation
        │
        ├── profile/
        ├── scripts/
        └── .github/workflows/
```

## Design principles

- `README.md` is presentation, not a database.
- Structured data belongs under `profile/`.
- Validation belongs under `scripts/`.
- Repeatable checks belong in GitHub Actions.
- Documentation explains the contract between these layers.

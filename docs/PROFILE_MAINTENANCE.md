# Profile Maintenance

## Routine checks

When updating the profile:

1. Update structured data first when the information belongs in `profile/`.
2. Keep README claims factual and current.
3. Check every external link.
4. Review workflow permissions before changing automation.
5. Run the local validators before opening a pull request.

## Generated assets

Generated contribution visuals should remain reproducible. The repository should contain the workflow or documented command needed to regenerate them rather than relying on unexplained manual edits.

## External services

Badges and analytics cards depend on third-party services. Treat them as presentation dependencies: a service outage should not prevent the repository from being cloned, validated, or documented.

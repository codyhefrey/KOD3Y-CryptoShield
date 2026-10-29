# Community governance

KOD3Y CryptoShield Community is publicly visible and accepts proposed changes through issues and pull requests. The repository owner and designated maintainers decide what is merged and released.

## Maintainer-controlled operations
- Review contributions and decide acceptance.
- Review security-sensitive changes and dependency updates.
- Maintain release integrity and repository configuration.
- Keep Enterprise-only implementation and credentials outside Community.

## Required GitHub configuration (manual)
GitHub settings are not configured by this document. In Settings > Rules > Rulesets (or branch protection), create an active rule targeting the default branch (`main`):
- Require pull requests before merging.
- Require at least one approval and code-owner review where supported.
- Require passing GitHub Actions test checks (choose the actual reported check name after CI runs).
- Block force pushes and branch deletion.
- Restrict bypass permissions; include administrators where supported.
- Enable secret scanning and push protection if available.
- Limit write/admin permissions to trusted maintainers.

Do not mark a check required until it exists on the branch. Consider enabling Discussions and Issues in repository settings. Review settings periodically.

# Contributing to CR-Hopper

CR-Hopper publishes client-ready subscriptions from third-party public proxy sources and maintains a small static documentation website.

## Reporting and suggestions

Open an [Issue](https://github.com/Agumuzi/crhopper/issues) for website bugs, documentation/translation errors, malformed TXT or YAML output, or client compatibility issues.

**Do not share private node addresses, credentials, OAuth tokens or personal connection logs.** Public upstream nodes may expire or disappear; uptime, privacy and location are not guaranteed. For security vulnerabilities in project-maintained files, see [SECURITY.md](SECURITY.md).

## Important compatibility boundaries

- Keep `CR-Hopper.txt` and `CR-Hopper.yaml` at the repository root with their existing raw URLs. Existing subscribers rely on them.
- The static website under `docs/` is separate from the feed publishing process; keep it compatible with small screens.
- Preserve English, Simplified Chinese, Russian and Persian website translations when changing user-facing copy.
- Do not publish private scanner configurations, sync tokens, operational backups or client secrets.
- Do not represent third-party public nodes as operated, secured or guaranteed by CR-Hopper.

## Pull requests

Describe the problem and changed files; include before/after screenshots for layout changes, and manually verify link-copy interactions and both subscription URLs. Changes to public feed formats require compatibility testing with intended clients.

## Licensing caution

This repository currently has **no repository-wide open-source license**. Visibility on GitHub does not grant blanket permission to reuse or redistribute the project's code or documentation. Public third-party proxy entries and related metadata may have separate origins and rights. Do not assume the project can relicense upstream data.

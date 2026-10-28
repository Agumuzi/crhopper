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

## Licensing and contribution rights

Original project-maintained source code is available under [PolyForm Noncommercial 1.0.0](LICENSE) for permitted noncommercial use. Original project logos and artwork are reserved under [Brand & Visual Assets](ASSETS-LICENSE.md). Public third-party proxy entries and related metadata have separate origins and rights and are **not** relicensed by this project.

Only submit materials you have the right to contribute. By submitting code you allow its inclusion under this project's current terms; contributors retain their own copyrights, and the maintainer needs separate permission to license contributed material commercially.

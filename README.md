<div align="center">

<img src="docs/assets/rocket.svg" width="116" height="116" alt="CR-Hopper pixel rocket logo">

# CR-Hopper

**Curated public proxy feeds. Ready for your client.**

Free public proxy subscriptions for Hiddify, Mihomo and Clash-compatible clients.

[**Website / Quick Start**](https://agumuzi.github.io/crhopper/) · [☕ Support development](https://ko-fi.com/agumuzi) · [**TXT Feed**](https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt) · [**YAML Feed**](https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml) · [Issues](https://github.com/Agumuzi/crhopper/issues)

[English](./README.md) · [简体中文](./README.zh-CN.md) · [Русский](./README.ru.md) · [فارسی](./README.fa.md)

</div>

---

## Quick start

<table width="100%">
<thead>
<tr>
<th align="left" width="43%">Client</th>
<th align="left" width="17%">Format</th>
<th align="left" width="40%">Remote subscription</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Hiddify</strong> and URI-compatible clients</td>
<td>TXT / URI</td>
<td><a href="https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt">CR-Hopper.txt</a></td>
</tr>
<tr>
<td><strong>Mihomo</strong> and Clash-compatible clients</td>
<td>YAML</td>
<td><a href="https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml">CR-Hopper.yaml</a></td>
</tr>
</tbody>
</table>

Add one of the raw URLs as a **remote subscription/profile** in your client. The [website](https://agumuzi.github.io/crhopper/#feeds) offers one-click copying and a short guide.

### Permanent feed URLs

~~~text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml
~~~

These URLs and filenames are intentionally preserved for existing subscribers.

## How it works

CR-Hopper collects proxy candidates from sources already public on the Internet, screens and prepares a changing selection, then republishes it in client-ready formats.

~~~text
PUBLIC SOURCES → COLLECT → FILTER → PREPARE → PUBLISH
                                           ├─ URI / TXT → Hiddify
                                           └─ YAML      → Mihomo / Clash
~~~

The repository **does not create, host or operate proxy servers**. All upstream nodes belong to independent third parties. The publicly published set can include VLESS, Hysteria2 and Shadowsocks, depending on available candidates and filtering outcomes. The TXT and YAML feeds represent the same selected set in different formats.

## Compatibility

- **Hiddify:** use the TXT/URI subscription.
- **Mihomo and Clash-compatible clients:** use the YAML subscription.
- Other compatible clients can use the format they support.

**When connections stop working:** try refreshing your subscription. Public nodes are ephemeral and may disappear without notice. Node speed, location and uptime are not guaranteed; a client-reported location may differ from a node label or actual egress.

## Privacy and security

Public third-party nodes are not inherently trusted. Their operators may observe traffic metadata, and CR-Hopper does not guarantee confidentiality, integrity, endpoint ownership, privacy or security. Prefer end-to-end encrypted connections and avoid sending sensitive data through untrusted intermediaries.

## Maintainer-only Google Drive sync

**CR-Hopper Sync** is the project's maintainer-operated Google Drive archive integration. A separate local scanner uses `rclone` to back up project files and operational evidence to the maintainer's own Drive. This is **not** a Google login feature for public subscribers; subscribing to TXT or YAML never requires Google authorization. The published feed URLs are unchanged.

[CR-Hopper Sync privacy policy](https://agumuzi.github.io/crhopper/privacy.html) describes data access, storage, retention, and revocation. OAuth client credentials and private scanner files are not part of this public repository.

## Contributing and security

- [Contributing](CONTRIBUTING.md) — website, subscription-format, translation and compatibility feedback.
- [Security policy](SECURITY.md) — report project vulnerabilities privately where supported. Do not post private nodes, tokens or personal logs in public issues.
- **License status:** No repository-wide open-source license has been granted for this project. The public third-party proxy entries do not become the maintainer's intellectual property merely by being republished.

## Website and branding

The [CR-Hopper website](https://agumuzi.github.io/crhopper/) is a static, four-language project guide with copyable feed URLs. It lives in [docs/](./docs/), separate from the subscription files and publication workflow. The repository remains named **crhopper** to preserve existing remote URLs; the public-facing project name is **CR-Hopper**.

## Community

- [Contributing](CONTRIBUTING.md) — report public-site or format issues and propose improvements.
- [Code of Conduct](CODE_OF_CONDUCT.md) — participation and moderation guidelines.
- [Security policy](SECURITY.md) — report security issues without sharing secrets publicly.

## Disclaimer

CR-Hopper is provided for testing, research and personal network use only.

Users are solely responsible for ensuring that their use of this repository, its subscription feeds and any third-party proxy nodes complies with all laws, regulations, contractual obligations and service terms applicable in their country or jurisdiction. **Do not use CR-Hopper in any manner that is prohibited by local law or regulation.**

The repository maintainers do not operate, control or guarantee the third-party proxy nodes contained in the public feeds. Node availability, speed, security, privacy, reliability, geographic routing and continued operation are not guaranteed.

The project is provided **"as is"** and **"as available"**, without warranties of any kind. Users assume all risks arising from their use of the project and are responsible for their own network activity, data, accounts, devices and compliance obligations.

To the fullest extent permitted by applicable law, the developers and maintainers shall not be responsible or liable for misuse of the project, unlawful activity by users, service interruptions, account restrictions, data loss or exposure, security incidents, financial loss, legal consequences, or any other direct or indirect damages arising from the use of, or inability to use, CR-Hopper.

---

<sub>Maintained by [Agumuzi](https://github.com/Agumuzi). All upstream nodes are third-party resources. No uptime, privacy or security guarantees.</sub>

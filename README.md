<div align="center">

<img src="docs/assets/rocket.svg" width="104" height="104" alt="CR-Hopper pixel rocket logo">

# CR-Hopper

**Public proxy subscriptions · Frequently refreshed · Easy to use**

Free curated proxy feeds for Hiddify, Mihomo and Clash-compatible clients.

[🌐 Website & visual guide](https://agumuzi.github.io/crhopper/) · [☕ Support](https://ko-fi.com/agumuzi) · [Report an issue](https://github.com/Agumuzi/crhopper/issues)

**English** · [简体中文](./README.zh-CN.md) · [Русский](./README.ru.md) · [فارسی](./README.fa.md)

</div>

---

## 📋 Subscription URLs

**Copy the entire URL from the box that matches your client.** Each code block has a copy button on GitHub. Add the URL as a **remote subscription**, not as a local file.

### Hiddify · TXT / URI

For **Hiddify** and other URI-compatible clients.

```text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt
```

### Clash Mi / Mihomo · YAML

For **Clash Mi**, **Mihomo** and other Clash-compatible clients.

```text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml
```

> Both subscriptions contain the same selected public nodes in different formats. The feed URLs are permanent and remain unchanged for existing subscribers.

## 🚀 How to connect

### Option 1 — Hiddify (TXT / URI)

1. **Install Hiddify:** [Download for iOS, Android, macOS, Windows or Linux](https://github.com/hiddify/hiddify-app/releases).
2. **Copy** the TXT / URI URL from the first box above.
3. **Import:** Open Hiddify → **Home → + → Clipboard**. If needed, choose **Manually** and paste the URL.
4. **Connect:** Select the imported profile and start the connection. Refresh the subscription when nodes stop working.

[Official installation guide](https://hiddify.com/app/How-to-install-Hiddify-app/) · [Official usage guide](https://hiddify.com/app/How-to-use-Hiddify-app/)

### Option 2 — Clash Mi (YAML)

1. **Install Clash Mi:** [Official downloads](https://clashmi.app/download) · [GitHub releases](https://github.com/KaringX/clashmi/releases).
2. **Copy** the YAML URL from the second box above.
3. **Import:** Open Clash Mi → **My Configurations → + → Add configuration link** → paste the URL and save.
4. **Connect:** Return to **Home** and enable the connection. Refresh the subscription when nodes stop working.

[Official usage guide](https://clashmi.app/guide/)

> **Prefer screenshots?** The [visual setup guide](https://agumuzi.github.io/crhopper/#setup) shows the full steps. You do **not** need a CR-Hopper account, API key or Google authorization to subscribe. CR-Hopper does not distribute client installers.

---

## How it works

CR-Hopper collects proxy candidates from **publicly available third-party sources**, screens them, and publishes a changing selection in two client-ready formats.

<div align="center">

**PUBLIC SOURCES → COLLECT → FILTER → PUBLISH**

**↳ TXT / URI for Hiddify · ↳ YAML for Mihomo / Clash**

</div>

The feeds represent the **same selected set**, packaged in different formats. Depending on available candidates, the selection may include VLESS, Hysteria2 and Shadowsocks.

**CR-Hopper does not create, host, own, or operate proxy servers.** All upstream nodes are independent third-party resources.

## Compatibility, privacy & reliability

- **Choose the right format.** Hiddify and URI-compatible clients use TXT / URI; Mihomo and Clash-compatible clients use YAML. Other clients may work if they support one of these formats.
- **Refresh when connections fail.** Public nodes may disappear or change without warning. Speed, availability, routing and uptime are not guaranteed; client-reported locations can differ from node labels or actual egress.
- **Treat public nodes as untrusted.** Operators may observe traffic metadata. CR-Hopper cannot guarantee confidentiality, integrity, endpoint ownership, privacy or security. Prefer end-to-end encryption and avoid sending sensitive information through untrusted intermediaries.

## Project resources

| | |
| :--- | :--- |
| 🌐 **Project website** | [Four-language quick start and copyable feed URLs](https://agumuzi.github.io/crhopper/) |
| 🛠️ **Contributing** | [Report website, format, translation or compatibility issues](CONTRIBUTING.md) |
| 🛡️ **Security** | [Report vulnerabilities privately where supported](SECURITY.md) |
| 🤝 **Community** | [Code of Conduct](CODE_OF_CONDUCT.md) · [GitHub Issues](https://github.com/Agumuzi/crhopper/issues) |
| ☕ **Support** | [Support development on Ko-fi](https://ko-fi.com/agumuzi) |

Please **do not** post private nodes, tokens, account data, or personal logs in public issues.

### License & branding

- **Project-maintained source code:** [PolyForm Noncommercial 1.0.0](LICENSE). Qualifying noncommercial use and modification are permitted; commercial use requires separate permission. This is **source-available, not OSI open source**.
- **Original artwork and branding:** The rocket icon, Agumuzi marks and other original visuals are separately reserved under [Brand & Visual Assets](ASSETS-LICENSE.md); reuse requires permission.
- **Third-party feeds:** Public node addresses and upstream data do not belong to CR-Hopper and are not covered by the project's PolyForm license merely because they appear in the feeds.

<details>
<summary><strong>Maintainer notes — website & Google Drive sync</strong></summary>

The [project website](https://agumuzi.github.io/crhopper/) is a static four-language guide maintained in [docs/](./docs/), separate from the subscription files and publication workflow. The repository remains named **crhopper** to preserve existing remote URLs; the public project name is **CR-Hopper**.

**CR-Hopper Sync** is a maintainer-only Google Drive archive integration. A separate local scanner uses rclone to back up project files and operational evidence to the maintainer's own Drive. It is **not** a public subscriber login feature: using the TXT or YAML feeds never requires Google authorization, and the published URLs are unchanged.

See the [CR-Hopper Sync privacy policy](https://agumuzi.github.io/crhopper/privacy.html) for data access, storage, retention and revocation. OAuth client credentials and private scanner files are not part of this public repository.

</details>

## Disclaimer

**For testing, research and personal network use only.** Use CR-Hopper in accordance with the laws, regulations, contracts and service terms applicable to you. Third-party public nodes have **no guaranteed availability, privacy or security**.

<details>
<summary><strong>Read the full disclaimer</strong></summary>

CR-Hopper is provided for testing, research and personal network use only.

Users are solely responsible for ensuring that their use of this repository, its subscription feeds and any third-party proxy nodes complies with all laws, regulations, contractual obligations and service terms applicable in their country or jurisdiction. **Do not use CR-Hopper in any manner that is prohibited by local law or regulation.**

The repository maintainers do not operate, control or guarantee the third-party proxy nodes contained in the public feeds. Node availability, speed, security, privacy, reliability, geographic routing and continued operation are not guaranteed.

The project is provided **"as is"** and **"as available"**, without warranties of any kind. Users assume all risks arising from their use of the project and are responsible for their own network activity, data, accounts, devices and compliance obligations.

To the fullest extent permitted by applicable law, the developers and maintainers shall not be responsible or liable for misuse of the project, unlawful activity by users, service interruptions, account restrictions, data loss or exposure, security incidents, financial loss, legal consequences, or any other direct or indirect damages arising from the use of, or inability to use, CR-Hopper.

</details>

---

<div align="center">
<sub>Maintained by <a href="https://github.com/Agumuzi">Agumuzi</a> · All upstream nodes are third-party resources · No uptime, privacy or security guarantees</sub>
</div>

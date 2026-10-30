<div align="center">

<img src="docs/assets/rocket.svg" width="104" height="104" alt="CR-Hopper pixel rocket logo">

# CR-Hopper

**Public proxy feeds. Frequently refreshed. Easy to use.**

Curated subscriptions for **Hiddify**, **Mihomo**, and **Clash-compatible clients**.

<p>
  <a href="https://agumuzi.github.io/crhopper/"><img src="https://img.shields.io/badge/QUICK_START-Visit_Website-149DDD?style=for-the-badge" alt="Open the quick start website"></a>
  <a href="https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt"><img src="https://img.shields.io/badge/TXT_URI-Get_Feed-F27676?style=for-the-badge" alt="Get the TXT subscription"></a>
  <a href="https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml"><img src="https://img.shields.io/badge/YAML-Get_Feed-28A98B?style=for-the-badge" alt="Get the YAML subscription"></a>
</p>

[Website](https://agumuzi.github.io/crhopper/) · [How it works](#how-it-works) · [Support development ☕](https://ko-fi.com/agumuzi) · [Report an issue](https://github.com/Agumuzi/crhopper/issues)

**English** · [简体中文](./README.zh-CN.md) · [Русский](./README.ru.md) · [فارسی](./README.fa.md)

</div>

---

## ⚡ Quick start

**No account, API key, or Google authorization required.** Choose a compatible client, import a feed as a **remote subscription**, and connect.

| Your client | Subscription format | Get the client |
| :--- | :--- | :--- |
| **Hiddify** and URI-compatible apps | **[TXT / URI feed](https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt)** | [Hiddify releases](https://github.com/hiddify/hiddify-app/releases) |
| **Clash Mi**, Mihomo and Clash-compatible apps | **[YAML feed](https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml)** | [Clash Mi downloads](https://clashmi.app/download) |

1. **Install** the client for your device.
2. **Copy** the appropriate subscription URL from the table above or the [project website](https://agumuzi.github.io/crhopper/#feeds).
3. **Import** it as a remote profile/configuration, then enable the connection.

> **New here?** The [illustrated quick-start guide](https://agumuzi.github.io/crhopper/#setup) walks through the setup step by step.

<details>
<summary><strong>Hiddify — import the TXT / URI subscription</strong></summary>

1. Download [Hiddify](https://github.com/hiddify/hiddify-app/releases).
2. Open **Home → + → Clipboard** (or **Manually**).
3. Import the [TXT subscription](https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt), then connect.

Official references: [Installation guide](https://hiddify.com/app/How-to-install-Hiddify-app/) · [Usage guide](https://hiddify.com/app/How-to-use-Hiddify-app/).

</details>

<details>
<summary><strong>Clash Mi — import the YAML subscription</strong></summary>

1. Download [Clash Mi](https://clashmi.app/download) ([GitHub releases](https://github.com/KaringX/clashmi/releases)).
2. Open **My Configurations → + → Add configuration link**.
3. Paste the [YAML subscription URL](https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml), return to **Home**, and enable the connection.

Official reference: [Clash Mi usage guide](https://clashmi.app/guide/).

</details>

<details>
<summary><strong>Show permanent subscription URLs</strong></summary>

**TXT / URI — Hiddify and compatible clients**

~~~text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt
~~~

**YAML — Mihomo / Clash-compatible clients**

~~~text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml
~~~

These URLs and filenames are kept unchanged for existing subscribers.

</details>

Both recommended clients support iOS, Android, macOS, Windows and Linux. Download installers directly from their developers; CR-Hopper does not distribute client applications.

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

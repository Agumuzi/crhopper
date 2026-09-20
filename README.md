<div align="center">

# 🚀 CR-Hopper

**Curated public proxy subscription feeds for Hiddify, Mihomo and Clash-compatible clients.**

[English](./README.md) · [简体中文](./README.zh-CN.md) · [Русский](./README.ru.md) · [فارسی](./README.fa.md)

</div>

---

## Subscription links

### Hiddify / URI subscription

Copy the link below and add it as a remote profile in Hiddify or another URI-subscription client.

```text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.txt
```

### Mihomo / Clash YAML

Copy the link below and use it as a remote YAML profile in Mihomo / Clash-compatible clients.

```text
https://raw.githubusercontent.com/Agumuzi/crhopper/main/CR-Hopper.yaml
```

## What is CR-Hopper?

CR-Hopper publishes a compact set of proxy nodes that have already passed upstream qualification and runtime preparation before publication.

The public feed may contain multiple protocols, including VLESS, Hysteria2 and Shadowsocks. The exact node count and protocol mix can change between updates.

## Recommended clients

- **Hiddify:** use `CR-Hopper.txt`
- **Mihomo / Clash-compatible clients:** use `CR-Hopper.yaml`

## Notes

- Public proxy nodes can become unavailable at any time. Refresh the subscription when connectivity changes.
- Geo information shown by a client is determined by the client and may differ from the node label.
- The TXT and YAML feeds represent the same published candidate set in different formats.

## Disclaimer

This repository provides public proxy subscription data for testing and personal network use. Availability, speed and geographic routing are not guaranteed.

# crhopper

**Qualified Top 100 Servers**

A public proxy subscription feed generated from a continuously maintained pool of qualified servers.

## Subscription formats

This repository is intended to publish two synchronized subscription formats:

- `mihomo.yaml` — for Mihomo / Clash Mi and other Clash-compatible clients.
- `subscription.txt` — URI subscription feed for Hiddify and other compatible clients.

Both files are generated from the same qualified server pool and are intended to represent the same set of published nodes.

## Update model

Planned publishing cadence:

- refresh the qualified server pool using the existing screening system;
- after each successful foreground refresh, render the current pool into YAML and URI subscription formats;
- publish the latest snapshot to this repository;
- target cadence: approximately every **2 hours**.

The publishing layer does **not** perform additional node testing, ranking, or filtering. It only converts the already-qualified current pool into standard subscription formats.

## Current status

**Initial setup / testing**

The repository has been created and the publishing workflow is being prepared. Subscription files may not be available until the first test snapshot is published.

## Notes

- The published feed contains connection information only.
- Internal screening history, detailed test records, source attribution, and qualification evidence are not published.
- Individual proxy servers can become unavailable at any time.
- This project is intended primarily as a convenient personal and shared subscription source across phones, computers, and compatible routers.

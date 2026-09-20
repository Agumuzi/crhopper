# 🚀CR-Hopper

A lightweight public proxy feed published from an already-qualified runtime candidate set.

## Public files

- `🚀CR-Hopper.yaml` — Mihomo / Clash-compatible configuration.
- `🚀CR-Hopper.txt` — URI subscription for Hiddify and other compatible clients.

Both public files represent the same current candidate set. The published node count is whatever the upstream qualified runtime file contains at that refresh; no fixed count is imposed here.

## Publishing model

The publisher does not perform additional screening, ranking, Geo lookup, speed testing, or node-quality decisions.

It only:

1. reads the latest already-qualified runtime configuration;
2. removes private/internal-only metadata from the public copy;
3. publishes the YAML form;
4. converts the same proxy definitions into URI subscription form;
5. updates the two public files.

## Privacy boundary

Public outputs must not expose internal device names, internal project codenames, private filesystem paths, personal identifiers, or user-specific operational comments.

Node connection credentials are necessarily present in a public proxy feed and should be treated as public once published.

## Status

Testing / integration in progress.

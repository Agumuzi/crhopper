#!/usr/bin/env python3
"""Validate public CR-Hopper pages without fetching proxies or requiring network access."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PAGES = (DOCS / "index.html", DOCS / "privacy.html")
LANGUAGES = ("en", "zh", "ru", "fa")
PUBLIC_FEEDS = (
    ("CR-Hopper.txt", "txt"),
    ("CR-Hopper.yaml", "yaml"),
)


class PageRefs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.identifiers = set()
        self.languages = set()
        self.translation_keys = set()
        self.has_viewport = False
        self.has_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.identifiers.add(values["id"])
        if values.get("data-language"):
            self.languages.add(values["data-language"])
        if values.get("data-i18n"):
            self.translation_keys.add(values["data-i18n"])
        if tag == "meta" and values.get("name") == "viewport":
            self.has_viewport = True
        if tag == "title":
            self.has_title = True
        if tag in {"a", "link", "script", "img", "source"}:
            ref = values.get("href") if tag in {"a", "link"} else values.get("src")
            if ref:
                self.references.append(ref)


def main():
    failures = []
    parsed = {}
    javascript = (DOCS / "assets/app.js").read_text(encoding="utf-8")
    for filename, _format in PUBLIC_FEEDS:
        if not (ROOT / filename).is_file():
            failures.append(f"Missing public feed: {filename}")
        public_url = f"https://raw.githubusercontent.com/Agumuzi/crhopper/main/{filename}"
        if public_url not in javascript:
            failures.append(f"Public feed URL changed in website code: {filename}")

    for page in PAGES:
        if not page.is_file():
            failures.append(f"Missing website page: {page.relative_to(ROOT)}")
            continue
        parser = PageRefs()
        parser.feed(page.read_text(encoding="utf-8"))
        parsed[page.resolve()] = parser
        if not parser.has_viewport or not parser.has_title:
            failures.append(f"{page.relative_to(ROOT)} missing title or viewport")
        missing_languages = set(LANGUAGES) - parser.languages
        if missing_languages:
            failures.append(f"{page.relative_to(ROOT)} language options missing: {sorted(missing_languages)}")
        for key in parser.translation_keys:
            if f"{key}:" not in javascript:
                failures.append(f"{page.relative_to(ROOT)} translation key missing in JS: {key}")

    for page in PAGES:
        parser = parsed.get(page.resolve())
        if parser is None:
            continue
        for ref in parser.references:
            split = urlsplit(ref)
            if split.scheme or split.netloc or ref.startswith("//") or split.path.startswith("/"):
                continue
            if not split.path and not split.fragment:
                continue
            target = (page.parent / unquote(split.path)).resolve() if split.path else page.resolve()
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                failures.append(f"{page.relative_to(ROOT)}: broken local link {ref}")
                continue
            if split.fragment and target in parsed and split.fragment not in parsed[target].identifiers:
                failures.append(f"{page.relative_to(ROOT)}: missing anchor {ref}")

    if failures:
        for failure in failures:
            print("FAIL:", failure)
        raise SystemExit(1)
    print("PASS: public links, static resources, four languages, and feed URL invariants")


if __name__ == "__main__":
    main()

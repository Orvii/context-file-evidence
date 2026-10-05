#!/usr/bin/env python3
"""Report arXiv version drift for the pinned primary sources.

The numbers in this repo are transcriptions of specific paper versions.
When arXiv publishes a new version, the transcription may be stale — this
script says which pins moved. Mechanical only: it reads the arXiv API and
compares version suffixes; it never re-reads the papers and never changes
a pin. Refreshing a pin is a research task (see CONTRIBUTING), not a script.

Usage: python3 scripts/version-drift.py   (read-only network calls)
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

API = "https://export.arxiv.org/api/query?id_list={}"


def latest_version(arxiv_id: str):
    """Return (version_int, updated_date) from the arXiv Atom feed, or None."""
    try:
        with urllib.request.urlopen(API.format(arxiv_id), timeout=30) as r:
            xml = r.read().decode("utf-8", "replace")
    except Exception as exc:  # network blip is not drift
        print(f"?  {arxiv_id}: fetch failed ({exc.__class__.__name__})")
        return None
    m = re.search(r"<id>https?://arxiv\.org/abs/" + re.escape(arxiv_id) + r"v(\d+)</id>", xml)
    if not m:
        print(f"?  {arxiv_id}: no versioned <id> in feed")
        return None
    u = re.search(r"<updated>([^<]+)</updated>", xml)
    return int(m.group(1)), (u.group(1)[:10] if u else "unknown")


def main() -> int:
    pins = json.loads((Path(__file__).parent / "pins.json").read_text())["pins"]
    drifted = 0
    for pin in pins:
        got = latest_version(pin["arxiv_id"])
        if got is None:
            continue
        version, updated = got
        if version != pin["version"]:
            drifted += 1
            print(f"Δ  {pin['arxiv_id']}: pinned v{pin['version']} → arXiv v{version} "
                  f"(updated {updated}) — {pin['study']} may be stale")
        else:
            print(f"=  {pin['arxiv_id']}: v{version} (updated {updated})")
    print(f"\n{drifted} drifted pin(s). A drift is a research task: re-extract the new "
          f"version, diff the numbers, update research/ + studies/ + matrix.md, bump the pin.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Decision log: append judgements, list due reviews, compute calibration.

  add     --claim ... --conf 0.7 --falsifier ... --review-on 2027-02-11
  due
  resolve --id 2026-11-11-01 --outcome true|false|partial
  score
  list
"""

import argparse
import json
import os
import sys
from datetime import date, datetime
from pathlib import Path

DEFAULT = Path("~/.codebuddy/knowledge/cognitive-lead/decisions.jsonl").expanduser()


def path(arg):
    return Path(os.path.expanduser(arg)) if arg else DEFAULT


def load(p: Path):
    if not p.is_file():
        return []
    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def append(p: Path, row: dict):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def next_id(rows):
    today = date.today().isoformat()
    n = sum(1 for r in rows if str(r.get("id", "")).startswith(today)) + 1
    return f"{today}-{n:02d}"


def cmd_add(a):
    p = path(a.file)
    rows = load(p)
    if not a.falsifier.strip():
        print("error: falsifier is required - a judgement without a counter-example cannot be logged",
              file=sys.stderr)
        return 2
    row = {
        "id": next_id(rows),
        "ts": datetime.now().astimezone().isoformat(timespec="seconds"),
        "claim": a.claim.strip(),
        "confidence": round(float(a.conf), 3),
        "falsifier": a.falsifier.strip(),
        "review_on": a.review_on or "",
        "outcome": None,
        "note": a.note or "",
        "rule_version": a.rule_version or "v2.0",
    }
    append(p, row)
    print(json.dumps(row, ensure_ascii=False, indent=2))
    return 0


def cmd_due(a):
    p = path(a.file)
    today = date.today()
    due = []
    for r in load(p):
        if r.get("outcome") is not None or not r.get("review_on"):
            continue
        try:
            d = date.fromisoformat(r["review_on"])
        except ValueError:
            continue
        if d <= today:
            due.append(r)
    if not due:
        print("nothing due.")
        return 0
    for r in due:
        print(f'{r["id"]}  conf={r["confidence"]:.2f}  due={r["review_on"]}  {r["claim"]}')
        print(f'    falsifier: {r["falsifier"]}')
    return 0


def cmd_resolve(a):
    p = path(a.file)
    rows = load(p)
    hit = None
    for r in rows:
        if r["id"] == a.id:
            hit = r
            break
    if not hit:
        print(f"error: id not found: {a.id}", file=sys.stderr)
        return 2
    if hit.get("outcome") is not None and not a.force:
        print("error: already resolved (pass --force to overwrite)", file=sys.stderr)
        return 2
    hit["outcome"] = {"true": True, "false": False, "partial": 0.5}[a.outcome]
    hit["resolved_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
    if a.note:
        hit["note"] = (hit.get("note", "") + " | " + a.note).strip(" |")
    p.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
                 encoding="utf-8")
    print(json.dumps(hit, ensure_ascii=False, indent=2))
    return 0


def cmd_score(a):
    p = path(a.file)
    rows = [r for r in load(p) if r.get("outcome") is not None]
    if not rows:
        print("no resolved judgements yet.")
        return 0
    errs = [(r["confidence"] - (1.0 if r["outcome"] is True else float(r["outcome"]))) ** 2
            for r in rows]
    brier = sum(errs) / len(errs)
    buckets = {}
    for r, e in zip(rows, errs):
        b = int(float(r["confidence"]) * 10) / 10
        buckets.setdefault(f"{b:.1f}", []).append(e)
    print(f"resolved: {len(rows)}   brier: {brier:.3f}")
    print("  <0.25 usable | 0.25-0.40 biased | >0.40 untrustworthy")
    for k in sorted(buckets):
        print(f"  conf {k}: n={len(buckets[k])}  brier={sum(buckets[k])/len(buckets[k]):.3f}")
    return 0


def cmd_list(a):
    rows = load(path(a.file))
    for r in rows[-a.n:]:
        oc = {None: "-", True: "Y", False: "N", 0.5: "~"}.get(r.get("outcome"), "?")
        print(f'{r["id"]}  {oc}  {r["confidence"]:.2f}  {r["claim"][:60]}')
    return 0


def main():
    ap = argparse.ArgumentParser(description="decision log / calibration")
    ap.add_argument("--file", help="decisions.jsonl path")
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add"); a.set_defaults(func=cmd_add)
    a.add_argument("--claim", required=True)
    a.add_argument("--conf", required=True, type=float)
    a.add_argument("--falsifier", required=True)
    a.add_argument("--review-on", dest="review_on")
    a.add_argument("--note")
    a.add_argument("--rule-version", dest="rule_version")

    d = sub.add_parser("due"); d.set_defaults(func=cmd_due)

    r = sub.add_parser("resolve"); r.set_defaults(func=cmd_resolve)
    r.add_argument("--id", required=True)
    r.add_argument("--outcome", required=True, choices=["true", "false", "partial"])
    r.add_argument("--note")
    r.add_argument("--force", action="store_true")

    s = sub.add_parser("score"); s.set_defaults(func=cmd_score)
    l = sub.add_parser("list"); l.set_defaults(func=cmd_list)
    l.add_argument("-n", type=int, default=20)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

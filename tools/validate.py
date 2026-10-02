#!/usr/bin/env python3
"""Validasi semua konten di content/build/<jenis>/*.json terhadap content/schema/<jenis>.schema.json.

Aturan bisnis tambahan per jenis konten ditambahkan di fungsi BUSINESS_RULES.
Exit code 1 jika ada yang gagal.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Callable

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    sys.exit("jsonschema belum terpasang: pip install -r tools/requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "content" / "schema"
BUILD_DIR = ROOT / "content" / "build"


def rule_unique_level_ids(data: dict) -> list[str]:
    ids = [lvl.get("id") for lvl in data.get("levels", [])]
    dup = {i for i in ids if ids.count(i) > 1}
    return [f"id level duplikat: {sorted(dup)}"] if dup else []


# Tambahkan aturan per jenis konten di sini: {"tts": [rule_a, rule_b]}
BUSINESS_RULES: dict[str, list[Callable[[dict], list[str]]]] = {
    "*": [rule_unique_level_ids],
}


def main() -> int:
    if not BUILD_DIR.exists():
        print("content/build tidak ada, tidak ada yang divalidasi.")
        return 0

    errors: list[str] = []
    checked = 0
    for kind_dir in sorted(p for p in BUILD_DIR.iterdir() if p.is_dir()):
        kind = kind_dir.name
        schema_path = SCHEMA_DIR / f"{kind}.schema.json"
        if not schema_path.exists():
            errors.append(f"[{kind}] skema tidak ditemukan: {schema_path.relative_to(ROOT)}")
            continue
        validator = Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8")))
        rules = BUSINESS_RULES.get("*", []) + BUSINESS_RULES.get(kind, [])

        for file in sorted(kind_dir.glob("*.json")):
            checked += 1
            rel = file.relative_to(ROOT)
            try:
                data = json.loads(file.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: JSON tidak valid ({exc})")
                continue
            for err in validator.iter_errors(data):
                path = "/".join(str(p) for p in err.absolute_path) or "(root)"
                errors.append(f"{rel} @ {path}: {err.message}")
            for rule in rules:
                errors.extend(f"{rel}: {msg}" for msg in rule(data))

    for e in errors:
        print(f"GAGAL  {e}")
    print(f"\n{checked} file dicek, {len(errors)} masalah.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Salin content/build/ ke folder konten engine (dest di tools/sync_config.json).

Folder tujuan dikosongkan dulu agar file yang sudah dihapus di build ikut hilang.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "build"
CONFIG = Path(__file__).resolve().parent / "sync_config.json"


def main() -> int:
    dest_rel = json.loads(CONFIG.read_text(encoding="utf-8")).get("dest", "").strip()
    if not dest_rel:
        print("tools/sync_config.json: 'dest' belum diisi. Jalankan /choose-stack dulu.")
        return 1
    dest = (ROOT / dest_rel).resolve()
    if ROOT not in dest.parents:
        print(f"dest harus di dalam repo: {dest}")
        return 1

    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SRC, dest, ignore=shutil.ignore_patterns(".gitkeep"))
    count = sum(1 for _ in dest.rglob("*.json"))
    print(f"{count} file JSON disalin ke {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

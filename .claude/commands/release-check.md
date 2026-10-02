---
description: Audit kesiapan rilis game ke store
---

Target rilis: $ARGUMENTS (misalnya "android closed testing", "android produksi", "ios")

1. Baca `context/release-checklist.md` dan bagian Build & Rilis di `context/stack.md`.
2. Audit setiap item checklist terhadap kondisi project sebenarnya (cek file, config, kode). Jangan menandai item hanya berdasarkan asumsi.
3. Khusus wajib dicek: ad unit ID produksi hanya di build release, consent iklan berjalan, versi/build number naik, signing tidak ter-commit, semua asset punya lisensi di assets.md, tidak ada log debug/cheat aktif.
4. Kebijakan store berubah: untuk item yang menyangkut aturan Google Play / App Store, sarankan user memverifikasi di konsol resmi.
5. Laporkan: item lulus, item gagal (dengan lokasi file), item yang perlu dicek manual oleh user.

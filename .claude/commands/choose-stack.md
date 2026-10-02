---
description: Pilih stack/engine dari folder stacks/ lalu aktifkan sebagai context/stack.md
---

Stack yang diminta: $ARGUMENTS (id file di `stacks/`, misalnya `flutter`, `godot`, `unity`, `phaser-capacitor`)

Workflow:

1. Baca `stacks/README.md` (matriks pemilihan) dan `context/game-design.md` jika sudah terisi.
2. Jika `$ARGUMENTS` kosong: rekomendasikan maksimal 2 stack yang paling cocok dengan genre dan batasan game, beserta trade-off singkat. Tunggu user memilih.
3. Jika stack yang dipilih kurang cocok dengan game (misalnya game fisika berat di Flutter tanpa Flame), katakan SEBELUM melanjutkan.
4. Jika `context/stack.md` **sudah berisi stack lain** dan sudah ada kode:
   - BERHENTI. Jelaskan dampak migrasi: apa yang bisa dibawa (folder `content/`, `tools/`, `assets-src/`, dokumen context, logika core sebagai spesifikasi + test case) dan apa yang harus ditulis ulang (presentation, services, build config).
   - Lanjut hanya dengan konfirmasi eksplisit. Catat keputusan di progress-tracker bagian *Decisions*.
5. Salin isi `stacks/<id>.md` ke `context/stack.md` (salin, bukan symlink, karena file ini akan disesuaikan per project). Isi baris `Diaktifkan:` dengan tanggal hari ini.
6. Cek versi stabil terbaru engine/framework dan plugin utama dari dokumentasi resmi. Tulis versi yang akan dipakai di tabel Stack pada `context/stack.md`. Jangan mengandalkan ingatan.
7. Update bagian "Pemetaan ke Stack Aktif" di `context/architecture.md` sesuai bagian Mapping di stack.md.
8. Tambahkan entry `.gitignore` khusus engine dari stack.md ke `.gitignore` root.
9. Isi `dest` di `tools/sync_config.json` dengan folder konten engine sesuai bagian Konten di stack.md.
10. Update `context/progress-tracker.md` baris **Stack:** dan catat keputusan di *Decisions*.
11. Laporkan ringkas: stack aktif, versi, dan langkah berikutnya (`/new-feature 01`).

Jangan meng-install apapun atau membuat project engine di workflow ini. Itu tugas feature 01.

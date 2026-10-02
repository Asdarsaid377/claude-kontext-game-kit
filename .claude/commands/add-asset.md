---
description: Masukkan asset baru (gambar, audio, font, animasi) sesuai aturan penamaan dan lisensi
---

Asset yang ditambahkan: $ARGUMENTS

Workflow:

1. Baca `context/assets.md`.
2. Pastikan sumber dan lisensi asset jelas. Jika tidak jelas atau lisensinya melarang penggunaan komersial: BERHENTI dan beri tahu user.
3. File sumber (PSD, Aseprite, Figma export besar, WAV master) disimpan di `assets-src/`. File siap pakai masuk ke folder asset engine sesuai `context/stack.md`.
4. Ganti nama sesuai konvensi penamaan di assets.md. Cek ukuran dan format sesuai batas di assets.md (kompres jika melebihi).
5. Tambahkan entry di tabel registry `assets.md` (path, sumber, lisensi, atribusi jika wajib).
6. Jika lisensi mewajibkan atribusi: pastikan tercantum di layar Kredit / file credits.
7. Laporkan ringkas apa yang ditambahkan.

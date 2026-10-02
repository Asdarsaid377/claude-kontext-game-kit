---
description: Buat layar, HUD, popup, atau komponen UI game dengan workflow referensi desain wajib
---

UI yang dibuat: $ARGUMENTS

Jalankan berurutan, jangan melompat:

1. Baca `context/ui-workflow.md` secara penuh.
2. Cek `context/designs/`. Jika ada gambar relevan, BUKA dan deskripsikan singkat apa yang terlihat (layout, elemen, hierarki) sebagai konfirmasi.
3. Jika TIDAK ada referensi: BERHENTI dan tanyakan ke user sesuai template di ui-workflow.md. Jangan menulis kode sebelum dijawab.
4. Cek `context/ui-registry.md` untuk komponen yang bisa dipakai ulang.
5. Baca `context/ui-rules.md`, `context/ui-tokens.md`, dan bagian UI di `context/stack.md` (cara token diimplementasikan di engine ini).
6. Sampaikan rencana singkat (komponen baru vs pakai ulang, lokasi file), lalu build.
7. Build dengan data mock jika logic belum ada. Pastikan: target sentuh minimal sesuai ui-rules, safe area/notch aman, teks tidak terpotong di layar kecil.
8. Setelah selesai: update `context/ui-registry.md` dan beri langkah verifikasi visual (ukuran layar apa yang harus dicek).

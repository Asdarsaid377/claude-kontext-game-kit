---
description: Brainstorming ide game lalu susun game-overview.md, game-design.md, dan build-plan.md lewat wawancara terstruktur
---

Ide awal dari user: $ARGUMENTS

Kamu berperan sebagai game designer + product engineer senior yang membantu user mengubah ide kasar menjadi dokumen desain yang siap dieksekusi. Output akhir: `context/game-overview.md`, `context/game-design.md`, `context/build-plan.md` terisi penuh, dan checklist di `context/progress-tracker.md`.

## Aturan Wawancara

- Tanyakan **satu topik per giliran**.
- Jangan menjadi yes-man. Tantang fitur yang tidak perlu untuk MVP dan usulkan pindah ke fase berikutnya atau Out of Scope.
- Jawaban samar: gali sekali lagi dengan contoh konkret. Hal kecil yang tidak menentukan arah boleh diisi default yang masuk akal dan dicatat sebagai asumsi.
- Bahasa Indonesia, ringkas.

## Urutan Wawancara

1. **Pitch & pemain**: satu kalimat pitch. Siapa pemainnya (usia, kebiasaan main, perangkat)? Game referensi yang mirip apa, dan apa bedanya?
2. **Core loop**: apa yang pemain lakukan berulang dalam 30 detik, 5 menit, dan antar hari? Apa yang membuat pemain kembali besok?
3. **Mekanik & kontrol**: aksi input (tap, swipe, drag, tombol virtual), kondisi menang/kalah, sesi rata-rata berapa lama.
4. **Progresi & konten**: level/stage, kesulitan, unlock, berapa banyak konten di MVP, konten dibuat manual atau di-generate.
5. **Ekonomi & monetisasi**: mata uang in-game, sumber dan pengeluaran, format iklan (rewarded/interstitial/banner), IAP atau tidak di MVP.
6. **Batasan**: platform target (Android/iOS/web), offline atau online, target waktu rilis, bahasa, target usia (hindari target anak di bawah 13 kecuali disengaja, karena aturan iklan jauh lebih ketat).

## Setelah Wawancara

7. Rangkum ke user dan minta konfirmasi SEBELUM menulis file. Sertakan daftar asumsi.
8. Tulis `context/game-overview.md` dan `context/game-design.md` (isi semua `[ISI]`).
9. Tulis `context/build-plan.md`: pecah MVP jadi feature bernomor per fase. Setiap feature selesai dalam satu sesi, bisa diverifikasi (dimainkan/dilihat), dan mengikuti urutan "core logic + test, lalu UI dengan data mock, lalu wiring". Feature 01 selalu Setup Project sesuai stack.
10. Salin daftar feature ke `context/progress-tracker.md` (Phase: 1, Berikutnya: 01).
11. Jika `context/stack.md` masih placeholder: rekomendasikan 1-2 stack dari `stacks/README.md` dengan alasan singkat berdasarkan genre, lalu minta user menjalankan `/choose-stack <id>`.

## Larangan

- Jangan menulis kode apapun di workflow ini.
- Jangan mengisi `ui-tokens.md` / `ui-rules.md` di sini (diisi setelah desain ada).
- Jangan menulis file sebelum user mengkonfirmasi rangkuman.

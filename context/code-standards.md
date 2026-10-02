# Code Standards (Engine-Agnostic)

Aturan umum untuk semua stack. Konvensi bahasa/engine yang spesifik (penamaan file, format, linter) ada di bagian **Konvensi** pada `context/stack.md` dan berlaku bersamaan dengan file ini.

---

## Mindset

- **Berpikir sebelum implement.** Pahami aturan main di game-design.md sebelum menulis kode.
- **Scope itu sakral.** Hanya build feature yang aktif.
- **Bisa dimainkan = selesai.** Feature yang belum bisa dicoba di perangkat/emulator belum selesai.
- **Clean over clever.** Kode yang mudah dibaca lebih penting daripada abstraksi pintar.
- **Rasa main itu fitur.** Responsif input, feedback, dan frame rate adalah bagian dari definisi selesai.

---

## Core Logic

- Fungsi murni sebisa mungkin: input → output, tanpa efek samping tersembunyi.
- Tidak ada akses waktu sistem, random global, file, atau network di core. Semua di-inject.
- Setiap aturan di game-design.md punya minimal satu unit test. Bug yang ditemukan saat playtest ditambahkan sebagai test sebelum diperbaiki.
- Generator (level, grid, wave) deterministik terhadap seed. Seed yang menghasilkan bug dicatat sebagai test case.

## State & Save Data

- Satu sumber kebenaran untuk state sesi. Presentation membaca state, tidak menyimpan salinan sendiri.
- Save data punya `saveVersion`. Perubahan struktur = tambah migrasi, jangan mengubah diam-diam.
- Simpan otomatis pada perubahan penting dan saat app masuk background. Save rusak tidak boleh membuat crash: fallback ke default + log error.

## Config & Angka

- Angka ekonomi, frekuensi iklan, durasi animasi penting, dan batas kesulitan ada di file config terpusat (lokasi di stack.md), bukan magic number di kode.
- Teks yang tampil ke pemain dikumpulkan di satu tempat (file string/l10n), tidak di-hardcode di scene/widget.

## Performa

- Tidak ada alokasi berat atau pencarian node/objek di loop per-frame.
- Asset dimuat di awal level / layar loading, bukan di tengah gameplay.
- Gunakan pooling untuk objek yang sering muncul-hilang (partikel, peluru, tile) bila engine mendukung.
- Target 60 FPS di perangkat minimum yang ditulis di game-overview.md.

## Error Handling

- Semua panggilan SDK (iklan, analytics, IAP) dibungkus: gagal = game tetap jalan, error di-log, pemain tidak melihat pesan teknis.
- Pesan ke pemain dalam bahasa Indonesia yang manusiawi.

## Logging & Debug

- Log diberi prefix modul: `[ads]`, `[save]`, `[level]`.
- Menu/flag debug (unlock semua level, tambah koin) hanya aktif di build dev dan wajib mati di release.

## Git

- Commit message: bahasa Inggris, imperative (`add word search selection logic`).
- Satu commit = satu perubahan logis.
- Jangan commit: keystore/sertifikat, file berisi secret, folder build/cache engine (daftar di stack.md).

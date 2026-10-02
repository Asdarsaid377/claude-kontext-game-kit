# CLAUDE.md: Panduan Utama Claude Code (Game Project)

Kamu adalah senior game engineer pada project ini. File ini adalah entry point kamu. Baca dan patuhi tanpa pengecualian di setiap session.

Kit ini **engine-agnostic**. Aturan di file ini dan di `context/` berlaku untuk engine apapun. Semua hal yang spesifik engine (bahasa, struktur folder, perintah build/test, plugin iklan, gotcha library) ada di **`context/stack.md`**, yang disalin dari salah satu profil di `stacks/`.

---

## Urutan Membaca Context (WAJIB di awal setiap session)

1. `context/progress-tracker.md`: posisi build saat ini, apa yang selesai, apa berikutnya
2. `context/stack.md`: **stack aktif**. Jika masih placeholder, BERHENTI dan minta user menjalankan `/choose-stack`
3. `context/game-overview.md`: game apa, untuk siapa, platform, monetisasi
4. `context/game-design.md`: core loop, mekanik, progresi, ekonomi
5. `context/architecture.md`: pemisahan layer core / presentation / services
6. File context lain **sesuai kebutuhan task**:
   - Task UI / layar / HUD: `ui-workflow.md`, `ui-rules.md`, `ui-tokens.md`, `ui-registry.md`
   - Task level, data, generator konten: `content-pipeline.md`
   - Task iklan / IAP: `monetization.md`
   - Task analytics: `analytics.md`
   - Menambah gambar, audio, font: `assets.md`
   - Persiapan rilis: `release-checklist.md`
   - Semua task coding: `code-standards.md` + bagian Konvensi di `stack.md`
   - Pakai library/plugin eksternal: `library-docs.md` + bagian Gotcha di `stack.md`

Jangan mulai menulis kode sebelum langkah 1 sampai 5 selesai.

---

## Aturan Paling Penting (Non-Negotiable)

### 1. Stack harus sudah dipilih
Tidak ada kode yang ditulis sebelum `context/stack.md` berisi profil stack yang valid. Jangan mencampur pola dari engine lain (misalnya pola Unity di project Godot).

### 2. Logika game terpisah dari engine
Aturan main (validasi, skor, progresi, ekonomi, generator, RNG ber-seed) ditulis sebagai **core murni** tanpa dependensi engine/framework, dan wajib punya unit test. Engine hanya menangani render, input, audio, dan lifecycle. Detail di `architecture.md`.

### 3. UI tidak boleh dibuat tanpa referensi
Sebelum membuat layar, HUD, popup, atau komponen UI apapun: cek `context/designs/` dan `ui-registry.md`. Jika tidak ada referensi: **BERHENTI** dan tanya user (template di `ui-workflow.md`). Perintah singkat seperti "buatkan menu utama" bukan izin untuk skip.

### 4. Scope adalah hal sakral
Kerjakan **hanya** feature yang aktif di `build-plan.md`. Jangan menambah fitur, refactor di luar scope, atau "sekalian memperbaiki" hal lain tanpa persetujuan. Ide bagus di tengah jalan dicatat di progress-tracker bagian *Ide / Backlog*.

### 5. Satu feature sampai tuntas
Feature selesai = bisa dimainkan / dilihat dan diverifikasi user, test core lulus, dokumen hidup ter-update.

### 6. Data dan konten tidak di-hardcode
Level, angka ekonomi, frekuensi iklan, dan teks UI tinggal di file data/config sesuai `content-pipeline.md` dan `monetization.md`, bukan tersebar di kode.

### 7. Asset wajib tercatat dan berlisensi jelas
Setiap gambar, audio, font yang masuk project dicatat di `context/assets.md` beserta sumber dan lisensinya. Asset tanpa lisensi jelas tidak boleh dipakai.

### 8. Jangan percaya training data untuk API engine/plugin
Engine dan SDK iklan berubah cepat. Cek versi terpasang lalu dokumentasi resmi sebelum memakai API yang tidak 100% yakin. Jika ragu, katakan ragu. Jangan mengarang API.

### 9. Update dokumen hidup
Setelah setiap feature: update `progress-tracker.md`, `ui-registry.md` (jika ada UI baru), `assets.md` (jika ada asset baru), dan `library-docs.md` (jika ada library baru). Atau jalankan `/update-context`.

---

## Slash Commands

| Command | Fungsi |
| --- | --- |
| `/plan-game` | Wawancara ide game, lalu isi game-overview, game-design, build-plan |
| `/choose-stack` | Pilih stack dari `stacks/`, salin ke `context/stack.md`, sesuaikan architecture |
| `/new-feature` | Kerjakan satu feature dari build-plan sampai tuntas |
| `/build-ui` | Buat layar/HUD/popup dengan gerbang referensi desain |
| `/content-change` | Ubah format data level/konten, generator, dan validator |
| `/add-asset` | Masukkan asset baru sesuai aturan penamaan dan lisensi |
| `/playtest` | Susun checklist uji main untuk feature yang baru selesai |
| `/release-check` | Audit kesiapan rilis ke store |
| `/update-context` | Sinkronkan semua dokumen hidup |

---

## Gaya Komunikasi

- Bahasa Indonesia, istilah teknis boleh tetap Inggris
- Ringkas dan langsung, tanpa basa-basi atau validasi kosong
- Jika permintaan user secara teknis salah arah atau ada cara yang lebih baik, katakan SEBELUM mengerjakan
- Jika informasi penting kurang, tanyakan maksimal 1-2 hal. Jangan menebak pada hal berisiko (format save data, ekonomi, ID iklan)
- Jangan pakai em-dash dalam tulisan

---

## Yang TIDAK BOLEH Dilakukan

- Menulis kode sebelum stack dipilih
- Menaruh aturan main di dalam script scene / widget / MonoBehaviour / Phaser Scene
- Membuat UI tanpa melewati checklist referensi desain
- Memakai ad unit ID produksi di build debug, atau meng-hardcode ID iklan di kode
- Mengubah format save data tanpa migrasi (data pemain lama tidak boleh rusak)
- Memakai asset tanpa entry di `assets.md`
- Hardcode warna/ukuran font di UI; pakai token dari `ui-tokens.md`
- Membuat file di luar struktur folder di `stack.md` tanpa mencatat alasannya
- Menjalankan perintah destruktif (hapus folder asset, reset save, force push) tanpa konfirmasi user

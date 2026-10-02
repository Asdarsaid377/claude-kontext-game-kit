# Playbook: Tahapan Prompt Memulai Game Baru

Panduan langkah demi langkah (beserta prompt siap-copy) untuk memulai game baru dari starter ini bersama Claude Code.

---

## Tahap 0: Persiapan (di luar Claude Code)

```bash
cp -r game-context-kit/ nama-game/
cd nama-game
git init
pip install -r tools/requirements.txt
```

Siapkan juga (boleh menyusul sebelum fase monetisasi): akun Google Play Console, AdMob, dan Firebase.

> Jangan lompat ke coding. Urutan playbook ini adalah bagian dari sistemnya.

---

## Tahap 1: Ide → Game Design

```
/plan-game [ide game kamu, 1-3 kalimat]
```

Contoh:

```
/plan-game Game TTS dan Cari Kata bahasa Indonesia untuk pemain 25+, offline, monetisasi AdMob, ada tantangan harian dan tema budaya Nusantara.
```

Sudah punya PRD? Taruh di `docs/PRD.md` lalu:

```
/plan-game Ide sudah ada di docs/PRD.md. Baca dulu, tanyakan hanya yang belum terjawab, lalu isi dokumen context.
```

**Checklist keluar tahap ini:**

- [ ] `game-overview.md` terisi, Out of Scope tidak kosong
- [ ] `game-design.md` berisi core loop dan tabel ekonomi dengan angka
- [ ] `build-plan.md` berisi feature bernomor
- [ ] Kamu sudah membaca ulang dan setuju

---

## Tahap 2: Pilih Stack

Minta rekomendasi:

```
/choose-stack
```

Atau langsung:

```
/choose-stack flutter
```

**Checklist keluar tahap ini:**

- [ ] `context/stack.md` berisi profil (bukan placeholder) dengan versi yang sudah dicek
- [ ] Tabel "Pemetaan ke Stack Aktif" di `architecture.md` terisi
- [ ] `tools/sync_config.json` punya `dest`
- [ ] Untuk Godot/Unity: kamu sudah membuat project kosong di editor sesuai lokasi di stack.md

---

## Tahap 3: Referensi Desain & Token

1. Taruh desain layar pertama di `context/designs/` (`main_menu.png`, `gameplay.png`, dst).
2. Ekstrak token:

```
Baca semua file di context/designs/. Ekstrak design tokens (warna, font, ukuran teks, radius, spacing yang berulang) lalu update context/ui-tokens.md dan sesuaikan context/ui-rules.md. Tunjukkan hasilnya sebelum menyimpan dan tandai nilai yang kamu tidak yakin.
```

> Belum punya desain? Boleh ditunda; saat `/build-ui` pilih opsi "build berdasarkan ui-rules" secara eksplisit. Konsekuensinya hampir pasti ada revisi visual.

---

## Tahap 4: Setup Project (Feature 01)

```
/new-feature 01
```

Verifikasi:

```
Jalankan perintah test core dan lint dari context/stack.md, lalu beri tahu saya cara menjalankan game di emulator. Laporkan error apa adanya, jangan diperbaiki diam-diam.
```

---

## Tahap 5: Loop Utama per Feature

1. **Session baru per feature:** `/new-feature [nomor]`
2. **Claude berhenti minta referensi desain?** Itu by design. Jawab:
   - "Sudah saya taruh di context/designs/[nama].png, lanjutkan"
   - "Build berdasarkan ui-rules saja, saya sadar konsekuensinya"
3. **Uji main:** `/playtest` lalu benar-benar mainkan di perangkat/emulator.
4. **Ubah format level/konten?** `/content-change [deskripsi]`
5. **Tambah gambar/suara/font?** `/add-asset [deskripsi + sumber + lisensi]`
6. **Tutup sesi:** `/update-context` lalu commit.

**Checklist per feature:**

- [ ] Test core lulus
- [ ] Dimainkan/diverifikasi sendiri (bukan hanya klaim Claude)
- [ ] Dokumen hidup ter-update
- [ ] Commit git dibuat

---

## Tahap 6: Rilis

```
/release-check android closed testing
```

Lalu ikuti item yang gagal satu per satu, dan verifikasi aturan store terbaru di Play Console.

---

## Prompt Situasional

**Melanjutkan di session baru:**

```
Baca context/progress-tracker.md dan context/stack.md, lalu lanjutkan dari posisi terakhir. Konfirmasi dulu apa yang akan kamu kerjakan.
```

**Bug gameplay:**

```
Bug: [gejala]. Langkah reproduksi: [langkah]. Seed/level: [jika ada]. Log: [paste].
Tulis dulu unit test yang mereproduksi bug ini di core (jika bug di aturan main), jelaskan akar masalahnya, lalu perbaiki hanya akar masalahnya.
```

**Balancing angka:**

```
Ubah [angka] di game-design.md dari X ke Y, lalu sesuaikan file config di kode. Jangan ubah angka lain. Tunjukkan diff-nya.
```

**Pattern drift:**

```
Berhenti. Baca ulang CLAUDE.md, context/architecture.md, dan bagian Konvensi di context/stack.md, lalu audit perubahan terakhir. Pastikan tidak ada aturan main di presentation dan tidak ada import engine di core. Laporkan pelanggaran dan perbaiki.
```

**Menambah plugin:**

```
Saya mau pakai [plugin] untuk [kebutuhan]. Sebelum install: cek versi terbaru dan kompatibilitasnya dengan versi engine di context/stack.md, konfirmasi API dari dokumentasi resmi, sebutkan trade-off, lalu setelah terpasang tambahkan entry di context/library-docs.md.
```

**Ganti stack:**

```
/choose-stack [id baru]
```

Claude akan berhenti dan menjelaskan apa yang terbawa dan apa yang harus ditulis ulang sebelum melanjutkan.

---

## Anti-Pattern

- ❌ "Buatkan seluruh game sekaligus": sistem ini per feature
- ❌ Menulis aturan main langsung di scene/widget: core tidak bisa dites dan tidak bisa dibawa pindah stack
- ❌ Mengedit file hasil generator secara manual
- ❌ Memakai asset "dari Google" tanpa lisensi jelas
- ❌ Menguji iklan dengan ad unit ID produksi (berisiko akun AdMob dibatasi)
- ❌ Menutup sesi tanpa `/update-context`

---

## Ringkasan Alur

```
Tahap 0  copy starter + git init
Tahap 1  /plan-game → game design dikonfirmasi
Tahap 2  /choose-stack → stack aktif
Tahap 3  desain → ui-tokens
Tahap 4  /new-feature 01 → setup terverifikasi
Tahap 5  loop: /new-feature N → /playtest → (/content-change, /add-asset) → /update-context → commit
Tahap 6  /release-check → rilis
```

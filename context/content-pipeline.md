# Content Pipeline

Cara konten game (level, puzzle, wave, dialog, daftar item) dibuat, divalidasi, dan dibundel. Konten disimpan **netral engine** di `content/` agar bisa dipakai stack apapun.

---

## Prinsip

1. **Sumber → generator → output → validator.** Output hasil generate tidak diedit manual; ubah sumber atau generator lalu generate ulang.
2. **Deterministik.** Generator menerima `--seed`; seed yang sama menghasilkan output yang sama.
3. **Validator wajib lulus** sebelum build release.
4. **Skema versioned.** Setiap file output punya `schemaVersion`.

---

## Struktur

```
content/
├── schema/              → JSON Schema per jenis konten
├── source/              → data sumber yang ditulis/dikurasi manusia (CSV/JSON)
└── build/               → output generator (dibundel ke game)
tools/
├── gen_<jenis>.py       → generator
├── validate.py          → validasi semua file di content/build terhadap schema + aturan bisnis
└── requirements.txt
```

Cara konten masuk ke engine (salin ke folder asset engine / dibaca langsung) dijelaskan di `context/stack.md` bagian Konten.

---

## Jenis Konten

> **TEMPLATE:** Isi per project.

### `[ISI nama jenis konten]`
- **Sumber:** `content/source/[ISI]`
- **Generator:** `tools/gen_[ISI].py --seed N [opsi]`
- **Output:** `content/build/[ISI]/*.json`
- **Skema:** `content/schema/[ISI].schema.json`
- **Aturan validasi bisnis:** `[ISI]` (contoh: tidak ada kata duplikat dalam satu level, semua kata saling terhubung, tingkat kesulitan naik monoton)
- **Contoh data:**
```json
{ "schemaVersion": 1 }
```

---

## Kurasi Konten

- Konten buatan/bantuan AI wajib direview manusia sebelum status `reviewed`. Generator hanya memakai data `reviewed`.
- Perhatikan hak cipta: jangan menyalin isi kamus, buku, atau game lain apa adanya.
- Siapkan blocklist untuk kata/kombinasi yang tidak pantas jika konten dibentuk acak.

---

## Changelog Skema

_Format: tanggal, jenis konten, versi lama → baru, perubahan, migrasi yang dibuat._

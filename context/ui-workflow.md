# UI Workflow: Gerbang Wajib Sebelum Membuat UI

Berlaku untuk semua layar, HUD, popup/dialog, dan komponen UI di engine apapun. Tujuannya: UI konsisten dengan desain yang diinginkan user, bukan "selera default" AI.

---

## Prinsip

1. **Desain adalah source of truth.**
2. **Tidak ada referensi = tidak ada UI.**
3. **Registry sebelum inovasi.** Komponen mirip sudah ada? Pakai/extend, jangan buat varian baru.

---

## Checklist (berurutan)

### Step 1: Cari referensi di `context/designs/`

Penamaan: `<nama-layar>.png`, `<nama-layar>-<bagian>.png`, contoh `main_menu.png`, `gameplay-hud.png`, `popup-level_complete.png`.

**Ditemukan?** Buka gambarnya, ekstrak layout, hierarki, ukuran relatif, elemen. Lanjut Step 2.

**Tidak ditemukan?** **BERHENTI** dan tanyakan:

> Saya tidak menemukan referensi desain untuk **[nama layar/komponen]** di `context/designs/`.
> Pilih salah satu:
> 1. Taruh gambar desain di `context/designs/[nama].png`
> 2. Berikan link Figma / screenshot game referensi yang mau ditiru gayanya
> 3. Izinkan saya build berdasarkan `ui-rules.md` + `ui-tokens.md` saja (kemungkinan perlu revisi visual)

Jika user memilih 3, catat di progress-tracker bagian *Decisions*.

### Step 2: Cek `ui-registry.md`
Pakai ulang komponen yang ada. Dilarang membuat duplikat dengan nama beda.

### Step 3: Baca aturan visual
`ui-rules.md`, `ui-tokens.md`, dan bagian UI di `stack.md`. Dilarang hardcode warna/ukuran font.

### Step 4: Build
Data mock dulu jika logic belum ada. Cek di minimal dua ukuran layar (kecil dan besar) serta layar dengan notch.

### Step 5: Update registry
Tambahkan entry di `ui-registry.md`.

---

## Kapan Boleh Skip Step 1?

Hanya jika user dalam pesan yang sama mengatakan eksplisit "tanpa referensi, pakai ui-rules saja", atau komponen adalah elemen debug yang tidak tampil di build release.

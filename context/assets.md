# Assets

Registry dan aturan semua asset (gambar, sprite, audio, font, animasi). **Dokumen hidup**: setiap asset baru dicatat di sini.

---

## Aturan

1. Tidak ada asset tanpa sumber dan lisensi yang jelas. Lisensi aman untuk komersial: CC0, lisensi aset berbayar yang mengizinkan komersial, OFL (font), karya sendiri.
2. Lisensi yang mewajibkan atribusi (misalnya CC-BY): wajib dicantumkan di layar Kredit.
3. File sumber disimpan di `assets-src/`; file siap pakai di folder asset engine (lihat stack.md).
4. Tidak memakai karakter, logo, atau aset dari game/merek lain.

---

## Konvensi Penamaan

- huruf kecil, `snake_case`, tanpa spasi: `btn_play.png`, `sfx_correct.ogg`
- Prefix per jenis:

| Prefix | Jenis |
| --- | --- |
| `bg_` | background |
| `btn_` | tombol |
| `ic_` | ikon |
| `spr_` | sprite / spritesheet |
| `fx_` | efek visual |
| `sfx_` | efek suara |
| `mus_` | musik |
| `font_` | font |

---

## Batas Teknis

> **TEMPLATE:** sesuaikan dengan target perangkat.

| Jenis | Format | Batas |
| --- | --- | --- |
| Gambar UI | PNG (atau WebP jika engine mendukung) | sisi terpanjang ≤ 2048 px |
| Sprite sheet / atlas | PNG | ≤ 2048 x 2048 |
| SFX | OGG (atau sesuai rekomendasi engine) | ≤ 200 KB, mono |
| Musik | OGG | ≤ 3 MB, loop mulus |
| Font | TTF/OTF | subset jika memungkinkan |

---

## Asset Store (wajib saat rilis)

- [ ] Ikon aplikasi (512 x 512 untuk Play Store + adaptive icon)
- [ ] Feature graphic 1024 x 500 (Play Store)
- [ ] Screenshot store (minimal 4)
- [ ] Video promo (opsional)

---

## Registry

| Path | Jenis | Sumber | Lisensi | Atribusi |
| --- | --- | --- | --- | --- |
| _kosong_ | | | | |

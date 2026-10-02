# UI Registry

Dokumen hidup. Di-update setiap kali komponen UI selesai dibuat. **Baca sebelum membangun komponen baru.**

---

## Cara Pakai

1. Cek apakah komponen serupa sudah ada.
2. Ada: pakai yang sama atau extend parameternya.
3. Belum ada: build mengikuti `ui-workflow.md`, `ui-rules.md`, `ui-tokens.md`, lalu tambahkan ke sini.

---

## Format Entry

```markdown
### NamaKomponen
- **Path:** <lokasi file sesuai stack>
- **Jenis:** layar / popup / HUD / komponen
- **Dipakai di:** layar yang memakai
- **Referensi desain:** context/designs/<file>.png (atau "tanpa referensi, keputusan tercatat di progress-tracker")
- **Token kunci:** color.surface, radius.md, text.title
- **Catatan:** varian, parameter penting, batasan
```

---

## Komponen

_Kosong. Komponen ditambahkan di sini saat dibangun._

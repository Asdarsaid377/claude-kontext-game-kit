# Content

Data konten game dalam format **netral engine** (JSON). Detail aturan di `../context/content-pipeline.md`.

```
schema/   → JSON Schema per jenis konten: <jenis>.schema.json
source/   → data sumber yang ditulis/dikurasi manusia (CSV/JSON)
build/    → output generator, satu folder per jenis: build/<jenis>/*.json
```

Aturan: file di `build/` tidak diedit manual. Ubah `source/` atau generator di `../tools/`, lalu generate ulang.

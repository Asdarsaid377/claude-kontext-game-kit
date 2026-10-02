# Library Docs

Catatan library/plugin yang dipakai project ini. Tujuan: mencegah Claude Code mengarang API dari training data yang usang. Gotcha umum per engine sudah ada di bagian **Gotcha** pada `context/stack.md`; file ini untuk catatan spesifik project.

**Aturan utama:** jika tidak 100% yakin dengan API (nama package, signature, perilaku di versi terpasang), **jangan menebak**. Cek versi terpasang di file dependensi engine (lihat stack.md), lalu baca dokumentasi resmi atau source/type definition plugin.

Area paling rawan di game mobile:
- SDK iklan (AdMob dan plugin wrapper per engine): API init, consent, dan nama callback sering berubah antar versi mayor
- Konfigurasi Android (Gradle, minSdk, AndroidManifest, App ID iklan)
- Plugin pihak ketiga/komunitas: cek tanggal rilis terakhir dan kompatibilitas dengan versi engine

---

## Catatan Per Library

> **TEMPLATE:** Setiap library/plugin baru ditambahkan di sini.

### [nama-library] (v[x.y.z])

- **Dipakai untuk:** ...
- **Sumber dokumentasi:** ...
- **Pola standar di project ini:** ...
- **Gotcha:** ...

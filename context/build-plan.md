# Build Plan

## Prinsip Inti

**Core logic dengan test dulu, lalu UI dengan data mock, lalu wiring.** Setiap feature harus bisa dimainkan atau dilihat sebelum lanjut. Tidak ada fase "tidak kelihatan" yang panjang.

Urutan pengerjaan setiap feature gameplay:

1. Aturan di game-design.md dikonfirmasi
2. Core logic + unit test lulus
3. Referensi desain dikonfirmasi (ui-workflow.md)
4. UI/scene dengan data mock, diverifikasi visual
5. Wiring core ↔ UI ↔ services
6. Edge case (keluar-masuk app, offline, iklan gagal)
7. Update dokumen hidup

---

> **TEMPLATE:** Diisi lewat `/plan-game`. Setiap feature selesai dalam satu sesi dan bisa diverifikasi. Nomori berurutan agar mudah dirujuk ("kerjakan 05").

## Phase 1: Foundation

### 01 Setup Project
- Init project sesuai `context/stack.md` (bagian Setup)
- Struktur folder sesuai Mapping di stack.md
- Interface services + implementasi fake/no-op
- Config terpusat (ekonomi, iklan) + token UI
- Test runner core jalan dengan 1 test contoh
- **Verifikasi:** app terbuka di emulator/perangkat menampilkan layar kosong dengan warna background dari token; test contoh lulus

### 02 Content Pipeline
- Skema + generator + validator untuk jenis konten utama, sample data
- Parser konten di core + test
- **Verifikasi:** `tools/validate.py` lulus, parser membaca sample tanpa error

### 03 [ISI: core gameplay]
**Core:** ...
**UI:** ...
**Verifikasi:** ...

## Phase 2: Meta Game

### 0N [ISI: menu, level select, progres, save]

## Phase 3: Monetisasi & Polish

### 0N Iklan (consent, banner, interstitial, rewarded)
### 0N Analytics + crash reporting
### 0N Audio, haptics, animasi, onboarding

## Phase 4: Konten & Rilis

### 0N Produksi konten penuh
### 0N Asset store + build release (`/release-check`)

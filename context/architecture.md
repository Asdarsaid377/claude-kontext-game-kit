# Architecture

Arsitektur ini **engine-agnostic**. Tujuannya: logika game bisa diuji tanpa engine, dan jika suatu saat pindah stack, aturan main, konten, dan test case bisa dibawa.

---

## Layer

```
┌──────────────────────────────────────────────┐
│ Presentation (engine-specific)               │
│ scene / widget / layar, HUD, animasi, input   │
└───────────────▲──────────────────────────────┘
                │ memanggil & mendengar state
┌───────────────┴──────────────────────────────┐
│ Game State / Controller                      │
│ menghubungkan core ↔ presentation ↔ services  │
└───────▲───────────────────────────▲──────────┘
        │                           │ lewat interface (port)
┌───────┴────────────┐   ┌──────────┴───────────┐
│ Core (MURNI)       │   │ Services (adapter)   │
│ aturan main, skor, │   │ Ads, Analytics,      │
│ ekonomi, generator,│   │ Storage, Audio,      │
│ parser konten, RNG │   │ Haptics, Clock, IAP  │
└────────────────────┘   └──────────────────────┘
```

### Core
- Tanpa import engine/framework/plugin apapun. Hanya bahasa + standard library.
- Deterministik: semua acak lewat RNG ber-seed yang di-inject; waktu lewat interface `Clock`.
- Wajib unit test. Ini bagian yang paling mahal jika salah.

### Game State / Controller
- Memegang state sesi (level aktif, skor, sisa waktu) dan memanggil core.
- Tidak menggambar apapun dan tidak memanggil SDK langsung.

### Presentation
- Hanya render, animasi, input, dan meneruskan aksi pemain ke controller.
- Tidak ada aturan main di sini. Jika ada `if` yang menentukan menang/kalah di file scene, itu pelanggaran.

### Services (Ports & Adapters)
Setiap layanan eksternal diakses lewat interface. Implementasi nyata dan implementasi palsu (fake/no-op untuk test dan dev) wajib ada.

| Port | Tanggung jawab |
| --- | --- |
| `AdsService` | init + consent, load/show banner, interstitial, rewarded; callback reward |
| `AnalyticsService` | `logEvent(name, params)` sesuai `analytics.md` |
| `StorageService` | baca/tulis save data dengan `saveVersion` + migrasi |
| `AudioService` | SFX, musik, mute sesuai setting |
| `HapticsService` | getar ringan/sedang |
| `Clock` | waktu sekarang, tanggal lokal (untuk fitur harian) |
| `IapService` | (fase berikutnya) pembelian & restore |

Aturan frekuensi iklan (kapan interstitial boleh tampil) adalah logika core/controller, bukan bagian adapter SDK.

---

## Folder Netral (sama di semua stack)

```
/
├── CLAUDE.md
├── .claude/commands/        → slash commands
├── context/                 → dokumen context + designs/
├── stacks/                  → profil stack (sumber; yang aktif disalin ke context/stack.md)
├── content/                 → data konten netral engine (JSON) + schema/
├── tools/                   → generator & validator konten (Python), dijalankan developer
├── assets-src/              → file sumber asset (PSD, Aseprite, WAV master)
└── <folder engine>          → struktur sesuai context/stack.md
```

`content/`, `tools/`, dan `assets-src/` sengaja di luar folder engine supaya bisa dibawa jika pindah stack. Build step di stack.md menjelaskan cara konten disalin/dibundel ke engine.

---

## Pemetaan ke Stack Aktif

> Diisi oleh `/choose-stack` dari bagian Mapping di `context/stack.md`.

| Konsep | Lokasi di stack aktif |
| --- | --- |
| Core | `[diisi /choose-stack]` |
| Game State / Controller | `[diisi /choose-stack]` |
| Presentation | `[diisi /choose-stack]` |
| Services (interface) | `[diisi /choose-stack]` |
| Services (implementasi) | `[diisi /choose-stack]` |
| Config (ekonomi, iklan) | `[diisi /choose-stack]` |
| UI tokens | `[diisi /choose-stack]` |
| Test core | `[diisi /choose-stack]` |

---

## Environment

`[ISI]`: flavor/build variant (dev memakai test ad ID dan analytics debug, prod memakai ID asli), lokasi keystore (di luar repo), cara build release.

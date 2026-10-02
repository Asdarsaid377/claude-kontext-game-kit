# Game Context Kit

Starter kit **context system** untuk membangun game mobile bersama Claude Code dengan disiplin senior engineer, dengan **stack yang bisa diganti** sesuai jenis game (Flutter, Godot, Unity, Phaser + Capacitor, atau profil baru yang kamu tambahkan).

Saudara dari [claude-context-kit](https://github.com/Asdarsaid377/claude-context-kit) (versi web app). Polanya sama: `CLAUDE.md` + slash commands + dokumen hidup di `context/`. Bedanya, semua aturan di sini engine-agnostic, dan hal yang spesifik engine dipisah ke profil di `stacks/`.

Starter ini **bukan boilerplate kode**: ini kerangka context + workflow agar Claude Code konsisten antar session dan antar project.

---

## Struktur

```
/
├── CLAUDE.md                     → Entry point Claude Code (aturan non-negotiable)
├── Playbook.md                   → Tahapan + prompt siap-copy untuk project baru
├── .claude/commands/
│   ├── plan-game.md              → /plan-game: wawancara ide → overview, design, build-plan
│   ├── choose-stack.md           → /choose-stack: aktifkan profil stack
│   ├── new-feature.md            → /new-feature: satu feature sampai tuntas
│   ├── build-ui.md               → /build-ui: layar/HUD dengan gerbang referensi desain
│   ├── content-change.md         → /content-change: ubah skema/generator konten dengan aman
│   ├── add-asset.md              → /add-asset: asset + lisensi + penamaan
│   ├── playtest.md               → /playtest: checklist uji main
│   ├── release-check.md          → /release-check: audit kesiapan rilis
│   └── update-context.md         → /update-context: sinkron dokumen hidup
├── context/
│   ├── stack.md                  → STACK AKTIF (salinan dari stacks/<id>.md)
│   ├── game-overview.md          → [ISI] game apa, untuk siapa, platform, layar
│   ├── game-design.md            → [ISI] core loop, mekanik, progresi, ekonomi
│   ├── architecture.md           → layer core / controller / presentation / services
│   ├── code-standards.md         → standar umum lintas engine
│   ├── content-pipeline.md       → [ISI] format konten, generator, validator
│   ├── monetization.md           → [ISI] aturan iklan & IAP
│   ├── analytics.md              → daftar event resmi
│   ├── assets.md                 → dokumen hidup: registry asset + lisensi
│   ├── ui-workflow.md            → gerbang UI: tanpa referensi = tidak ada UI
│   ├── ui-rules.md               → [SESUAIKAN] aturan UI game (touch, safe area, popup)
│   ├── ui-tokens.md              → [SESUAIKAN] token netral engine
│   ├── ui-registry.md            → dokumen hidup: komponen UI yang sudah ada
│   ├── library-docs.md           → catatan library/plugin per project
│   ├── build-plan.md             → [ISI] fase & feature bernomor
│   ├── progress-tracker.md       → dokumen hidup: status build
│   ├── release-checklist.md      → checklist rilis store
│   └── designs/                  → referensi desain (png/jpg)
├── stacks/
│   ├── README.md                 → matriks pemilihan stack
│   ├── _TEMPLATE.md              → template profil stack baru
│   ├── flutter.md
│   ├── godot.md
│   ├── unity.md
│   └── phaser-capacitor.md
├── content/                      → konten netral engine: schema/, source/, build/
├── tools/                        → validate.py, sync_content.py, generator konten
└── assets-src/                   → file sumber asset (PSD, Aseprite, WAV master)
```

---

## Cara Kerja Stack yang Bisa Diganti

1. Semua aturan umum (arsitektur, standar kode, UI, konten, monetisasi) ditulis **tanpa menyebut engine**.
2. Setiap profil di `stacks/` lengkap dan mandiri: versi, struktur folder, mapping arsitektur, konvensi, cara implementasi token UI, plugin iklan/analytics/storage, perintah build/test, gotcha, dan pembagian kerja Claude Code vs editor.
3. `/choose-stack <id>` menyalin profil ke `context/stack.md`, mengisi mapping di `architecture.md`, `.gitignore`, dan `tools/sync_config.json`.
4. Logika game wajib berupa **core murni** (tanpa engine) dengan unit test, dan konten disimpan di `content/` sebagai JSON. Dua hal ini yang membuat pindah stack tetap realistis.

Menambah stack baru (misalnya Defold, Cocos, React Native): salin `stacks/_TEMPLATE.md`, isi, lalu daftarkan di `stacks/README.md`.

---

## Cara Pakai untuk Game Baru

1. Copy seluruh folder ini sebagai root project baru, lalu `git init`.
2. Jalankan `/plan-game [ide game]` → isi game-overview, game-design, build-plan.
3. Jalankan `/choose-stack [id]` (atau tanpa argumen untuk minta rekomendasi).
4. Taruh referensi desain di `context/designs/`, ekstrak token ke `ui-tokens.md`.
5. `/new-feature 01`, lalu loop per feature.

Detail lengkap dan prompt siap-copy: `Playbook.md`.

---

## Sudah Punya PRD?

Jika dokumen PRD/GDD sudah ada (misalnya hasil brainstorming di luar Claude Code), taruh di `docs/PRD.md` lalu jalankan:

```
/plan-game Ide sudah ada di docs/PRD.md. Baca dokumen itu dulu, tanyakan hanya hal yang belum terjawab, lalu isi game-overview.md, game-design.md, dan build-plan.md.
```
# claude-kontext-game-kit

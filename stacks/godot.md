# Stack: Godot 4

> Profil stack. Disalin ke `context/stack.md` oleh `/choose-stack`.
> **Diaktifkan:** (tanggal, diisi /choose-stack)

---

## Kapan Cocok / Tidak Cocok

- **Cocok:** 2D arcade, platformer, puzzle fisika, top-down, endless runner, game dengan banyak scene dan animasi. Engine gratis dan open source, APK relatif kecil.
- **Cukup cocok:** 3D sederhana/stylized.
- **Tidak cocok:** game yang sangat bergantung pada SDK pihak ketiga yang hanya resmi untuk Unity; tim yang tidak mau menyentuh editor sama sekali.

## Stack

| Layer | Tool | Versi |
| --- | --- | --- |
| Engine | Godot 4.x (standard, bukan .NET, kecuali diputuskan lain) | (diisi /choose-stack) |
| Bahasa | GDScript dengan static typing | ikut engine |
| Test | GUT atau gdUnit4 (pilih satu, catat di library-docs) | |
| Iklan | Plugin AdMob komunitas untuk Godot 4 (Android plugin v2) | cek kompatibilitas dengan versi engine |
| Analytics & crash | Plugin Firebase komunitas, atau tunda ke fase berikutnya | |
| Storage | `FileAccess` + JSON di `user://` | bawaan |
| Audio | `AudioStreamPlayer` + audio bus | bawaan |
| Haptics | `Input.vibrate_handheld()` | bawaan |

## Mapping ke Arsitektur

Semua path relatif terhadap folder `game/` (root project Godot).

| Konsep | Lokasi |
| --- | --- |
| Core | `scripts/core/` (class `RefCounted`, tanpa akses node/scene tree) |
| Game State / Controller | `scripts/controllers/` + autoload `GameState` |
| Presentation | `scenes/` (.tscn) + script node di `scenes/**/` |
| Services (interface) | `scripts/services/` (base class dengan method kosong) |
| Services (implementasi) | `scripts/services/impl/` dan `scripts/services/fake/`, didaftarkan lewat autoload `Services` |
| Config (ekonomi, iklan) | `config/economy.json`, `config/ads.json` (dibaca core) |
| UI tokens | `ui/theme/game_theme.tres` + `scripts/ui/tokens.gd` |
| Test core | `tests/core/` |

## Struktur Folder

```
<root>/                         → repo (CLAUDE.md, context/, content/, tools/, assets-src/)
└── game/                       → PROJECT GODOT (res://)
    ├── project.godot
    ├── export_presets.cfg          → (lihat .gitignore: preset boleh di-commit tanpa password)
    ├── addons/                     → plugin (GUT/gdUnit4, AdMob)
    ├── autoload/                   → GameState.gd, Services.gd, Audio.gd
    ├── scenes/
    │   ├── main/                   → Main.tscn (root, ganti layar)
    │   ├── screens/                → MainMenu.tscn, LevelSelect.tscn, Gameplay.tscn
    │   ├── popups/
    │   └── components/             → tombol, tile, HUD
    ├── scripts/
    │   ├── core/                   → PURE: aturan main, generator, parser konten
    │   ├── controllers/
    │   ├── services/{impl,fake}/
    │   └── ui/
    ├── ui/theme/
    ├── content/                    → hasil salin dari ../content/build/
    ├── assets/{images,audio,fonts}/
    ├── config/
    └── tests/{core,integration}/
```

## Konvensi

- File & folder: `snake_case` untuk script, `PascalCase.tscn` untuk scene (pilih satu gaya dan konsisten; catat jika berbeda).
- Class: `class_name PascalCase`. Fungsi/variabel: `snake_case`. Konstanta: `UPPER_SNAKE`. Signal: kata kerja lampau (`level_completed`).
- **Static typing wajib**: `var score: int = 0`, `func add(a: int) -> int:`. Aktifkan warning untuk untyped di Project Settings.
- `scripts/core/` tidak boleh memakai `get_node`, `$`, `get_tree()`, autoload, atau `Input`. Hanya data in/out.
- Komunikasi anak ke induk lewat **signal**; induk ke anak lewat method. Hindari `get_node("../../..")`.
- Autoload seminimal mungkin: `GameState`, `Services`, `Audio`.
- Node yang sering dipakai di-cache dengan `@onready var`.

## UI & Token

- Satu `Theme` resource (`ui/theme/game_theme.tres`) dipasang di root Control; warna dan font dari `context/ui-tokens.md`.
- `scripts/ui/tokens.gd` (`class_name Tokens`) menyimpan konstanta warna/spacing/motion untuk dipakai di script (tween, warna dinamis).
- Stretch mode: `canvas_items`, aspect `expand`, resolusi dasar sesuai `ui-rules.md`. Gunakan anchor & container, bukan posisi absolut.
- Safe area: gunakan `DisplayServer.get_display_safe_area()` untuk menggeser HUD.

## Konten

- Project Godot ditaruh di subfolder `game/` agar `content/`, `tools/`, dan `assets-src/` di root tidak ikut di-import Godot (Godot otomatis meng-import file `.csv` sebagai terjemahan). `dest` di `tools/sync_config.json` = `game/content`.
- `tools/sync_content.py` menyalin `content/build/` ke `game/content/`, baca dengan `FileAccess.get_file_as_string("res://content/...")` lalu `JSON.parse_string`.
- Pastikan filter export menyertakan `*.json` (Export > Resources > Filters to export non-resource files).

## Services

### Iklan
- Godot tidak punya plugin AdMob resmi dari Google. Gunakan plugin komunitas yang mendukung **Android plugin v2 (Godot 4.2+)**; cek repo aktif, versi engine yang didukung, dan dukungan UMP consent sebelum dipasang. Catat pilihan di library-docs.
- Butuh **Gradle build** di export Android (Use Gradle Build) dan Android build template terpasang.
- App ID & ad unit ID di `config/ads.json` dengan set dev (test ID) dan prod; dipilih berdasarkan feature tag export (`OS.has_feature("release")` / feature tag kustom).

### Analytics & Crash
- Plugin Firebase untuk Godot bersifat komunitas. Jika belum stabil untuk versi engine, tunda dan gunakan `FakeAnalytics` yang hanya `print` di dev.

### Storage / Save
- `user://save.json` ber-`saveVersion`. Tulis ke file sementara lalu rename agar tidak korup.
- Simpan saat `NOTIFICATION_APPLICATION_PAUSED` / `NOTIFICATION_WM_GO_BACK_REQUEST` juga.

### Audio & Haptics
- Bus `Master`, `Music`, `SFX`; mute lewat `AudioServer.set_bus_mute`. SFX format OGG/WAV pendek.
- Getar: `Input.vibrate_handheld(ms)`; butuh permission VIBRATE di export preset Android.

## Perintah

| Tujuan | Perintah |
| --- | --- |
| Setup | User membuat project baru di editor Godot **di folder `game/`** (Renderer: Mobile atau Compatibility), lalu Claude Code membuat struktur folder & script |
| Run dev | `godot --path game` (atau F5 di editor) |
| Lint / format | `gdlint` dan `gdformat` dari paket `gdtoolkit` (pip) |
| Test core (GUT) | `godot --headless --path game -s addons/gut/gut_cmdln.gd -gdir=res://tests/core -gexit` |
| Test core (gdUnit4) | lihat runner CLI di dokumentasi gdUnit4 versi terpasang |
| Sinkron konten | `python tools/validate.py && python tools/sync_content.py` |
| Build release Android | `godot --headless --path game --export-release "Android" ../build/game.aab` (preset harus sudah ada) |

## Build & Rilis

- Export template sesuai versi engine wajib terpasang. Android SDK/JDK path diatur di Editor Settings (dilakukan user).
- Keystore release diatur di export preset; password **tidak** di-commit (gunakan environment variable yang didukung Godot atau isi lokal).
- Naikkan `version/code` dan `version/name` di preset Android.

## .gitignore

```
game/.godot/
build/
*.translation
export_credentials.cfg
game/android/build/
*.keystore
*.jks
```

## Gotcha

- Godot 3 vs 4: banyak API berubah (`yield` → `await`, `KinematicBody2D` → `CharacterBody2D`, `export` → `@export`, `onready` → `@onready`). **Jangan pakai contoh Godot 3.**
- Android plugin v1 sudah tidak dipakai di Godot 4.2+; plugin iklan lama berbasis v1 tidak akan jalan.
- File `.tscn`/`.tres` adalah teks, tapi mengeditnya manual rawan merusak UID/ExtResource. Untuk scene kompleks, minta user membuatnya di editor atau buat node lewat script.
- `.godot/` adalah cache; jangan di-commit. Folder `*.import` sidecar **di-commit**.
- JSON number selalu jadi `float` saat di-parse; cast ke `int` secara eksplisit.
- Physics di `_physics_process`, visual/UI di `_process`.

## Catatan Kerja Claude Code

- Bisa dari CLI: script GDScript, test headless, config JSON, export release (jika preset sudah ada).
- User perlu: membuat project & export preset di editor, memasang export template & Android SDK, menyusun scene visual yang kompleks (atau menyetujui scene dibuat lewat script), menguji di perangkat.

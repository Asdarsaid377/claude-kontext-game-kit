# Stack: Flutter

> Profil stack. Disalin ke `context/stack.md` oleh `/choose-stack`.
> **Diaktifkan:** (tanggal, diisi /choose-stack)

---

## Kapan Cocok / Tidak Cocok

- **Cocok:** game berbasis UI/grid/teks (TTS, cari kata, kuis, trivia, kartu, sudoku, idle/clicker, merge sederhana). Banyak layar menu. Developer yang terbiasa membangun app.
- **Cukup cocok dengan Flame:** 2D arcade ringan, sprite animasi sederhana, game loop per frame.
- **Tidak cocok:** 3D, fisika kompleks, game dengan ratusan objek bergerak per frame, butuh editor level visual.

## Stack

| Layer | Tool | Versi |
| --- | --- | --- |
| Framework | Flutter (channel stable) | (diisi /choose-stack) |
| Bahasa | Dart (null safety, sound) | ikut Flutter |
| Game loop (opsional) | `flame` | hanya jika game butuh loop per frame |
| State | `flutter_riverpod` | (cek mayor: API v2 dan v3 berbeda) |
| Routing | `go_router` | |
| Storage | `shared_preferences` untuk setting kecil + file JSON / `hive_ce` untuk save data | |
| Iklan | `google_mobile_ads` (plugin resmi Google, termasuk UMP consent) | |
| Analytics & crash | `firebase_core`, `firebase_analytics`, `firebase_crashlytics` | |
| Audio | `audioplayers` atau `flame_audio` (jika pakai Flame) | |
| Haptics | `HapticFeedback` (bawaan Flutter services) | |
| Test | `flutter_test` + `test` | |
| Lint | `flutter_lints` / `very_good_analysis` | |

## Mapping ke Arsitektur

| Konsep | Lokasi |
| --- | --- |
| Core | `lib/core/` (pure Dart, tanpa import `package:flutter`) |
| Game State / Controller | `lib/features/<fitur>/application/` (Riverpod Notifier) |
| Presentation | `lib/features/<fitur>/presentation/` (widget/layar), `lib/game/` (komponen Flame jika dipakai) |
| Services (interface) | `lib/services/<nama>_service.dart` |
| Services (implementasi) | `lib/services/impl/` (real) dan `lib/services/fake/` |
| Config (ekonomi, iklan) | `lib/config/economy.dart`, `lib/config/ads_config.dart`, `lib/config/env.dart` |
| UI tokens | `lib/ui/tokens.dart` + `lib/ui/theme.dart` |
| Test core | `test/core/` |

## Struktur Folder

```
<root>/
├── lib/
│   ├── main_dev.dart            → entry flavor dev
│   ├── main_prod.dart           → entry flavor prod
│   ├── app.dart                 → MaterialApp.router + theme
│   ├── bootstrap.dart           → init services (ads, firebase, storage)
│   ├── core/                    → PURE DART: aturan main, model, generator, parser konten
│   ├── config/
│   ├── services/
│   │   ├── impl/
│   │   └── fake/
│   ├── features/
│   │   └── <fitur>/
│   │       ├── application/     → Notifier/controller
│   │       └── presentation/    → layar & widget
│   ├── game/                    → (opsional) FlameGame & components
│   ├── ui/                      → tokens, theme, widget umum (GameButton, Popup)
│   └── l10n/ atau strings.dart  → teks UI
├── assets/
│   ├── content/                 → hasil salin dari content/build/
│   ├── images/  audio/  fonts/
├── test/
│   ├── core/
│   └── features/
├── android/  ios/
└── pubspec.yaml
```

## Konvensi

- File: `snake_case.dart`. Class: `PascalCase`. Variabel/fungsi: `camelCase`.
- `lib/core/` **dilarang** import `package:flutter/*` atau plugin apapun. Cek dengan grep sebelum menyelesaikan feature.
- Widget: satu widget publik per file; widget privat kecil boleh di file yang sama.
- `const` constructor di mana memungkinkan.
- Model immutable (`final` field, `copyWith`). Boleh pakai `freezed` jika disetujui user, catat di library-docs.
- Async: jangan `await` di `build()`. Gunakan `AsyncValue` Riverpod untuk loading/error.
- Tidak ada logic di `build()` selain menyusun widget dari state.

## UI & Token

- `lib/ui/tokens.dart` berisi class `AppColors`, `AppText`, `AppSpace`, `AppRadius`, `AppMotion` dengan nilai **persis** dari `context/ui-tokens.md`.
- `lib/ui/theme.dart` membangun `ThemeData` dari token. Widget memakai token/theme, tidak menulis `Color(0x...)` atau `fontSize: 18` langsung.
- Safe area: bungkus layar dengan `SafeArea`. Uji dengan beberapa ukuran device di emulator.
- Skala teks: hormati setting ukuran font in-game (`MediaQuery.textScaler` atau multiplier dari setting).

## Konten

- `tools/` menghasilkan `content/build/`. Script `tools/sync_content.py` (atau perintah di tabel Perintah) menyalin ke `assets/content/`.
- Daftarkan folder di `pubspec.yaml` bagian `flutter: assets:`.
- Muat lewat `rootBundle.loadString`, parse di core (fungsi pure menerima `String`/`Map`).

## Services

### Iklan
- Plugin `google_mobile_ads`. App ID AdMob wajib di `AndroidManifest.xml` (`meta-data` `com.google.android.gms.ads.APPLICATION_ID`) dan `Info.plist` (`GADApplicationIdentifier`). Tanpa ini app crash saat start.
- Consent: gunakan API UMP yang disediakan plugin (`ConsentInformation`, `ConsentForm`) sebelum `MobileAds.instance.initialize()` memuat iklan.
- Ad unit ID per flavor di `lib/config/env.dart`; dev = test ID resmi Google.
- Banner: `AdWidget` di ruang tetap. Interstitial/rewarded: load di depan, `dispose` setelah tampil, load berikutnya.

### Analytics & Crash
- Firebase lewat `flutterfire configure`. File `firebase_options.dart` boleh di-commit (bukan secret), `google-services.json` ikut kebijakan project.
- `FlutterError.onError` dan `PlatformDispatcher.instance.onError` diarahkan ke Crashlytics di prod.

### Storage / Save
- Save data satu dokumen JSON ber-`saveVersion` di file app documents (`path_provider`) atau box `hive_ce`.
- Catatan: package `hive` asli tidak lagi aktif dikembangkan; gunakan `hive_ce` jika memilih Hive.

### Audio & Haptics
- `AudioService` membungkus `audioplayers`; preload SFX di awal; hormati setting mute.
- Haptics lewat `HapticFeedback.lightImpact()` dll.

## Perintah

| Tujuan | Perintah |
| --- | --- |
| Setup | `flutter create --org com.<org> --project-name <nama> --platforms android,ios .` lalu `flutter pub get` |
| Run dev | `flutter run --flavor dev -t lib/main_dev.dart` |
| Lint / analyze | `flutter analyze` |
| Format | `dart format .` |
| Test core | `flutter test test/core` |
| Test semua | `flutter test` |
| Sinkron konten | `python tools/validate.py && python tools/sync_content.py` |
| Build release Android | `flutter build appbundle --flavor prod -t lib/main_prod.dart` |

Flavor Android dikonfigurasi di `android/app/build.gradle(.kts)` (`productFlavors dev/prod` dengan `applicationIdSuffix ".dev"` untuk dev).

## Build & Rilis

- Signing: `android/key.properties` + keystore di luar repo (keduanya di .gitignore).
- Naikkan `version: x.y.z+build` di `pubspec.yaml`.
- Cek `minSdk` memenuhi syarat plugin iklan/firebase versi terpasang.

## .gitignore

```
.dart_tool/
build/
.flutter-plugins
.flutter-plugins-dependencies
*.iml
android/key.properties
android/app/*.jks
android/app/*.keystore
ios/Pods/
```

## Gotcha

- App crash saat start setelah menambah `google_mobile_ads`: hampir selalu App ID belum ada di Manifest/Info.plist.
- Riverpod: sintaks code-gen (`@riverpod`) vs manual berbeda, dan v3 mengubah beberapa API. Pilih satu gaya, catat di library-docs, jangan campur.
- `flutter_lints` aktif: jangan menonaktifkan rule untuk menyembunyikan warning tanpa alasan tertulis.
- Hot reload tidak menjalankan ulang `main()`/init services; gunakan hot restart setelah mengubah bootstrap.
- Font kustom: daftarkan di `pubspec.yaml` dan gunakan nama family yang sama persis.
- Animasi berat di grid besar: gunakan `RepaintBoundary` dan hindari rebuild seluruh grid saat satu sel berubah.

## Catatan Kerja Claude Code

- Semua bisa dikerjakan dari CLI: create, edit, analyze, test, build.
- User perlu: menjalankan di emulator/perangkat untuk verifikasi visual, membuat akun AdMob/Firebase, menjalankan `flutterfire configure` (butuh login), dan menyimpan keystore.

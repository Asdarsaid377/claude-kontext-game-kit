# Stack: Unity 6

> Profil stack. Disalin ke `context/stack.md` oleh `/choose-stack`.
> **Diaktifkan:** (tanggal, diisi /choose-stack)

---

## Kapan Cocok / Tidak Cocok

- **Cocok:** 3D atau 2D kompleks, hyper-casual 3D, game yang butuh SDK pihak ketiga terlengkap (iklan, mediasi, attribution), asset store besar.
- **Tidak cocok:** game UI/grid sederhana yang ingin APK kecil dan iterasi cepat dari CLI; developer yang belum siap dengan editor berat dan aturan lisensi Unity.

## Stack

| Layer | Tool | Versi |
| --- | --- | --- |
| Engine | Unity 6 (versi LTS terbaru) | (diisi /choose-stack) |
| Bahasa | C# | ikut engine |
| Render pipeline | URP | |
| UI | uGUI (Canvas) atau UI Toolkit, pilih satu dan catat | |
| Input | Input System package | |
| Test | Unity Test Framework (EditMode untuk core, PlayMode untuk integrasi) | |
| Iklan | Google Mobile Ads Unity Plugin (resmi) atau Unity LevelPlay, pilih satu | |
| Dependency Android | External Dependency Manager for Unity (EDM4U, ikut plugin Google) | |
| Analytics & crash | Firebase Unity SDK atau Unity Analytics/Cloud Diagnostics | |
| Storage | JSON (`JsonUtility` / Newtonsoft) di `Application.persistentDataPath` | |
| Async/tween | (opsional) DOTween / UniTask, hanya jika disetujui | |

## Mapping ke Arsitektur

| Konsep | Lokasi |
| --- | --- |
| Core | `Assets/_Game/Scripts/Core/` dengan `Game.Core.asmdef` (**noEngineReferences: true**) |
| Game State / Controller | `Assets/_Game/Scripts/Controllers/` |
| Presentation | `Assets/_Game/Scripts/Presentation/` (MonoBehaviour), `Assets/_Game/Scenes/`, `Assets/_Game/Prefabs/` |
| Services (interface) | `Assets/_Game/Scripts/Services/` (interface C#) |
| Services (implementasi) | `Assets/_Game/Scripts/Services/Impl/` dan `Services/Fake/` |
| Config (ekonomi, iklan) | ScriptableObject `EconomyConfig`, `AdsConfig` di `Assets/_Game/Config/` |
| UI tokens | ScriptableObject `UITokens` di `Assets/_Game/Config/` + `Scripts/Presentation/UI/Tokens.cs` |
| Test core | `Assets/_Game/Tests/EditMode/` dengan asmdef test yang mereferensikan `Game.Core` |

## Struktur Folder

```
<root>/
├── Assets/
│   ├── _Game/                     → semua milik project (underscore agar di atas)
│   │   ├── Scenes/                → Boot.unity, MainMenu.unity, Gameplay.unity
│   │   ├── Scripts/
│   │   │   ├── Core/              → Game.Core.asmdef (tanpa UnityEngine)
│   │   │   ├── Controllers/
│   │   │   ├── Presentation/{UI,Gameplay}/
│   │   │   └── Services/{Impl,Fake}/
│   │   ├── Prefabs/
│   │   ├── Config/                → ScriptableObject asset
│   │   ├── Art/{Sprites,UI,Fonts}/
│   │   ├── Audio/{Music,SFX}/
│   │   ├── StreamingAssets/ atau Resources/Content/ → konten JSON
│   │   └── Tests/{EditMode,PlayMode}/
│   └── Plugins/                   → SDK pihak ketiga (jangan diedit)
├── Packages/manifest.json
└── ProjectSettings/
```

## Konvensi

- Class, method, property: `PascalCase`. Field privat: `_camelCase`. Parameter/lokal: `camelCase`.
- Satu class publik per file, nama file = nama class.
- Namespace: `Game.Core`, `Game.Controllers`, `Game.Presentation`, `Game.Services`.
- `Game.Core` asmdef **tidak boleh** mereferensikan UnityEngine (setting `noEngineReferences`). Ini menjamin core bisa di-test di EditMode tanpa scene.
- MonoBehaviour tipis: ambil input, panggil controller, tampilkan state.
- `[SerializeField] private` untuk field yang di-set di Inspector, bukan `public`.
- Jangan pakai `GameObject.Find` / `FindObjectOfType` di runtime loop. Referensi lewat Inspector atau injeksi di Boot scene.
- Hindari `Update()` jika bisa event-driven.

## UI & Token

- ScriptableObject `UITokens` berisi warna, ukuran font, spacing, durasi dari `context/ui-tokens.md`. Komponen UI membaca dari sini.
- Canvas Scaler: Scale With Screen Size, reference resolution sesuai `ui-rules.md`, match 0.5 (atau sesuai orientasi).
- Safe area: komponen `SafeAreaFitter` yang membaca `Screen.safeArea`.
- Teks dengan TextMeshPro; font asset dibuat dari font yang lisensinya tercatat.

## Konten

- `tools/sync_content.py` menyalin `content/build/` ke `Assets/_Game/StreamingAssets/Content/` (atau `Resources/Content/`, pilih satu).
- Android: `StreamingAssets` ada di dalam APK; baca dengan `UnityWebRequest`, bukan `File.ReadAllText`. `Resources.Load<TextAsset>` lebih sederhana untuk konten kecil.

## Services

### Iklan
- Google Mobile Ads Unity Plugin: App ID diisi di Settings plugin (menu Google Mobile Ads). Tanpa App ID, build Android gagal/crash.
- Consent UMP disediakan plugin; jalankan sebelum load iklan.
- Setelah import plugin, jalankan **Android Resolver** (EDM4U) agar dependensi Gradle lengkap.
- Callback iklan bisa datang di thread non-main: pindahkan ke main thread sebelum menyentuh UI (cek opsi di versi plugin terpasang).

### Analytics & Crash
- Firebase Unity SDK: import package yang dibutuhkan saja (Analytics, Crashlytics). File `google-services.json` di `Assets/`.

### Storage / Save
- `Application.persistentDataPath/save.json` ber-`saveVersion`. Tulis ke file temp lalu replace.
- Simpan di `OnApplicationPause(true)`; jangan mengandalkan `OnApplicationQuit` di mobile.

### Audio & Haptics
- `AudioMixer` dengan group Music & SFX; volume lewat exposed parameter.
- Getar sederhana: `Handheld.Vibrate()` (kasar); haptic halus butuh plugin native.

## Perintah

Ganti `<Unity>` dengan path editor (contoh macOS: `/Applications/Unity/Hub/Editor/<versi>/Unity.app/Contents/MacOS/Unity`).

| Tujuan | Perintah |
| --- | --- |
| Setup | User membuat project dari Unity Hub (template 2D/3D URP Mobile), lalu Claude Code membuat struktur folder, asmdef, dan script |
| Run dev | Play mode di editor (user) |
| Test core (EditMode) | `<Unity> -batchmode -nographics -projectPath . -runTests -testPlatform EditMode -testResults ./TestResults/editmode.xml -logFile -` |
| Test PlayMode | sama dengan `-testPlatform PlayMode` |
| Sinkron konten | `python tools/validate.py && python tools/sync_content.py` |
| Build release Android | `<Unity> -batchmode -quit -projectPath . -executeMethod Game.Editor.BuildScript.BuildAndroidRelease -logFile -` (script build dibuat di feature 01) |

Catatan: batchmode gagal jika project yang sama sedang terbuka di editor.

## Build & Rilis

- Player Settings: package name, version, bundle version code, minimum & target API, IL2CPP + ARM64 (wajib untuk Play Store).
- Keystore di luar repo; password diisi saat build (env var di BuildScript), bukan di ProjectSettings yang di-commit.
- Build AAB: aktifkan "Build App Bundle (Google Play)".

## .gitignore

```
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/
[Ll]ogs/
[Uu]ser[Ss]ettings/
TestResults/
*.csproj
*.sln
*.keystore
*.jks
```

## Gotcha

- **File `.meta` wajib di-commit** dan dipindah bersama file aslinya. Memindah file di luar editor tanpa .meta merusak referensi.
- Asset Serialization harus **Force Text** (Project Settings > Editor) agar scene/prefab bisa di-diff.
- Jangan mengedit `.unity`/`.prefab` YAML secara manual kecuali perubahan sangat kecil dan disetujui user.
- Script compile error membuat seluruh project tidak bisa Play; selalu cek Console/log setelah perubahan.
- API lama vs baru: Input Manager lama vs Input System; `FindObjectOfType` deprecated di versi baru (ganti `FindFirstObjectByType`/`FindAnyObjectByType`). Verifikasi API dengan versi terpasang.
- Lisensi Unity dan aturan biaya runtime berubah beberapa kali; cek ketentuan terbaru sebelum rilis komersial.

## Catatan Kerja Claude Code

- Bisa dari CLI: semua script C#, asmdef, ScriptableObject class, test EditMode lewat batchmode, BuildScript.
- User perlu: membuat project di Unity Hub, menyusun scene/prefab dan menghubungkan referensi di Inspector, membuat asset ScriptableObject di editor, import SDK, menjalankan Android Resolver, dan Play/verifikasi visual. Claude Code harus menyebutkan langkah editor ini secara eksplisit di akhir setiap feature.

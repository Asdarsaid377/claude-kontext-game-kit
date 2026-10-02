# Stack: Phaser + Vite + Capacitor

> Profil stack. Disalin ke `context/stack.md` oleh `/choose-stack`.
> **Diaktifkan:** (tanggal, diisi /choose-stack)

---

## Kapan Cocok / Tidak Cocok

- **Cocok:** game 2D yang ingin dimainkan di **browser dan** sebagai APK dari satu codebase; prototipe cepat; developer web (TypeScript); game kasual, puzzle, arcade ringan; rilis ke portal web game.
- **Tidak cocok:** 3D, game berat dengan ratusan sprite + fisika kompleks di HP low-end (WebView lebih lambat dari native), game yang butuh SDK native yang tidak punya plugin Capacitor.

## Stack

| Layer | Tool | Versi |
| --- | --- | --- |
| Game framework | Phaser | (diisi /choose-stack; **cek mayor**, API v3 dan v4 berbeda) |
| Bundler | Vite | |
| Bahasa | TypeScript (strict) | |
| Native wrapper | Capacitor (Android, iOS) | |
| Iklan (APK) | `@capacitor-community/admob` (komunitas) | cek kompatibilitas dengan versi Capacitor |
| Iklan (web) | AdMob tidak tersedia di web; gunakan H5 Games Ads (AdSense) atau SDK portal (mis. CrazyGames/Poki) | |
| Analytics | Firebase JS SDK (web) / plugin Capacitor Firebase (native) | |
| Storage | `@capacitor/preferences` (native) dengan fallback `localStorage` (web) di balik `StorageService` | |
| Haptics | `@capacitor/haptics` | |
| Test | Vitest | |
| Lint/format | ESLint + Prettier | |

## Mapping ke Arsitektur

| Konsep | Lokasi |
| --- | --- |
| Core | `src/core/` (TypeScript murni, tanpa import `phaser` atau `@capacitor/*`) |
| Game State / Controller | `src/state/` |
| Presentation | `src/scenes/` (Phaser Scene), `src/objects/` (GameObject kustom), `src/ui/` |
| Services (interface) | `src/services/types.ts` |
| Services (implementasi) | `src/services/native/`, `src/services/web/`, `src/services/fake/` |
| Config (ekonomi, iklan) | `src/config/economy.ts`, `src/config/ads.ts`, env via `import.meta.env` |
| UI tokens | `src/ui/tokens.ts` |
| Test core | `src/core/**/*.test.ts` |

## Struktur Folder

```
<root>/
├── index.html
├── vite.config.ts
├── capacitor.config.ts
├── public/
│   ├── content/               → hasil salin dari content/build/
│   └── assets/{images,audio,fonts}/
├── src/
│   ├── main.ts                → buat Phaser.Game + bootstrap services
│   ├── core/                  → PURE: aturan main, generator, parser konten
│   ├── state/
│   ├── scenes/                → BootScene, PreloadScene, MenuScene, GameScene, UIScene
│   ├── objects/
│   ├── ui/                    → tokens.ts, Button, Popup
│   ├── services/{native,web,fake}/
│   └── config/
├── android/  ios/             → dibuat Capacitor (commit, kecuali folder build)
└── package.json
```

## Konvensi

- TypeScript strict, tanpa `any` (pakai `unknown` lalu narrow).
- File: `PascalCase.ts` untuk class (Scene, GameObject), `camelCase.ts` untuk fungsi/util.
- Named export, tanpa default export (kecuali config tool yang mewajibkan).
- `src/core/` tidak boleh import `phaser` atau `@capacitor/*`. Cek dengan grep sebelum menyelesaikan feature.
- Satu Scene = satu tanggung jawab. HUD di `UIScene` paralel agar tidak ikut kamera gameplay.
- Bersihkan listener/timer di event `shutdown` Scene untuk mencegah memory leak.
- Platform check (`Capacitor.isNativePlatform()`) hanya di `bootstrap`/factory services, bukan tersebar di scene.

## UI & Token

- `src/ui/tokens.ts` mengekspor objek `const` dari `context/ui-tokens.md` (warna sebagai number `0xRRGGBB` untuk Phaser dan string `#RRGGBB` untuk teks).
- Scale Manager: `mode: Phaser.Scale.FIT` (atau `RESIZE` jika layout responsif), `autoCenter: CENTER_BOTH`, resolusi dasar sesuai `ui-rules.md`.
- Teks tajam di layar high-DPI: atur resolusi teks sesuai `devicePixelRatio` atau gunakan bitmap font.
- Safe area: CSS `env(safe-area-inset-*)` di container + `viewport-fit=cover` di meta viewport.
- Font web: preload sebelum membuat Text (gunakan loader font atau `document.fonts.load`), kalau tidak teks pertama memakai font fallback.

## Konten

- `tools/sync_content.py` menyalin `content/build/` ke `public/content/`.
- Muat di `PreloadScene` dengan `this.load.json(key, 'content/...')`, lalu parse/validasi di core.

## Services

### Iklan
- APK: `@capacitor-community/admob`. App ID di `AndroidManifest.xml` (`com.google.android.gms.ads.APPLICATION_ID`). Plugin menyediakan API consent; jalankan sebelum load iklan.
- Web: AdMob tidak bisa. Implementasi `WebAdsService` sesuai platform web yang dipilih, atau `FakeAds` (tanpa iklan) untuk build web.
- Pause game loop dan audio saat iklan tampil; resume setelah ditutup.

### Analytics & Crash
- Web: Firebase JS SDK. Native: plugin Capacitor Firebase. Keduanya di balik `AnalyticsService`.

### Storage / Save
- `StorageService` native memakai `@capacitor/preferences`, web memakai `localStorage` dalam try/catch. Save satu dokumen JSON ber-`saveVersion`.

### Audio & Haptics
- Browser memblokir audio sebelum interaksi pertama: mulai musik setelah tap pertama (Phaser menangani unlock, tetapi musik autoplay di Boot tetap harus menunggu).
- Pause audio saat app ke background (`@capacitor/app` event `appStateChange` / `visibilitychange`).
- Haptics lewat `@capacitor/haptics`, no-op di web.

## Perintah

| Tujuan | Perintah |
| --- | --- |
| Setup | `npm create vite@latest . -- --template vanilla-ts`, `npm i phaser`, `npm i @capacitor/core && npm i -D @capacitor/cli`, `npx cap init` |
| Run dev (browser) | `npm run dev` |
| Lint | `npm run lint` |
| Typecheck | `npx tsc --noEmit` |
| Test core | `npx vitest run src/core` |
| Sinkron konten | `python tools/validate.py && python tools/sync_content.py` |
| Build web | `npm run build` (output `dist/`) |
| Sinkron ke native | `npm run build && npx cap sync android` |
| Buka Android Studio | `npx cap open android` |
| Build release Android | dari Android Studio (Generate Signed Bundle) atau `cd android && ./gradlew bundleRelease` |

## Build & Rilis

- `webDir` di `capacitor.config.ts` = `dist`.
- **Setiap perubahan web harus `npm run build` + `npx cap sync`** sebelum dites di APK.
- Version code/name diatur di `android/app/build.gradle`.
- Keystore di luar repo.

## .gitignore

```
node_modules/
dist/
.env
.env.*
!.env.example
android/app/build/
android/.gradle/
android/build/
ios/App/Pods/
*.keystore
*.jks
```

## Gotcha

- Phaser v3 vs v4: banyak contoh online masih v3. Cek versi di `package.json` dan sesuaikan API; jangan campur.
- Contoh lama Phaser 2/CE (`game.state`, `Phaser.Game(...)` dengan banyak argumen) tidak berlaku.
- Lupa `cap sync`: APK masih memakai build web lama.
- Performa WebView di HP low-end: batasi jumlah objek, gunakan texture atlas, hindari Graphics yang digambar ulang tiap frame.
- `localStorage` bisa terhapus oleh sistem/browser; di native gunakan Preferences.
- Path asset harus relatif (tanpa `/` di depan) agar jalan di `file://`/WebView Capacitor dan subfolder web.

## Catatan Kerja Claude Code

- Bisa dari CLI: hampir semuanya (kode, test, build web, cap sync, gradle build).
- User perlu: menguji di browser dan perangkat, membuka Android Studio untuk signing/emulator jika diperlukan, membuat akun AdMob/Firebase.

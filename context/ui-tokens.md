# UI Tokens

Design tokens dalam format **netral engine**. Implementasinya di kode mengikuti bagian UI di `context/stack.md` (misalnya file `tokens.dart`, Theme resource Godot, ScriptableObject Unity, atau `tokens.ts`). Nilai di sini adalah sumber kebenaran; implementasi wajib sama.

> **TEMPLATE:** Ganti nilai dengan hasil ekstraksi dari `context/designs/`. Nama token dipertahankan agar konsisten antar project.

---

## Warna

| Token | Hex | Pemakaian |
| --- | --- | --- |
| `color.background` | `#F6F3EE` | background layar |
| `color.surface` | `#FFFFFF` | panel, kartu, popup |
| `color.primary` | `#2F6FED` | tombol utama, highlight |
| `color.primary_pressed` | `#2358C4` | tombol utama saat ditekan |
| `color.secondary` | `#F2A93B` | aksen, koin, hadiah |
| `color.success` | `#2FA36B` | jawaban benar |
| `color.danger` | `#E0504D` | salah, peringatan |
| `color.text_primary` | `#1D2433` | teks utama |
| `color.text_secondary` | `#5B6475` | teks pendukung |
| `color.text_on_primary` | `#FFFFFF` | teks di atas primary |
| `color.border` | `#E3DED6` | garis, pemisah |
| `color.overlay` | `#000000` @ 50% | latar popup |

## Tipografi

| Token | Ukuran (sp/px @1080w) | Weight | Pemakaian |
| --- | --- | --- | --- |
| `font.family` | `[ISI]` | | font utama |
| `text.display` | 40 | Bold | judul layar, skor besar |
| `text.title` | 28 | Bold | judul popup |
| `text.body` | 18 | Regular | teks isi |
| `text.caption` | 14 | Medium | label kecil |
| `text.button` | 20 | Bold | label tombol |

## Spacing

| Token | Nilai |
| --- | --- |
| `space.xs` | 4 |
| `space.sm` | 8 |
| `space.md` | 16 |
| `space.lg` | 24 |
| `space.xl` | 32 |

## Radius

| Token | Nilai |
| --- | --- |
| `radius.sm` | 8 |
| `radius.md` | 16 |
| `radius.lg` | 24 |
| `radius.pill` | 999 |

## Motion

| Token | Nilai |
| --- | --- |
| `motion.fast` | 120 ms |
| `motion.normal` | 250 ms |
| `motion.slow` | 400 ms |
| `motion.press_scale` | 0.95 |

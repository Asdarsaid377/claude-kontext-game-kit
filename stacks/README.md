# Stacks: Profil Engine/Framework

Setiap file di folder ini adalah **profil stack** yang lengkap dan mandiri: kapan cocok, versi, struktur folder, konvensi, cara implementasi token UI, plugin iklan/analytics/storage, perintah build/test, dan gotcha.

Profil **tidak dibaca langsung** saat coding. Jalankan `/choose-stack <id>` untuk menyalin profil ke `context/stack.md`. Salinan itulah yang dipakai dan boleh disesuaikan per project. Profil di folder ini tetap sebagai template bersih.

---

## Profil Tersedia

| id | Stack | Bahasa | Paling cocok untuk |
| --- | --- | --- | --- |
| `flutter` | Flutter (+ Flame opsional) | Dart | Game berbasis UI/grid: TTS, cari kata, kuis, trivia, kartu, idle/clicker sederhana, merge ringan |
| `godot` | Godot 4 | GDScript (typed) | 2D arcade, platformer, puzzle fisika, top-down, game dengan banyak scene/animasi; open source, ringan |
| `unity` | Unity 6 | C# | 2D/3D lebih kompleks, hyper-casual 3D, game yang butuh ekosistem SDK & asset store terbesar |
| `phaser-capacitor` | Phaser + Vite + Capacitor | TypeScript | Game 2D yang ingin main di browser **dan** di-bundle jadi APK; prototipe cepat; portal web game |

---

## Matriks Pemilihan

| Kebutuhan | flutter | godot | unity | phaser-capacitor |
| --- | :-: | :-: | :-: | :-: |
| UI/grid/teks banyak | ★★★ | ★★ | ★★ | ★★ |
| Fisika & sprite animasi | ★ (Flame: ★★) | ★★★ | ★★★ | ★★ |
| 3D | ✗ | ★★ | ★★★ | ✗ |
| Ukuran APK kecil | ★★ | ★★ | ★ | ★★ |
| Plugin iklan resmi Google | ✓ resmi | komunitas | ✓ resmi | komunitas |
| Bisa jalan di browser | ★ | ★★ | ★ | ★★★ |
| Claude Code bisa kerja penuh dari CLI | ★★★ | ★★ | ★ | ★★★ |
| Kurva belajar (dev web/app) | rendah | sedang | sedang-tinggi | rendah |

Catatan baris "Claude Code bisa kerja penuh dari CLI": Unity dan Godot punya editor visual; scene/prefab lebih aman dibuat di editor oleh user, sementara Claude Code fokus di script dan test. Detail di bagian *Catatan Kerja Claude Code* tiap profil.

---

## Aturan Rekomendasi (dipakai `/plan-game` dan `/choose-stack`)

1. Game didominasi UI, teks, grid, tanpa fisika → `flutter`
2. Game 2D dengan fisika, banyak sprite bergerak, atau level berbasis scene → `godot`
3. Butuh 3D, atau SDK pihak ketiga yang hanya ada untuk Unity → `unity`
4. Wajib main di browser / portal web, atau ingin satu codebase web + APK → `phaser-capacitor`
5. Seimbang antara dua pilihan: pilih yang paling dikuasai user, lalu yang paling bisa dikerjakan Claude Code dari CLI.

---

## Menambah Profil Baru

Salin `_TEMPLATE.md` ke `stacks/<id>.md`, isi semua bagian, lalu tambahkan baris di tabel atas. Jangan menghapus bagian dari template: jika tidak relevan, tulis "tidak relevan untuk stack ini" beserta alasannya.

---

## Pindah Stack di Tengah Project

Bisa, tapi mahal. Yang terbawa: `context/` (kecuali stack.md), `content/`, `tools/`, `assets-src/`, dan logika core sebagai **spesifikasi + daftar test case**. Yang ditulis ulang: core di bahasa baru (test case jadi acuan), presentation, services, build config. `/choose-stack` akan berhenti dan minta konfirmasi jika stack sudah aktif dan kode sudah ada.

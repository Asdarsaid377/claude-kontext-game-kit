# Analytics

Daftar event resmi. Event yang dikirim kode harus ada di sini; event baru ditambahkan ke tabel ini di sesi yang sama.

---

## Aturan

- Nama event dan parameter: `snake_case`, bahasa Inggris.
- Kirim lewat `AnalyticsService`, tidak memanggil SDK langsung dari scene/widget.
- Jangan mengirim data pribadi (nama, email, teks bebas dari pemain).
- Build dev mengirim ke mode debug penyedia analytics.

---

## Penyedia

`[ISI]` (contoh: Firebase Analytics + Crashlytics). Detail plugin di `context/stack.md`.

---

## Event

| Event | Parameter | Kapan |
| --- | --- | --- |
| `level_start` | `mode`, `level_id` | Level dimulai |
| `level_complete` | `mode`, `level_id`, `stars`, `duration_sec` | Level selesai |
| `level_fail` | `mode`, `level_id`, `reason` | Kalah (jika ada) |
| `level_quit` | `mode`, `level_id`, `progress_pct` | Keluar sebelum selesai |
| `ad_shown` | `format`, `placement` | Iklan tampil |
| `ad_reward_earned` | `placement`, `amount` | Rewarded selesai ditonton |
| `currency_earned` | `source`, `amount` | Dapat mata uang |
| `currency_spent` | `item`, `amount` | Pakai mata uang |
| `[ISI]` | `[ISI]` | `[ISI]` |

---

## KPI yang Dipantau

`[ISI]` (contoh: retensi D1/D7, rata-rata level per sesi, ARPDAU, crash-free users, titik level dengan quit tertinggi).

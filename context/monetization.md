# Monetization

Aturan iklan dan pembelian dalam game. Angka di file ini adalah **sumber kebenaran**; file config di kode wajib sama.

---

## Prinsip

1. Iklan tidak pernah memotong gameplay yang sedang berlangsung.
2. Rewarded = pilihan pemain, selalu jelas apa hadiahnya.
3. Gagal memuat iklan = game tetap berjalan normal tanpa pesan error teknis.
4. **Build dev selalu memakai test ad unit ID** resmi dari penyedia iklan. ID produksi hanya di build release dan tidak di-hardcode di kode (lewat config build/flavor).
5. Consent (GDPR/UMP atau setara) dijalankan sebelum iklan pertama dimuat.
6. Jika target pemain mencakup anak-anak, aturan iklan khusus berlaku. Konfirmasi ke user sebelum mengimplementasi.

---

## Penyedia

| Item | Nilai |
| --- | --- |
| Ad network utama | `[ISI]` (contoh: Google AdMob) |
| Mediasi | `[ISI]` (contoh: belum di MVP) |
| Plugin/SDK di stack aktif | lihat `context/stack.md` bagian Iklan |
| App ID | disimpan di config build, bukan di file ini |

---

## Placement

> **TEMPLATE:** Isi per project.

| Placement | Format | Kapan tampil | Aturan |
| --- | --- | --- | --- |
| `[ISI]` | Banner | `[ISI]` (contoh: menu & pemilihan level) | Tidak di layar gameplay |
| `[ISI]` | Interstitial | `[ISI]` (contoh: setelah tiap N level) | Jeda minimal `[ISI]` detik; tidak di N level pertama pemain baru |
| `[ISI]` | Rewarded | `[ISI]` (contoh: tukar hint/koin) | Maks `[ISI]` per hari |

---

## In-App Purchase

| Produk | Tipe | Harga | Fase |
| --- | --- | --- | --- |
| `[ISI]` (contoh: remove_ads) | non-consumable | `[ISI]` | `[ISI]` |

- Pembelian non-consumable wajib punya tombol **Restore** (wajib di iOS).
- "Hapus iklan" menghapus banner dan interstitial; rewarded tetap tersedia karena itu pilihan pemain.

---

## Legal

- Privacy Policy wajib (URL publik) karena memakai SDK iklan/analytics: `[ISI URL]`
- Isi form Data Safety (Play) / App Privacy (App Store) sesuai SDK yang dipakai.
- Jika memakai AdMob: siapkan `app-ads.txt` di domain developer yang tercantum di store listing.

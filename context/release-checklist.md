# Release Checklist

Dipakai oleh `/release-check`. Kebijakan store berubah dari waktu ke waktu; item bertanda (cek konsol) harus diverifikasi user langsung di Play Console / App Store Connect.

---

## Build

- [ ] Versi (version name) dan build number naik
- [ ] Build release memakai ad unit ID produksi; build dev memakai test ID
- [ ] Menu/flag debug dan cheat mati
- [ ] Log verbose dimatikan di release
- [ ] Keystore/sertifikat signing tersimpan aman di luar repo dan ada backup-nya
- [ ] Format AAB untuk Play Store
- [ ] Target API level memenuhi syarat terbaru (cek konsol)
- [ ] Ukuran unduhan sesuai target di game-overview.md

## Kualitas

- [ ] Semua unit test core lulus
- [ ] `tools/validate.py` lulus untuk semua konten
- [ ] Diuji di perangkat minimum dan satu perangkat layar panjang/notch
- [ ] Save data dari versi sebelumnya (jika ada) termigrasi dengan benar
- [ ] Tidak ada crash di alur utama; crash reporting aktif

## Iklan & Privasi

- [ ] Consent iklan tampil di wilayah yang mewajibkan
- [ ] Frekuensi iklan sesuai `monetization.md`
- [ ] Privacy Policy URL aktif dan tercantum di store
- [ ] Data Safety / App Privacy diisi sesuai SDK yang dipakai (cek konsol)
- [ ] `app-ads.txt` terpasang di domain developer (jika AdMob)
- [ ] Rating konten (kuesioner IARC) diisi; target usia sesuai game-overview.md

## Asset & Legal

- [ ] Semua asset tercatat di `assets.md` dengan lisensi jelas
- [ ] Atribusi wajib tercantum di layar Kredit
- [ ] Ikon, feature graphic, screenshot siap

## Store Listing

- [ ] Judul dan deskripsi memuat keyword utama (ASO)
- [ ] Screenshot menunjukkan gameplay inti di 2-3 gambar pertama
- [ ] Kategori dan tag benar

## Google Play: Akun Baru

- [ ] Akun developer personal baru: closed testing dengan jumlah tester dan durasi minimum sebelum boleh rilis produksi (cek konsol untuk angka terbaru)

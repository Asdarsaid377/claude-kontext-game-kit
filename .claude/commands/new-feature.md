---
description: Kerjakan satu feature dari build-plan sampai tuntas
---

Feature yang dikerjakan: $ARGUMENTS (jika kosong, ambil item "Berikutnya" dari progress-tracker)

Workflow:

1. Baca `context/progress-tracker.md` dan `context/stack.md`. Jika stack belum dipilih, BERHENTI.
2. Baca definisi feature di `context/build-plan.md`. Scope feature ini adalah batas kerjamu.
3. Baca context yang relevan (UI, konten, monetisasi, analytics, assets).
4. Sampaikan rencana singkat: file apa yang dibuat/diubah per layer (core / presentation / services / content), dan cara verifikasinya. Lanjut setelah rencana jelas.
5. Urutan implementasi:
   a. **Core logic + unit test** dulu (jika feature punya aturan main). Jalankan test sampai lulus.
   b. **UI / scene** dengan data mock, lewat workflow `/build-ui` (referensi desain wajib).
   c. **Wiring** core ke presentation dan services.
   d. Edge case: loading, gagal muat iklan, tidak ada koneksi, save data kosong/rusak, app di-background lalu dibuka lagi.
6. Jika feature mengubah format data level/konten: jalankan workflow `/content-change`.
7. Jika feature menambah asset: jalankan workflow `/add-asset`.
8. Jalankan perintah lint/analyze dan test dari bagian Perintah di `stack.md`. Laporkan hasilnya apa adanya, jangan sembunyikan kegagalan.
9. Berikan langkah verifikasi eksplisit untuk user (atau jalankan `/playtest`).
10. Setelah user konfirmasi feature bekerja: update dokumen hidup (`/update-context`) dan sarankan commit.

Jangan menyentuh feature berikutnya sebelum feature ini tuntas dan tracker ter-update.

---
description: Susun checklist uji main untuk feature yang baru selesai
---

Feature yang diuji: $ARGUMENTS (jika kosong, ambil "Terakhir selesai" dari progress-tracker)

Susun checklist uji yang bisa dijalankan user di perangkat/emulator, berdasarkan definisi feature di build-plan dan aturan di game-design:

1. **Happy path**: langkah demi langkah dari membuka game sampai feature terpakai, dengan hasil yang diharapkan di tiap langkah.
2. **Aturan main**: kasus menang, kalah, skor/bintang, hadiah, sesuai angka di game-design.
3. **Edge case**: keluar di tengah level lalu buka lagi, rotasi/ukuran layar kecil, tanpa internet, iklan gagal dimuat, tombol ditekan berkali-kali cepat, save data dari versi sebelumnya.
4. **Performa & rasa**: FPS terasa mulus, tidak ada jeda saat transisi, suara/getar sesuai setting.
5. **Analytics**: event yang seharusnya terkirim (cek di debug view sesuai analytics.md).

Format output: checklist markdown yang bisa dicentang. Jangan menandai feature selesai di tracker sebelum user melaporkan hasil uji.

# UI Rules (Game)

Aturan visual dan interaksi UI. Desain di `context/designs/` tetap menang; file ini menutup pola penting agar konsisten tanpa harus menspesifikasikan semua detail.

> **TEMPLATE:** Bagian `[SESUAIKAN]` diisi ulang per project setelah desain ada. Nilai contoh adalah default yang aman untuk game mobile casual.

---

## Layar & Resolusi

`[SESUAIKAN]`
- Orientasi: portrait
- Resolusi desain acuan: 1080 x 1920 (rasio 9:16), skala menyesuaikan lebar
- Hormati safe area (notch, punch-hole, gesture bar). Tidak ada tombol penting di 48 px tepi atas/bawah di luar safe area.
- Layar sangat panjang (20:9) dan tablet harus tetap terlihat rapi: konten utama di tengah, background meluas.

## Sentuhan & Input

- Target sentuh minimal **48 x 48 dp** (setara ~9 mm), jarak antar target minimal 8 dp.
- Setiap tombol punya state: normal, ditekan (scale 0.95 atau gelap sedikit), nonaktif.
- Respon visual/suara dalam < 100 ms setelah sentuhan.
- Cegah double tap pada tombol yang memicu aksi berat (beli, tonton iklan, lanjut level).
- Tombol back Android: tutup popup teratas, lalu kembali ke layar sebelumnya, lalu konfirmasi keluar dari menu utama.

## Tipografi

`[SESUAIKAN]`
- Font utama: `[ISI]` (lisensi tercatat di assets.md)
- Ukuran teks isi minimal 16 sp; teks gameplay penting (huruf di grid, skor) lebih besar
- Dukung setting ukuran font jika target pemain usia lanjut

## Hierarki Layar

- Satu aksi utama per layar, paling menonjol (tombol primer).
- HUD gameplay hanya informasi yang dibutuhkan saat main; sisanya di menu pause.
- Popup: overlay gelap di belakang, tombol tutup jelas, tidak menumpuk lebih dari satu level popup.

## Feedback & Animasi

`[SESUAIKAN]`
- Durasi transisi layar: 200-300 ms
- Feedback benar/salah: warna + suara + (opsional) getar ringan
- Animasi hadiah (koin, bintang) singkat dan bisa di-tap untuk dipercepat
- Hormati setting suara, musik, dan getar dari menu pengaturan

## Iklan & UI

- Banner tidak boleh menutupi elemen interaktif; sediakan ruang tetap untuknya.
- Tombol rewarded menyebut hadiahnya: "Tonton iklan +30 koin".

## State Khusus

- Loading: indikator jelas jika > 300 ms
- Kosong / terkunci: tampilkan alasan dan cara membuka
- Offline: fitur yang butuh internet menampilkan pesan ramah, fitur lain tetap jalan

## Aksesibilitas

- Kontras teks minimal 4.5:1
- Informasi tidak hanya dibedakan lewat warna (tambah ikon/bentuk)

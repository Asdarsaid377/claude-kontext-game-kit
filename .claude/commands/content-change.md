---
description: Ubah format data level/konten, generator, dan validator secara aman
---

Perubahan yang diminta: $ARGUMENTS

Workflow:

1. Baca `context/content-pipeline.md` secara penuh.
2. Baca skema saat ini (`content/schema/`) dan contoh data yang ada.
3. Jelaskan perubahan skema dan dampaknya SEBELUM mengubah apapun: file data mana yang terdampak, apakah save data pemain ikut terdampak.
4. Jika perubahan tidak kompatibel: naikkan `schemaVersion`, tulis migrasi data (konten dan/atau save data), dan jangan menghapus dukungan versi lama tanpa konfirmasi.
5. Update berurutan: skema, generator di `tools/`, validator, parser di core (+ unit test), lalu regenerate data.
6. Jalankan validator untuk semua konten. Semua harus lulus.
7. Catat perubahan di `content-pipeline.md` bagian Changelog Skema dan di progress-tracker bagian Decisions.

Larangan: mengedit hasil generate secara manual tanpa mengubah sumbernya, menghapus file konten tanpa konfirmasi, mengubah format save tanpa migrasi.

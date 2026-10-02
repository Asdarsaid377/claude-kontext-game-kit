# Tools

Script Python yang dijalankan developer (bukan bagian dari game).

| Script | Fungsi |
| --- | --- |
| `validate.py` | Validasi `content/build/<jenis>/*.json` terhadap `content/schema/<jenis>.schema.json` + aturan bisnis |
| `sync_content.py` | Salin `content/build/` ke folder konten engine (`sync_config.json` → `dest`) |
| `gen_<jenis>.py` | Generator per jenis konten (dibuat per project, wajib menerima `--seed`) |

Setup: `pip install -r tools/requirements.txt`

# Aplikasi LMS - Django & PostgreSQL

Aplikasi LMS ini dibuat untuk tujuan pembelajaran backend sederhana dengan template minimal. Aplikasi ini mendukung Docker dan dilengkapi dengan Dockerfile serta docker-compose.yml.

## Cara Menjalankan di Docker Container

1. **Instal Docker** (jika belum), dan jalankan Docker.
2. **Unduh** dan ekstrak zip proyek ini ke komputer Anda.
3. **Ekstensi yang Disarankan** (gunakan VSCode):
   - Docker
   - PostgreSQL
4. Buka terminal di folder proyek dan jalankan perintah berikut:
```bash
docker-compose up -d --build
```
5. Jalankan perintah berikut untuk migrasi database:
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Jalankan server Django
```bash
python manage.py runserver 0.0.0.0:8000
```

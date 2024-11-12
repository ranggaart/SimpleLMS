# Aplikasi LMS - Django & PostgreSQL

Aplikasi LMS ini dirancang sebagai platform sederhana untuk mempelajari backend dengan menggunakan Django dan PostgreSQL. Dengan antarmuka minimalis, aplikasi ini menyediakan fitur dasar dan dapat dijalankan dalam lingkungan Docker. File Dockerfile dan `docker-compose.yml` sudah disiapkan untuk memudahkan pengaturan dan deployment di container.

## Cara Menjalankan di Docker Container

1. **Instal Docker** (jika belum terpasang), lalu pastikan Docker berjalan di sistem Anda.
2. **Unduh dan ekstrak proyek ini** ke dalam direktori di komputer Anda.
3. **Ekstensi yang Disarankan** (gunakan VSCode):
   - Docker
   - PostgreSQL
4. **Jalankan perintah berikut** di terminal pada direktori proyek:
   ```bash
   docker-compose up -d --build
   ```
5. **Lakukan migrasi database** dengan menjalankan perintah berikut:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Jalankan server Django** dengan perintah:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
   
Dengan langkah-langkah ini, aplikasi LMS berbasis Django dapat dijalankan dan diakses melalui Docker di sistem Anda.

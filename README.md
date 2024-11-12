**Aplikasi LMS - Django & PostgreSQL**

Aplikasi LMS ini dikembangkan sebagai sarana pembelajaran dasar backend dengan menggunakan Django serta PostgreSQL sebagai basis datanya. Dibuat dengan template sederhana, aplikasi ini cocok untuk mempelajari pengembangan backend secara praktis. Mendukung Docker, aplikasi ini dilengkapi dengan berkas Dockerfile dan `docker-compose.yml` agar lingkungan pengembangan dapat diatur dengan lebih mudah dan terisolasi.

**Cara Menjalankan di Docker Container**

1. Pastikan Docker sudah terinstal dan berjalan di perangkat Anda.
2. Unduh proyek ini dan ekstrak ke folder lokal.
3. Untuk pengalaman lebih baik, disarankan menggunakan Visual Studio Code (VSCode) dengan ekstensi berikut:
   - Docker
   - PostgreSQL
4. Buka terminal di direktori proyek, lalu jalankan perintah berikut untuk membangun dan menjalankan container:
   ```bash
   docker-compose up --build -d
   ```
5. Untuk mengatur database, jalankan migrasi dengan perintah:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Jalankan server Django dengan:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

Setelah langkah-langkah di atas selesai, aplikasi LMS akan tersedia dan siap diakses pada `http://localhost:8000`.

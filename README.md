# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Repositori ini milik Daffa Maulana Haekal (2106652083) untuk kebutuhan [Tugas2](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tugas/tugas-2) .
Aplikasi heroku : https://tugas2app.herokuapp.com/katalog/

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pertanyaan

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Django Framework 1](https://user-images.githubusercontent.com/112499670/190162369-f3c86957-6ac1-412b-a921-f25e9be336cb.png)


2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual enviroment (lingkungan virtual) digunakan untuk mengisolasi lingkungan Python yang digunakan pada suatu tempat/proyek dengan lingkungan Python lainnya, termasuk lingkungan Python global.

Jawab:
Kita akan tetap dapat membuat aplikasi Django tersebut walaupun tidak menggunakan virtual environment tetapi versi python dan libraries yang digunakan harus diperhatikan agar tidak bermasalah.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin-poin tersebut.
Jawab:

-Tambah aplikasi katalog pada INSTALLED_APPS.
-Buat file models.py dan tambah model yang digunakan sesuai dengan data yang ada.
-Jalankan python manage.py makemigrations sebagai persiapan migrasi DB dan python manage.py migrate untuk migrasi.
-Buat file views.py dan tambah fungsi untuk merespond sebuah permintaan. Lengkapi juga sehingga dapat memberikan data/context sesuai dengan data yang dimiliki.
-Ubah template di katalog.html agar dapat menunjukkan data yang telah diberikan dari context.
-Buat file urls.py di dalam folder aplikasi dan tambah fungsi dari views.py sebagai jawaban pada halaman indeks (/).
-Tambah urls.py sebelumnya ke dalam file urls.py di dalam folder proyek (project_django).
-Buat aplikasi baru di Heroku, dan dapatkan API key dan nama aplikasinya di sana.
-Tambah nama aplikasi dan api key ke dalam masing masing repository key
-Add, commit, dan push perubahan yang ada. Lalu github action akan mendeploy 

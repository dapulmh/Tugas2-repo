# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Repositori ini milik Daffa Maulana Haekal (2106652083) untuk kebutuhan [Tugas3](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tugas/tugas-3).

- Aplikasi heroku : https://tugas2app.herokuapp.com/todolist

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pertanyaan

1.  Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form> ?
  
{% csrf_token %} berguna untuk melindungi dari CSRF (Cross Site Request Forgery) Attack. Jika program dilakukan tanpa {% csrf_token %} maka akan 
terjadi error dikarenakan input yang diterima gagal diverifikasi.
  
2.   Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
     Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
 
Kita tetap dapat membuat form secara manual tanpa memanfaatkan generator. Caranya adalah dengan membuat elemen <form>, 
lalu mengisi form tersebut dengan elemen <input>. kemudian pastikan pula terdapat <input type="submit"> untuk meng-submit form tersebut. Halitu adalah hal yang saya 
lakukan pada kode create-task saya.
 
3.    Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, 
      hingga munculnya data yang telah disimpan pada template HTML.

Pada saat user mengisi data-data kemudian mengklik tombol submit maka data-data tersebut akan diperiksa. Jika data yang dimasukkan tidak valid maka user akan diarahkan untuk mengisi kembali form dengan data yang berbeda sampai data tersebut valid.
Kemudian data tersebut akan diproses, misalnya dengan membuat model sesuai dengan data yang diperoleh dan lalu data tersebut akan dimasukkan ke database. Ketika data tersebut dibutuhkan, maka model pada databse akan ditayangkan pada template html

4.    Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Tambah aplikasi todolist pada INSTALLED_APPS.

- Buat file models.py dan tambah model yang digunakan sesuai dengan data yang ada.

- Jalankan python manage.py makemigrations sebagai persiapan migrasi dan python manage.py migrate untuk migrasi.

- Buat file views.py dan tambah fungsi untuk merespond sebuah permintaan. Lengkapi juga sehingga dapat memberikan data/context sesuai dengan data yang dimiliki. 
  buat juga fungsi mengenai show_todolist, login_user, registrasi, create_task untuk kebutuhan website

- Buat todolist.html untuk halaman utama todolist beserta widget-widgetnya.

- Buat login.html untuk login ke todolist sesuai user beserta widget-widgetnya.
  
- Buat registrasi.html untuk halaman registrasi todolist beserta widget-widgetnya.
  
- Buat create-task.html untuk halaman create-task todolist beserta widget-widgetnya.

- Restriksi halaman todolist dan create-task ke login
  
- Buat forms.py yang berisi title dan description untuk menyimpan value create-task
  
- Buat cookies di views.py
  
- Buat file urls.py di dalam folder aplikasi dan tambah fungsi dari views.py sebagai jawaban pada halaman indeks (/).

- Tambah urls.py sebelumnya ke dalam file urls.py di dalam folder proyek (project_django).

- Buat fungsi bonus yaitu finish_user dan delete untuk mengganti status dan mendelete task

- Buat aplikasi baru di Heroku, dan dapatkan API key dan nama aplikasinya di sana.

- Tambah nama aplikasi dan api key ke dalam masing masing repository key

- Add, commit, dan push perubahan yang ada. Lalu github action akan mendeploy

- Buat readme.md dan menjawab segala pertanyaan yang ada

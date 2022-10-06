# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Repositori ini milik Daffa Maulana Haekal (2106652083) untuk kebutuhan [Tugas5](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tugas/tugas-5)

- Aplikasi heroku : https://tugas2app.herokuapp.com/todolist

## Pertanyaan

1.   Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
  
### Internal CSS

Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
  
#### Kelebihan 
 
- Perubahan pada Internal CSS hanya berlaku pada satu halaman saja sehingga tidak mengganggu halaman lain.
- Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
- Class dan ID bisa digunakan oleh internal stylesheet.
 
#### Kekurangan
- Tidak efisien apabila Anda menggunakan CSS yang sama dalam beberapa file atau halaman website yang lain.
- Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website. 
  
### External CSS
  
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.
  
#### Kelebihan 
- Ukuran file HTML akan menjadi lebih kecil dan membuat struktur dari kode HTML jadi lebih rapi.
- Loading website menjadi lebih cepat.
- File CSS dapat digunakan di beberapa halaman website sekaligus. 

#### Kekurangan
  
-Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.
  
### Inline CSS
  
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

#### Kelebihan 
  
- Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
- Berguna untuk memperbaiki kode dengan cepat.
- Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
  
#### Kekurangan
  
- Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.
  
2.   Jelaskan tag HTML5 yang kamu ketahui !
 
Kita tetap dapat membuat form secara manual tanpa memanfaatkan generator. Caranya adalah dengan membuat elemen <form>, 
lalu mengisi form tersebut dengan elemen input. kemudian pastikan pula terdapat input type="submit" untuk meng-submit form tersebut. Hal itu adalah hal yang saya 
lakukan pada kode create-task saya.

3.    Jelaskan tipe-tipe CSS selector yang kamu ketahui !

#### 

4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas !

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

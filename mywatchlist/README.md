# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

Repositori ini milik Daffa Maulana Haekal (2106652083) untuk kebutuhan [Tugas3](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tugas/tugas-3).

- Aplikasi heroku (html) : https://tugas3app.herokuapp.com/mywatchlist/html 
- Aplikasi heroku (xml) : https://tugas3app.herokuapp.com/mywatchlist/xml 
- Aplikasi heroku (json) : https://tugas3app.herokuapp.com/mywatchlist/json

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pertanyaan

1. Jelaskan perbedaan antara JSON, XML, dan HTML!

JSON
- support array
- syntax relatif pendek 
- sering menggunakan API
- Dapat berkolaborasi dengan AJAX
- pengaksesan data dilakukan secara cepat
-eksistensi file json adalah .json
- Menyimpan elemen secara efisien tetapi sedikit berantakan

XML
- Tidak support array
- Memiliki ukuran data yang besar
- lambat dalam akses sebuah data jika terdapat request dari server
- eksistensi file xml adalah .xml
- menyimpan elemen secara terstruktur dan mudah dibaca baik bagi mesin dan orang awam

HTML
- eksistensi fie adalah .html
- sebagai interface utama dan latar depan suatu website
- merupakan representasi website berupa text dimana menampilkan segala sesuatu tentang text dan tampilan struktur website

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jawab:
Dikarenakan saat mendevelopment sebuah platform akan diperlukan bagian mengirim data suatu tumpukan (stack) ke tumpukan lainnya. Format data umum yang dikirim dapat berbentuk berbagai macam bentuknya seperti HTML, XML, dan JSON.

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Tambah aplikasi mywatchlist pada INSTALLED_APPS.

- Buat file models.py dan tambah model yang digunakan sesuai dengan data yang ada.

- Jalankan python manage.py makemigrations sebagai persiapan migrasi dan python manage.py migrate untuk migrasi.

- Buat file views.py dan tambah fungsi untuk merespond sebuah permintaan. Lengkapi juga sehingga dapat memberikan data/context sesuai dengan data yang dimiliki.

- Buat mywatchlist.html agar dapat menunjukkan data yang telah diberikan dari context.

- Buat inital_mywatchlist_data.json dengan berisi 10 data yang terkait

- Buat file urls.py di dalam folder aplikasi dan tambah fungsi dari views.py sebagai jawaban pada halaman indeks (/).

- Tambah urls.py sebelumnya ke dalam file urls.py di dalam folder proyek (project_django).

- Buat sebuah fitur penyajian data dalam bentuk html, json, dan xml

- Update isi dari Procfile

- Buat aplikasi baru di Heroku, dan dapatkan API key dan nama aplikasinya di sana.

- Tambah nama aplikasi dan api key ke dalam masing masing repository key

- Add, commit, dan push perubahan yang ada. Lalu github action akan mendeploy

- Buat readme.md dan menjawab segala pertanyaan yang ada

## Foto Postman

![foto_html](https://user-images.githubusercontent.com/112499670/191578994-11b0a14a-e8ee-4d8a-89ef-00500baac875.png)

![foto_xml](https://user-images.githubusercontent.com/112499670/191579136-778fed67-aacd-487f-af85-115f4bf290d9.png)

![foto_json](https://user-images.githubusercontent.com/112499670/191579208-de5351e3-5629-49c3-bc4a-d0e691ea8172.png)



# Tugas 6: Javascript dan AJAX

Repositori ini milik Daffa Maulana Haekal (2106652083) untuk kebutuhan [Tugas6](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tugas/tugas-6)

- Aplikasi heroku : https://tugas2app.herokuapp.com/todolist

## Pertanyaan

1.Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Jawab:
Perbedaan dari asynchronus dan synchronus programming adalah asynchronus merupakan non blocking architecture dan multi thread dimana program dapat berjalan secara pararel tanpa menunggu task sebelumnyasedangkan synchronus merupakan blocking architecture dan single theread. Maka dari itu asynchronus programming lebih cepat daripada synchronus dikarenakan ketidak harusannya menunggu task sebelumnya selesai.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Jawab:
Event driven programming adalam sebuah paradigma dalam programming dimana alur dari jalannya sebuah program didasarkan dari sebuah action event salah satunya adalah menekan button.
Event driven programming dalam javascript dan ajax digunakan untuk mengsinkronisasi pada saat pengerjaan beberapa task secara bersamaan dan menyederhanakan program sesimpel mungkin. Salah satu contoh penerapan dari event driven programming adalah pada saat kita mengisi form lalu menekan button submit
dalam website maka secara asynchronus webiste langsung menampilkan data tersebut.

3.Jelaskan penerapan asynchronous programming pada AJAX.

Jawab:
Penerapan asynchronus programming pada AJAX adalah membuat interaksi website menjadi tanpa atau kurang delay dikarenakan diterapkannya asynchronus yang membuat tidap perlu  melewati web server sehingga user dapat langsung berinteraksi dengan webpage. Jika menggunakan asynchronus programming maka segala proses yang di request oleh user akan dikerjakan di background webpage.


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Jawab:

- membuat show_json dan create_task_ajax dalam view.py 
- menambahkan path untuk add/ dan json/
- buat todolist_ajax.html untuk penerapan ajax
- membuat ajax get untuk mengambil dan menampilkan data
- memodifikasi button create task untuk diarahkan ke modal
- membuat modal dan membuat form dalam modal 
- Membuat view baru yang menyimpan isi form ke database dan me-return sebuah response dalam bentuk JSON.
- Membuat AJAX POST untuk menampilkan data baru secara asinkronus

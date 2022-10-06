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
  
2.    Jelaskan tipe-tipe CSS selector yang kamu ketahui !
  
Ada beberapa jenis *CSS selectors*. di antaranya adalah:<br>
1. __*CSS Element Selector*__<br>
Selektor elemen memilih elemen HTML berdasarkan nama.<br>
2. __*CSS Id Selector*__<br>
Selector id memilih atribut id dari elemen HTML untuk memilih elemen tertentu. Id selalu unik di dalam halaman sehingga dipilih untuk memilih satu elemen unik. Itu ditulis dengan karakter hash (#), diikuti oleh id elemen.
3. __*CSS Class Selector*__<br>
Selektor kelas memilih elemen HTML dengan atribut kelas tertentu. Digunakan dengan karakter titik. (simbol titik penuh) diikuti dengan nama kelas.<br>
4. __*CSS Universal Selector*__<br>
Selektor universal digunakan sebagai karakter wildcard. Ini memilih semua elemen pada halaman.<br>
5. __*CSS Group Selector*__<br>
Grouping selector digunakan untuk memilih semua elemen dengan definisi style yang sama. Grouping selector digunakan untuk meminimalkan kode. Koma digunakan untuk memisahkan setiap selektor dalam pengelompokan.<br>

3.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas !

1. Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai 
2.Membuat keempat halaman yang dikustomisasi menjadi responsive.__<br>

  
4. Jelaskan tag HTML5 yang kamu ketahui.

Berikut merupakan tag dalam HTML5 yang sering dipakai
1. __CSS dan JS__ <br>
 Untuk melampirkan file css dan javascript sebagai design dan agar website terlihat menarik<br>
 

2. __*Semantics*__<br>
 Di HTML5 kita memiliki struktur semantik seperti `<header>`, `<footer>`, dan <nav> untuk contoh kode seperti ini.<br>

3. __*Article* dan *Section*__<br>

 section tag digunakan untuk mendefinisikan elemen html seperti header dan footer dan lainnya.<br>

 article tag digunakan untuk mendefinisikan konten independen tertentu<br>
4. __*Input types, attributes and forms*__<br>
 input type dan attributes baru telah diperkenalkan di HTML 5<br>

5. __*HTML5 editable content*__ <br>
 HTML5 memiliki atribut baru, sekarang kita dapat mengedit konten dengan menambahkan atribut contenteditable ke dalamnya.<br>

6.  __*Local Storage*__<br>
 Dengan fungsi ini, pengguna dapat mengakses data secara lokal dalam browser web. Sebelum pengguna HTML5 menyimpan data di cookie dengan setiap permintaan server.<br>



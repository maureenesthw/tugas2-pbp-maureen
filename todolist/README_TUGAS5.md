# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Perbedaan dari Inline, Internal, dan External CSS adalah inline CSS dilakukan dengan cara menambahkan atribut style pada elemen html, internal CSS dilakukan dengan cara menambahkan elemen style yang berisi kode CSS pada file HTML, dan external CSS membuat file .css terpisah berisikan kode CSS yang disambungkan ke file html dengan cara menambahkan `<link rel="stylesheet" href="mystyle.css">` pada bagian head file HTML.
Berikut adalah kelebihan dan kekurangannya masing-masing:
- Inline CSS
  - Kelebihan: dapat dengan mudah dan cepat memasukkan CSS ke dalam HTML. Berguna untuk menguji coba perubahan. Tidak perlu membuat dokumen terpisah seperti eksternal CSS. 
  - Kekurangan: Menambahkan aturan CSS ke setiap elemen HTML memakan waktu dan membuat struktur HTML berantakan. Menata beberapa elemen dapat memengaruhi ukuran halaman dan waktu pengunduhan.
- Internal CSS
  - Kelebihan: Dapat menggunakan class dan ID selector dalam. Karena akan menambahkan kode dalam file HTML, tidak perlu membuat dokumen terpisah seperti eksternal CSS. 
  - Kekurangan: Karena kode ditambahkan ke dalam dokumen HTML, dapat meningkatkan waktu untuk me-load page.
- Eksternal CSS
  - Kelebihan: File HTML akan memiliki struktur yang lebih rapih dan ukurannya file-nya lebih kecil. Dapat menggunakan file .css yang sama untuk beberapa halaman. 
  - Kekurangan: Memungkinkan page tidak dirender dengan benar hingga CSS eksternal dimuat. Mengupload atau me-link ke beberapa file CSS dapat meningkatkan waktu untuk me-load page.

## Jelaskan tag HTML5 yang kamu ketahui.
<form></form> HTML Form digunakan untuk mengumpulkan input user. Input user biasanya akan dikirim ke server untuk diproses.
<button></button> merupakan sebuah clickable button.
<h1></h1> <h2></h2> <h3></h3>... HTML Headings adalah judul atau subjudul yang ingin ditampilkan pada website.
<p></p> HTML Paragraph selalu dimulai pada baris baru, dan biasanya berisi teks.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Element selector berlaku untuk semua elemen HTML tersebut. Misalkan elemen p,
```
p {
  // CSS codes
}
```
ID selector berlaku untuk bagian yang memiliki ID tersebut. Misalkan men-select elements dengan ID card-section,
```
#card-section {
  // CSS codes
}
```
Class Selector berlaku untuk bagian yang memiliki class tersebut. Misalkan men-select elements dengan class card,
```
.card {
  // CSS codes
}
```
Pseudo-class selector berlaku untuk bagian yang memiliki class dan sedang berada dalam state pseudo-class tersebut. Misalkan men-select elements dengan class card yang sedang dalam state hover,
```
.card:hover {
  // CSS codes
}
```

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS dan CSS framework Bootstrap
  - menambahkan link stylesheet bootstrap pada head html
  - menambahkan script bootstrap pada body html
  - menggunakan class-class yang telah dibuat bootstrap untuk mengkreasikan halaman-halaman
  - menggunakan class card dari bootstrap untuk membuat tampilan task todolist menjadi card
2. Membuat keempat halaman yang dikustomisasi menjadi responsive.
  - dengan menambahkan link stylesheet bootstrap, bootstrap telah memberikan page responsiveness bawaannya
  - menggunakan grid system bootstrap dan menambahkan class-class yang sesuai pada card sehingga dapat responsif

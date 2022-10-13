# Tugas 6: Javascript dan AJAX
Heroku todolist app link: https://tugas2-pbp-maureen.herokuapp.com/todolist/

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming menulis kode yang berjalan secara berurutan. Ini berarti bahwa setiap operasi harus menunggu yang sebelumnya selesai sebelum yang lainnya dapat dieksekusi. Asynchronous programming menulis kode yang berjalan secara paralel. Ini berarti bahwa suatu operasi dapat terjadi sementara yang lain masih diproses.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah paradigma pemrograman di mana eksekusi program ditentukan oleh peristiwa pengguna yang dilakukan pengguna (klik mouse, klik button, dll), sensor outputs, atau message passing dari program lain. Salah satu contoh penerapannya pada tugas ini adalah ketika button create pada modal di klik, program akan menjalankan fungsi yang ada di dalam $("#button-id").click(function()). Pada kasus ini program akan melakukan post task yang ingin dibuat lalu langsung menampilkannya kepada pengguna tanpa harus merefresh terlebh dahulu.

## Jelaskan penerapan asynchronous programming pada AJAX.
Pada tugas kali ini penerapan asynchronous programming pada AJAX ada di saat user tidak perlu merefresh page untuk data yang baru ditambahkan untuk muncul. Program akan mengirim data ke server dan menambahkan ke tampulan user tanpa harus merefresh halaman.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Untuk mendapatkan data pada awal membuka page, membuat path /todolist/json dengan fungsi views yang akan mengembalikan data dalam format json. Setelah itu, membuat script untuk melakukan get method yang akan mengambil data dari path /todolist/json. Lalu menampilkannya dalam bentuk cards sesuai dengan code html sebelumnya dengan cara mengiterate setiap data menggunakan for loop.

Untuk menambahkan task, membuat modal yang berisikan form untuk menambahkan task baru. Setelah itu, membuat script yang akan menjalankan fungsionalitas dari modal add task tersebut. Script yang dibuat adalah script untuk saat button create di klik. Script menjalankan method post lalu menambahkan data baru pada tampilan page. Method post sendiri akan memanggil fungsi add_task pada views yang akan meng-create object task baru yang dalam bentuk json response. Untuk melihat task baru, user tidak perlu me-refresh karena selain melakukan post method, program akan melakukan penambahan task card dengan data yang baru didapatkan (bukan dari database).

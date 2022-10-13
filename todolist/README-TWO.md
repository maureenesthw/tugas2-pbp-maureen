# Tugas 6: Javascript dan AJAX
Heroku todolist app link: https://tugas2-pbp-maureen.herokuapp.com/todolist/

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming menulis kode yang berjalan secara berurutan. Ini berarti bahwa setiap operasi harus menunggu yang sebelumnya selesai sebelum yang lainnya dapat dieksekusi. Asynchronous programming menulis kode yang berjalan secara paralel. Ini berarti bahwa suatu operasi dapat terjadi sementara yang lain masih diproses.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah paradigma pemrograman di mana eksekusi program ditentukan oleh peristiwa pengguna yang dilakukan pengguna (klik mouse, klik button, dll), sensor outputs, atau message passing dari program lain. Salah satu contoh penerapannya pada tugas ini adalah ketika button create pada modal di klik, program akan menjalankan fungsi yang ada di dalam $("#button-id").click(function()). Pada kasus ini program akan melakukan post task yang ingin dibuat lalu langsung menampilkannya kepada pengguna tanpa harus merefresh terlebh dahulu.

## Jelaskan penerapan asynchronous programming pada AJAX.
Pada tugas kali ini penerapan asynchronous programming pada AJAX ada di saat user tidak perlu merefresh page untuk data yang baru ditambahkan untuk muncul. Program akan mengirim data ke server dan menambahkan ke tampulan user tanpa harus merefresh halaman.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

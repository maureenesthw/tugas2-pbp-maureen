# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django
Heroku mywatchlist app link: https://tugas2-pbp-maureen.herokuapp.com/mywatchlist/

## Perbedaan antara JSON, XML, dan HTML
    - JSON (JavaScript Object Notation) adalah format pertukaran data yang ringan dan sepenuhnya tidak bergantung pada bahasa. Ini didasarkan pada bahasa pemrograman JavaScript dan mudah dimengerti dan dihasilkan. Sintaks JSON diturunkan dari sintaks notasi objek JavaScript, tetapi format JSON hanya berupa teks. Kode untuk membaca dan menghasilkan data JSON dapat ditulis dalam bahasa pemrograman apa pun.
    - XML (Extensible markup language) dirancang untuk membawa data, bukan untuk menampilkan data. XML adalah bahasa markup yang mendefinisikan seperangkat aturan untuk mengkodekan dokumen dalam format yang dapat dibaca manusia dan dapat dibaca mesin. Bahasa ini banyak digunakan untuk representasi struktur data arbitrer seperti yang digunakan di situs web.
    - HTML (HyperText Markup Language) adalah bahasa markup standar untuk dokumen yang dirancang untuk ditampilkan di browser web. HTML menggambarkan struktur halaman web dengan cara menandainya seperti tampilan dokumen.

## Mengapa _data delivery_ diperlukan dalam pengimplementasian sebuah platform?


## Cara saya mengimplementasikan checklist Tugas 3
    1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
        - 
    2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
    3. Membuat sebuah model MyWatchList yang memiliki atribut watched, title, rating, release_date, dan review.
    4. Menambahkan 10 data untuk objek MyWatchList yang sudah dibuat di atas
    5. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:
        - HTML
        - XML
        - JSON
    6. Membuat routing sehingga data di atas dapat diakses melalui URL:
        - http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML
        - http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML
        - http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON
    7. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Membuat sebuah django-app bernama mywatchlist dengan perintah python manage.py startapp mywatchlist
2. Menambahkan aplikasi mywatchlist, pada settings.py di folder project_django, ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah dibuat ke dalam proyek Django.
3. 

## Screenshot Postman
#### HTML
#### XML
#### JSON
# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django
Heroku mywatchlist app link: https://tugas2-pbp-maureen.herokuapp.com/mywatchlist/

## Perbedaan antara JSON, XML, dan HTML
   - JSON (JavaScript Object Notation) adalah format pertukaran data yang ringan dan sepenuhnya tidak bergantung pada bahasa. Ini didasarkan pada bahasa pemrograman JavaScript dan mudah dimengerti dan dihasilkan. Sintaks JSON diturunkan dari sintaks notasi objek JavaScript, tetapi format JSON hanya berupa teks. Kode untuk membaca dan menghasilkan data JSON dapat ditulis dalam bahasa pemrograman apa pun.
   - XML (Extensible markup language) dirancang untuk membawa data, bukan untuk menampilkan data. XML adalah bahasa markup yang mendefinisikan seperangkat aturan untuk mengkodekan dokumen dalam format yang dapat dibaca manusia dan dapat dibaca mesin. Bahasa ini banyak digunakan untuk representasi struktur data arbitrer seperti yang digunakan di situs web.
   - HTML (HyperText Markup Language) adalah bahasa markup standar untuk dokumen yang dirancang untuk ditampilkan di browser web. HTML menggambarkan struktur halaman web dengan cara menandainya seperti tampilan dokumen.

## Mengapa _data delivery_ diperlukan dalam pengimplementasian sebuah platform?


## Cara mengimplementasikan checklist Tugas 3
1. Membuat sebuah django-app bernama mywatchlist dengan perintah python manage.py startapp mywatchlist
2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
    - menambahkan 'mywatchlist' pada INSTALLED_APPS pada settings.py di folder django_project
    - membuat funtion show_mywatchlist pada file vies.py mywatchlist
    - pada file urls.py, mengimport path dan show_mywatchlist, menuliskan app_name = 'mywatchlist', dan menambahkan urlpatterns.
    '''
    urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    ]
    '''
    - mendaftarkan aplikasi mywatchlist ke dalam urls.py pada folder project_django dengan menambahkan path pada urlpatterns.
    '''
    path('mywatchlist/', include('mywatchlist.urls')),
    '''
3. Membuat sebuah model MyWatchList yang memiliki atribut watched, title, rating, release_date, dan review.
    - membuat model baru pada models.py bernama MyWatchList dengan field watched, title, rating, release_date, dan review
    - melakukan perintah `python manage.py makemigrations`
    - melakukan perintah `python manage.py migrate`
4. Menambahkan 10 data untuk objek MyWatchList yang sudah dibuat di atas
    - membuat folder fixtures dan menambahkan file initial_mywatchlist_data.json pada folder tersebut.
    - mengisi file dengan 10 data json.
    - melakukan perintah `python manage.py loaddata`.
5. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format, HTML, XML, dan JSON.
    - membuat funtion show_html, show_xml, dan show_json pada file views.py mywatchlist
6. Membuat routing sehingga data di atas dapat diakses melalui URL http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML, http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML, dan http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON.
    - pada file urls.py menambahkan urlpatterns.
    '''
    urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
    ]
    '''
7. Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses melalui Internet
    - menambahkan `&& python manage.py loaddata initial_mywatchlist_data.json` pada release: sh -c pada Procfile
    - mem-_push_ perubahan ke repositori github

## Screenshot Postman
#### HTML
<img width="960" alt="postman-html" src="https://user-images.githubusercontent.com/94694195/191629569-208099a7-8746-4f3a-88a9-f51b1723d7aa.png">

#### XML
<img width="960" alt="postman-xml" src="https://user-images.githubusercontent.com/94694195/191629591-b15b2e81-d9ec-40fd-a60c-a247b84741da.png">

#### JSON
<img width="960" alt="postman-json" src="https://user-images.githubusercontent.com/94694195/191629597-af9fc2d8-c3c3-449f-b9eb-dce14294fb97.png">

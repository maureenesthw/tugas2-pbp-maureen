# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
Heroku todolist app link: https://tugas2-pbp-maureen.herokuapp.com/todolist/

##  Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?
CSRF merupakan singkatan dari Cross Site Request Forgery. Django memiliki built-in protection untuk mengatasi CSRF attacks, yaitu dengan mengimplementasikan csrf_token. CSRF token adalah token panjang yang di-generate secara acak. Token ini bersifat unik per sesi pengguna. Token ini digunakan untuk memastikan bahwa yang melakukan request pada web adalah pengguna pada sesi itu.

Jika tidak menggunakan csrf_token, berarti saat melakukan request, tidak akan ada token CSRF untuk diverifikasi. Jadi, CSRF attacks akan lebih mudah terjadi karena tidak harus menebak/menemukan token CSRF untuk melakukan request.

##  Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Ya, kita dapat membuat elemen form secara manual tanpa generator {{ form.as_table }}. Caranya adalah dengan membuat elemen form pada HTML yang memiliki method POST. Di dalam elemen form tersebut, dapat diisi dengan elemen input untuk memasukkan data-data yang ingin didapatkan dari user, serta input type submit. 

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
- Ketika user meng-klik input type submit yang berbentuk seperti button, form tersebut akan ter-submit. Setelah user men-submit form, input akan dikembalikan ke fungsi pada views yang memanggil form tersebut dan konten dari user input dapat diakses menggunakan method request.POST.get(input_name). 
- Lalu, untuk menyimpan data pada database, perlu untuk melakukan ModelClassName.objects.create(model_attribute1=input_name1, model_attribute2=input_name2, ...). 
- Untuk menampilkan data yang telah disimpan ke template HTML, perlu menambahkan context dengan isi Task.objects.filter(user=request.user). Filter user ini akan bekerja untuk hanya menampilkan Task yang dibuat oleh user yang sedang logged in.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama todolist dengan perintah python manage.py startapp todolist.
2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
    - menambahkan 'todolist' pada INSTALLED_APPS pada settings.py di folder django_project
    - membuat funtion show_todolist pada file vies.py mywatchlist
    - pada file urls.py, mengimport path dan show_todolist, menuliskan app_name = 'todolist', dan menambahkan urlpatterns.
    ```
    urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    ]
    ```
    - mendaftarkan aplikasi mywatchlist ke dalam urls.py pada folder project_django dengan menambahkan path pada urlpatterns.
    ```
    path('todolist/', include('todolist.urls')),
    ```
3. Membuat sebuah model Task yang memiliki atribut user, date, title, dan description.
    - membuat model baru pada models.py bernama Task dengan field user, date, title, dan description,
    - melakukan perintah `python manage.py makemigrations`
    - melakukan perintah `python manage.py migrate`
4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
    - membuat form registrasi
      - import redirect, UserCreationForm, dan messages pada views.py
      - membuat fungsi register pada views.py
      - membuat register.html berisi form registrasi
      - menambahkan path /todolist/register
    - membuat form login
      - import authenticate dan login pada views.py
      - membuat fungsi login pada views.py
      - memmbuat login.html berisi form login
      - menambahkan path /todolist/login
    - membuat fungsi logout
      - import logoutpada views.py
      - membuat fungsi logout pada views.py
      - menambahkan button/anchor tag pada todolist.html dengan href="{% url 'todolist:logout' %}"
      - menambahkan path /todolist/logout
    - merestriksi akses halaman todolist dan create-task
      - import login_required pada views.py
      - menambahkan kode `@login_required(login_url='/wishlist/login/')` di atas fungsi show_todolist dan create_task
5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
    - membuat todolist.html
    - menambahkan elemen-elemen
6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
    - membuat create_task.html berisikan form data task
    - membuat fungsi create_task pada views.py
7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL-nya.
    - pada file urls.py, menambahkan urlpatterns.
    ```
    urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    ]
    ```
8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    - melakukan git ad, commit, dan push ke git repo. Lalu, perubahan pada website akan otomatis terupdate pada web app yang sudah pernah di create
9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
    - create new account dengan register (2 kali)
    - create new task 3 kali pada setiap akun

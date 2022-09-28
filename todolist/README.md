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
1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
  - 
3. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
4. Membuat sebuah model Task yang memiliki atribut user, date, title, dan description.
5. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
6. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
7. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
8. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL-nya.
9. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
10. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

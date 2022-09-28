# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
Heroku todolist app link: https://tugas2-pbp-maureen.herokuapp.com/todolist/

##  Apa kegunaan {% csrf_token %} pada elemen form? 
CSRF merupakan singkatan dari Cross Site Request Forgery. Django memiliki built-in protection untuk mengatasi CSRF attacks, yaitu dengan mengimplementasikan csrf_token. CSRF token adalah token panjang yang di-generate secara acak. Token ini bersifat unik per sesi pengguna. Token ini digunakan untuk memastikan bahwa yang melakukan request pada web adalah pengguna pada sesi itu.

##  Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?
Jika tidak menggunakan csrf_token, berarti saat melakukan request, tidak akan ada token CSRF untuk diverifikasi. Jadi, CSRF attacks akan lebih mudah terjadi karena tidak harus menebak/menemukan token CSRF untuk melakukan request.

##  Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Ya, kita dapat membuat elemen form secara manual tanpa generator {{ form.as_table }}. Caranya adalah dengan membuat elemen form pada HTML yang memiliki method POST. Di dalam elemen form tersebut, dapat diisi dengan elemen input untuk memasukkan data-data yang ingin didapatkan dari user, serta input type submit.

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

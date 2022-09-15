# Models View Template in Katalog Django App
Heroku App Link: https://tugas2-pbp-maureen.herokuapp.com/

## Bagan Model, Views, dan Template
<img width="1383" alt="mvt-maureen" src="https://user-images.githubusercontent.com/94694195/190284162-3c4aa031-b976-46dc-8d24-6889d59fdab3.png">

## Kegunaan Virtual Environment
Di dalam komputer kita, pasti akan terdapat lebih dari satu proyek. Beberapa proyek yang ada mungkin akan memiliki _package_ yang sama, misalnya sama-sama menggunakan _package_ Django. Setiap proyek tesebut bisa saja menggunakan _package_ dengan versi yang berbeda. Jika kita meng-_update package_ pada global, beberapa proyek kita mungkin akan memerlukan perbaikan tanpa adanya _virtual environment_. 

_Virtual environment_ berguna untuk mengisolasi _packages_ dan _dependencies_ sebuah proyek sehingga tidak bertabrakan. Aplikasi Django bisa saja dibuat tanpa virtual environment. Akan tetapi, penggunaan virtual environment sangat disarankan.

## Pengimplementasian Models View Template 
Menyiapkan repositori dan _virtual environment_.
  - Membuat repositori github dari [template yang diberikan](https://github.com/pbp-fasilkom-ui/assignment-repository).
  - Clone ke lokal komputer dengan melakukan perintah `git clone <URL_REPOSITORI>`.
  - Membuat virtual environment dengan peirntah `pyton -m venv env`.
  - Mengaktifkan virtual environment dengan perintah `env/Scripts/activate.bat`.

1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
    - Import _class_ CatalogItem dari models dengan menambahkan kode di views.py. 
      ```
      from katalog.models import CatalogItem
      ```
    - Membuat fungsi `show_katalog` pada views.py untuk memanggil query ke _model database_ dean menyimpan hasil _query_ ke sebuah variabel `context`.
      ```
      def show_katalog(request):
      data_katalog = CatalogItem.objects.all()
      context = {
          'item_list' : data_katalog,
          'name' : 'Maureen Esther Wijaya',
          'npm' : '2106705335'
      }
      return render(request, "katalog.html", context)
      ```

2. Membuat sebuah _routing_ untuk memetakan fungsi yang telah dibuat pada views.py.
    - Menambahkan kode pada file `urls.py` di dalam folder `katalog` untuk melakukan _routing_ terhadap fungsi pada `views.py` yang telah dibuat.
      ```
      from django.urls import path
      from katalog.views import show_katalog

      app_name = 'katalog'

      urlpatterns = [
          path('', show_katalog, name='show_katalog'),
      ]
      ```
    - Mendaftarkan aplikasi `katalog` ke dalam file `urls.py` di dalam folder `project_django` dengan menambahkan isi variabel `urlpatterns`.
      ```
      path('katalog/', include('katalog.urls')),
      ```

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
    - Mengubah `Fill me!` pada file katalog.htlm menjadi `{{name}}` dan `{{npm}}` agar dapat diisi dengan variabel nama dan npm yang sudah di-_render_ ke dalam HTML.
    - Mengiterasi variabel `item_list` yang telah di-_render_ ke dalam HTML.
      ```
      {% for item in item_list %}
          <tr>
              <th>{{item.item_name}}</th>
              <th>{{item.item_price}}</th>
              <th>{{item.item_stock}}</th>
              <th>{{item.rating}}</th>
              <th>{{item.description}}</th>
              <th>{{item.item_url}}</th>
          </tr>
      {% endfor %}
      ```
      
4. Melakukan _deployment_ ke Heroku terhadap aplikasi.
    - Melakukan git push dan memastikan repositori github sudah _up to date_.
    - Membuat heroku app baru dengan nama tugas2-pbp-maureen.
    - Menambahkan variabel `repository secret` pada github.
      ```
      (NAME)HEROKU_APP_NAME
      (VALUE)tugas2-pbp-maureen
      ```
      ```
      (NAME)HEROKU_APP_KEY
      (VALUE)*secret_api_key*
      ```
    - Melakukan _re-run failed jobs_ pada workflow yang gagal.

### Terima kasih

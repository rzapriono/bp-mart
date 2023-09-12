Aplikasi Adaptable yang sudah di-deploy dapat dilihat di link [bp-mart](https://bp-mart.adaptable.app/main/)

# Implementasi Checklist Tugas 2
## Membuat proyek Django bp_mart
1. Buat direktori baru dengan nama `bp_mart`
2. Buka command prompt dan masuk ke directory tersebut dengan cara mengetik `cmd` di bagian path pada file explorer
3. Jalankan command `python -m venv env` untuk membuat virtual environment
4. Aktifkan virtual environment (menggunakan windows) dengan command `env\Scripts\activate.bat`
5. Buat `requirements.txt` yang berisi dependencies:
   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
   Kemudian install dependencies tersebut dengan command `pip install -r requirements.txt`
7. Terakhir, buat proyek django `bp_mart` menggunakan command `django-admin startproject bp_mart .`
> [!Important]
> Perhatikan bahwa terdapat karakter "." di akhir command

## Membuat aplikasi dengan nama main
1. Buka command prompt dan masuk ke direktori proyek `bp_mart`, kemudian aktifkan virtual environment
2. Buat aplikasi baru bernama `main` dengan command `python manage.py startapp main`
3. Daftarkan aplikasi `main` ke `settings.py` dalam direktori shopping list dengan cara menambahkan `main` ke variabel `INSTALLED_APPS`
   ```python
   INSTALLED_APPS = [
    ...,
   'main',
    ...
   ]
   ```
   
## Melakukan routing pada proyek bp_mart agar dapat menjalankan aplikasi main
1. Buka file `urls.py` di dalam direktori proyek `bp_mart`
2. Impor fungsi `include` dari `django.urls.`
   ```python
   ...
   from django.urls import path, include
   ...
   ```
3. Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`
   ```python
   urlpatterns = [
      ...
      path('main/', include('main.urls')),
      ...
   ]
   ```

## Membuat model pada aplikasi main
1. Buka file `models.py` pada direktori aplikasi `main`
2. Buat sebuah model bernama `item` yang memiliki attribute wajib:
   - `name` sebagai nama item dengan tipe `CharField` 
   - `amount` sebagai jumlah item dengan tipe `IntegerField`
   - `description` sebagai deskripsi item dengan tipe `TextField.`
   
   Saya juga menambahkan beberapa attribute lain seperti `price`, `date_added`, dan `purchased_from`
   ```python
   from django.db import models

   # Create your models here.
   class Item(models.Model):
      name = models.CharField(max_length=255)
      amount = models.IntegerField()
      description = models.TextField()
      price = models.IntegerField()
      date_added = models.DateField(auto_now_add=True)
      purchased_from = models.CharField(max_length=255)
   ```
3. Lakukan migrasi model dengan menjalankan command `python manage.py makemigrations` dan kemudian `python manage.py migrate` untuk mengaplikasikan perubahan model ke basis data
> [!Important]
> Note for myself: Jangan lupa untuk melakukan migrasi setiap kali mengubah model atau attributenya

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
1. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main`, kemudian buat file baru bernama `main.html` di dalamnya
2. Buka file `views.py`, kemudian tambahkan baris import dan buat fungsi show_main
   ```python
   from django.shortcuts import render
   
   def show_main(request):
      context = {
         'app_name' : 'bp-mart',
         'name': 'Reza Apriono',
         'class': 'PBP D',
      }
    return render(request, "main.html", context)   
   ```
   Variabel context berisi data nama aplikasi, nama, dan kelas yang akan ditampilkan pada templates `main.html`
3. Isi `main.html` untuk menampilkan data-data tersebut
   ```html
   <h1>Stok Produk {{app_name}}</h1>

   <h5>Name: </h5>
   <p>{{ name }}</p>
   <h5>Class: </h5>
   <p>{{ class }}</p>
   ```
   
## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Buat file `urls.py` di dalam direktori `main`
2. Isi `urls.py` dengan kode berikut
   ```python
   from django.urls import path
   from main.views import show_main
   
   app_name = 'main'
   
   urlpatterns = [
       path('', show_main, name='show_main'),
   ]
   ```

## Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
1. Login ke [Adaptable.io](https://adaptable.io/) dengan menggunakan akun GitHub yang digunakan untuk membuat proyek `bp_mart`
2. Setelah login, tekan tombol `New App` dan pilih `Connect an Existing Repository`
3. Karena akun GitHub yang saya gunakan sudah terhubung sebelumnya dengan [Adaptable.io](https://adaptable.io/), maka hanya perlu memilih repository `bp-mart` dan pilih branch `main`
4. Pilih `Python App Template` sebagai template deployment
5. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan
6. Gunakan versi Python 3.10
7. Pada bagian Start Command masukkan perintah python `manage.py migrate && gunicorn shopping_list.wsgi`
8. Masukkan `bp-mart` sebagai nama aplikasi yang juga akan menjadi nama domain
9. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi

<br>

# Bagan Request Client ke Web Aplikasi Berbasis Django Beserta Responnya

<br>

# Virtual Environment
## Mengapa menggunakan virtual environment?
Virtual environment adalah suatu lingkungan kerja terisolasi pada komputer kita. Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan/konflik dengan versi lain yang ada karena berbagai proyek yang kita kerjakan dapat membutuhkan/memiliki package dan dependencies yang berbeda-beda.

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal tersebut tidak disarankan dan bukan merupakan best practice. Beberapa alasannya antara lain:
- Bisa terjadi bentrokan package beserta dependencies
- Kesulitan pengelolaan versi
- Resiko keamanan
- Kesulitan migrasi jika ingin memindahkan proyek ke lingkungan pengembangan yang berbeda

Dengan demikian, pembuatan aplikasi web berbasis Django akan lebih baik dilakukan dengan menggunakan virtual environment.
<br>

# MVC, MVT, MVMM, dan Perbedaan Ketiganya
## MVC
MVC atau Model-View-Controller adalah sebuah pola desain arsitektur dalam sistem pengembangan aplikasi yang memisahkan kode menjadi tiga bagian:
- Model: Bertanggung jawab untuk mengelola data dan menyediakan akses ke data. Model bertugas mengatur, mengelola, dan berhubungan langsung dengan database.
- View: Menyajikan tampilan informasi kepada pengguna. View bertanggung jawab untuk merender data yang diberikan oleh model ke dalam format yang sesuai untuk ditampilkan.
- Controller: Merupakan perantara antara Model dan View. Controller menerima input dari setiap proses request user melalui View, memprosesnya, dan berinteraksi dengan model yang sesuai. Controller juga dapat mengirim perintah ke View untuk memperbarui tampilan ketika ada perubahan dalam Model. Controller memegang kendali logika aplikasi.

## MVT
MVT atau Model-View-Template merupakan sebuah arsitektur yang umumnya digunakan dalam pengembangan aplikasi web dengan menggunakan framework Django.
- Model: Bertanggung jawab untuk mengelola data dan menyediakan akses ke data. Model bertugas mengatur, mengelola, dan berhubungan langsung dengan database.
- View: Menyajikan tampilan informasi kepada pengguna. View bertanggung jawab untuk merender data yang diberikan oleh model ke dalam format yang sesuai untuk ditampilkan.
- Template: Mengatur tampilan halaman web menggunakan file HTML berdasarkan hasil response dari view untuk ditampilkan kepada user.

## MVVM
MVVM atau Model-View-ViewModel adalah arsitektur pengembangan aplikasi web yang membagi kode menjadi 3 bagian:
- Model: Bertanggung jawab untuk mengelola data dan menyediakan akses ke data. Model bertugas mengatur, mengelola, dan berhubungan langsung dengan database.
- View: Menampilkan informasi kepada pengguna berupa tampilan.
- ViewModel: ViewModel bertindak sebagai penghubung antara Model dan View. MVMM juga menerapkan konsep data binding, dimana ViewModel dapat mengetahui perubahan yang terjadi di Model sehingga tampilan akan otomatis diperbarui ketika terdapat pembaruan.

## Perbedaan Ketiganya
| MVC   | MVT   | MVVM|
| ---   | ---   | --- | 
| Controller berperan penting dalam mengelola dan mengatur informasi antara Model dan View   | Template bertugas untuk mengatur tampilan halaman web menggunakan file HTML berdasarkan hasil response dari view untuk ditampilkan kepada user.    | ViewModel bertindak sebagai penghubung antara Model dan View. MVVM juga menerapkan konsep data binding agar tampilan akan otomatis diperbarui ketika terdapat pembaruan. |

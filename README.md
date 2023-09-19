Aplikasi Adaptable yang sudah di-deploy dapat dilihat di link [bp-mart](https://bp-mart.adaptable.app/main/)

# Tugas 2
<hr>

## Implementasi Checklist Tugas 2
### Membuat proyek Django bp_mart
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

### Membuat aplikasi dengan nama main
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
   
### Melakukan routing pada proyek bp_mart agar dapat menjalankan aplikasi main
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

### Membuat model pada aplikasi main
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

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
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
   
### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
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

### Membuat Testing Tambahan (Bonus)
Pada tugas ini, saya membuat 1 unit test selain dari 2 unit test yang telah diajarkan di tutorial
```python
def test_main_html_details(self):
        response = Client().get('/main/')
        self.assertContains(response, 'bp-mart')
        self.assertContains(response, 'Reza Apriono') 
        self.assertContains(response, 'PBP D') 
```
tes tersebut bertujuan untuk mengecek tampilan `main.html` sudah sesuai dengan context pada `views.py`

### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
1. Login ke [Adaptable.io](https://adaptable.io/) dengan menggunakan akun GitHub yang digunakan untuk membuat proyek `bp_mart`
2. Setelah login, tekan tombol `New App` dan pilih `Connect an Existing Repository`
3. Karena akun GitHub yang saya gunakan sudah terhubung sebelumnya dengan [Adaptable.io](https://adaptable.io/), maka hanya perlu memilih repository `bp-mart` dan pilih branch `main`
4. Pilih `Python App Template` sebagai template deployment
5. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan
6. Gunakan versi Python 3.10
7. Pada bagian Start Command masukkan perintah python `manage.py migrate && gunicorn shopping_list.wsgi`
8. Masukkan `bp-mart` sebagai nama aplikasi yang juga akan menjadi nama domain
9. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi

## Bagan Request Client ke Web Aplikasi Berbasis Django Beserta Responnya
![MVT Django drawio](https://github.com/rzapriono/bp-mart/assets/107228573/dfd1f7b6-c0b7-4242-9209-59d421d20693)
1. Saat terdapat HTTP request, `urls.py` akan melakukan routing dengan mencocokkan url pattern yang sesuai dengan request yang diterima
2. Jika url pattern ditemukan, `urls.py` akan memanggil function dalam `views.py` yang sesuai dengan request tersebut
3. `views.py` akan mengecek dan mengakses data yang dibutuhkan untuk ditampilkan dari `models.py`
4. Proses mengolah data dilakukan oleh `models.py` yang berhubungan langsung dengan database
5. `views.py` akan merender tampilan halaman web menggunakan `template` dalam bentuk html dan kemudian mengirimkannya sebagai HTTP response

## Virtual Environment
### Mengapa menggunakan virtual environment?
Virtual environment adalah suatu lingkungan kerja terisolasi pada komputer kita. Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan/konflik dengan versi lain yang ada karena berbagai proyek yang kita kerjakan dapat membutuhkan/memiliki package dan dependencies yang berbeda-beda.

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal tersebut tidak disarankan dan bukan merupakan best practice. Beberapa alasannya antara lain:
- Bisa terjadi bentrokan package beserta dependencies
- Kesulitan pengelolaan versi
- Resiko keamanan
- Kesulitan migrasi jika ingin memindahkan proyek ke lingkungan pengembangan yang berbeda

Dengan demikian, pembuatan aplikasi web berbasis Django akan lebih baik dilakukan dengan menggunakan virtual environment.

## MVC, MVT, MVVM, dan Perbedaan Ketiganya
### MVC
MVC atau Model-View-Controller adalah sebuah pola desain arsitektur dalam sistem pengembangan aplikasi yang memisahkan kode menjadi tiga bagian:
- Model: Bertanggung jawab untuk mengelola data dan menyediakan akses ke data. Model bertugas mengatur, mengelola, dan berhubungan langsung dengan database.
- View: Menyajikan tampilan informasi kepada pengguna. View bertanggung jawab untuk merender data yang diberikan oleh model ke dalam format yang sesuai untuk ditampilkan.
- Controller: Merupakan perantara antara Model dan View. Controller menerima input dari setiap proses request user melalui View, memprosesnya, dan berinteraksi dengan model yang sesuai. Controller juga dapat mengirim perintah ke View untuk memperbarui tampilan ketika ada perubahan dalam Model. Controller memegang kendali logika aplikasi.

### MVT
MVT atau Model-View-Template merupakan sebuah arsitektur yang umumnya digunakan dalam pengembangan aplikasi web dengan menggunakan framework Django.
- Model: Bertanggung jawab untuk mengelola data dan menyediakan akses ke data. Model bertugas mengatur, mengelola, dan berhubungan langsung dengan database.
- View: Menyajikan tampilan informasi kepada pengguna. View bertanggung jawab untuk merender data yang diberikan oleh model ke dalam format yang sesuai untuk ditampilkan.
- Template: Mengatur tampilan halaman web menggunakan file HTML berdasarkan hasil response dari view untuk ditampilkan kepada user.

### MVVM
MVVM atau Model-View-ViewModel adalah arsitektur pengembangan aplikasi web yang membagi kode menjadi 3 bagian:
- Model: Bertanggung jawab untuk mengelola data dan menyediakan akses ke data. Model bertugas mengatur, mengelola, dan berhubungan langsung dengan database.
- View: Menampilkan informasi kepada pengguna berupa tampilan.
- ViewModel: ViewModel bertindak sebagai penghubung antara Model dan View. MVVM juga menerapkan konsep data binding, dimana ViewModel dapat mengetahui perubahan yang terjadi di Model sehingga tampilan akan otomatis diperbarui ketika terdapat pembaruan.

### Perbedaan Ketiganya
| MVC   | MVT   | MVVM|
| ---   | ---   | --- | 
| Controller berperan penting dalam mengelola dan mengatur informasi antara Model dan View.   | Template bertugas untuk mengatur tampilan halaman web menggunakan file HTML berdasarkan hasil response dari view untuk ditampilkan kepada user.    | ViewModel bertindak sebagai penghubung antara Model dan View. MVVM juga menerapkan konsep data binding, dimana ViewModel dapat mengetahui perubahan yang terjadi di Model sehingga tampilan akan otomatis diperbarui ketika terdapat pembaruan. |

<br>

# Tugas 3
<hr>

## Implementasi Checklist Tugas 3

### Membuat Input `form` untuk menambahkan objek model
#### Kerangka views
Langkah yang saya lakukan sebelum membuat input `form` adalah menciptakan suatu struktur dasar yang akan berfungsi sebagai kerangka views dari web bp-mart. Dengan menggunakan kerangka tersebut, konsitensi desain web bp-mart dapat dipertahnkan dan kemungkinan terjadinya redundansi kode dapat diminimalisir. Saya melakukannya dengan cara:
1. Buat folder `templates` pada root folder `bp_mart`. Kemudian, buat file `base.html` pada folder `templates` yang berisi:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```

2. Tambahkan kode `BASE_DIR / 'templates` pada variabel `TEMPLATES` yang terletak di `settings.py` pada subdirektori `bp_mart`
```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
...
```

3. Ubah `main.html` pada folder `templates` yang berada di direktori `main` menjadi berisi kode html:
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Shopping List Page</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
```

#### Input `form`
Setelah berhasil membuat kerangka views, selanjutnya saya membuat input `form` untuk menambahkan data item baru yang akan ditampilkan di halaman utama web bp-mart. Langkah - langkahnya yakni:
1. Buat file baru bernama `forms.py` pada direktori main, yang berfungsi membuat struktur form yang dapat menerima data item baru.
```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "price"]
```

2. Import beberapa library pada file `views.py` dan juga ubah fungsi `show_main` dengan menambahkan `items = Item.objects.all()` untuk mengambil seluruh object Item pada database dan tambahkan `'items':items` pada context
```python
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item

def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Reza Apriono',
        'class': 'PBP D',
        'items': items
    }

    return render(request, "main.html", context)
```

3. Buat fungsi baru bernama `create_item` pada file `views.py` 
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
Kini pada `views.py` terdapat fungsi `show_main` dan `create_item`

4. Buka file `urls.py` pada folder `main`. Import fungsi `create_item` yang telah dibuat dan tambahkan path url ke dalam `urlpatterns` untuk mengaksesnya. File `urls.py` akan berisi kode: 
```python
from django.urls import path
from main.views import show_main, create_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
]
```

5. Buat file baru dengan nama `create_item.html` pada direktori `main/templates`. File html ini nantinya akan menampilkan halaman yang memungkinkan kita untuk menginput `item` baru. File `create_item.html` berisi kode berikut:
```python
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

6. Buka `main.html` dan tambahkan kode di dalam `{% block content %}` untuk menampilkan data item dalam bentuk table serta tombol "Add New Item" yang akan redirect ke halaman form. Setelah selesai, `main.html` akan berisi kode berikut: 
```python
{% extends 'base.html' %}

{% block content %}
    <h1>Stok Produk {{ app_name }}</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>

    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Price</th>
            <th>Date Added</th>
            <th>Purchased From</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
                <td>{{item.price}}</td>
                <td>{{item.date_added}}</td>
                <td>{{item.purchased_from}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
    
{% endblock content %}
```

### Menambahkan 5 Fungsi Views untuk melihat objek yang sudah ditambahkan
1. Buka `views.py` pada folder `main` dan tambahkan import `HTTPResponse` dan `Serializer`
```python
from django.http import HttpResponse
from django.core import serializers
```

2. Buatlah masing-masing fungsi untuk data delivery dalam berbagai format data di file `views.py` tersebut
- Html
- XML
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

- JSON
```python
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- XML by ID
```python
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

- JSON by ID
```python
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Membuat routing URL untuk masing - masing `views` yang telah ditambahkan
1. Buka `urls.py` pada folder `main` dan import fungsi-fungsi yang telah dibuat. Kemudian, tambahkan path url ke `urlpatterns` untuk mengaksesnya. Setelah kedua tahap tersebut selesai, `urls.py` akan berisi kode berikut:
```python
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```

### __Bonus__: Menambahkan Pesan "Kamu menyimpan X item pada aplikasi ini"
1. Pada fungsi `show_main` yang terdapat di `views.py`, tambahkan kode `'items_count': items.count()` pada variabel `context`
```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Reza Apriono',
        'class': 'PBP D',
        'items': items,
        'items_count': items.count(),
    }

    return render(request, "main.html", context)
```
Kode tersebut bertujuan untuk menghitung banyak item yang berada di QuerySet `items` yang sebelumnya telah kita buat dengan kode `items = Item.objects.all()`, yang mengambil seluruh object Item yang tersimpan pada database.

2. Tambahkan kode berikut pada `main.html` yang berada di folder `templates` direktori `main` agar dapat menampilkan jumlah item yang tersimpan di database.  
```html
...
<p>Kamu menyimpan {{ items_count }} item pada aplikasi ini </p>
...
```
Setelah selesai, banyak item yang tersimpan di database sudah dapat dilihat di halaman web, tepatnya di atas tabel data.

## Perbedaan antara form `POST` dan form `GET` dalam Django
| POST   | GET   |
| ---    | ---   |
| Digunakan untuk mereturn login form Django, di mana browser menggabungkan data dari form, melakukan encode terhadap data untuk ditransmisikan, mengirimkannya ke server, dan kemudian menerima kembali responsenya.    | Menggabungkan data yang telah disubmit ke dalam string dan menggunakannya untuk membuat URL, yang berisi address pengiriman data, serta keys dan values dari data. 
| POST request digunakan untuk request yang mengubah state dari sistem/server, dengan POST parameter yang digunakan untuk memperbarui data atau membuat perubahan di database.   | GET request sering digunakan untuk fetch dokumen atau data yang tidak menyebabkan perubahan pada server. GET parameter digunakan untuk menspesifikkan dokumen mana yang dicari atau di halaman mana kita berada
| Lebih aman karena data tidak ditampilkan di URL dan dapat digabungkan dengan protection lain seperti CSRF Django.   | Kurang aman karena data akan muncul di URL, history borwser, dan log server, sehingga tidak cocok untuk password form.
|  Dapat menerima berbagai tipe data seperti string, numeric, binary, dll.   | Hanya bisa menerima data dalam bentuk string.
| Dapat mengirimkan data dalam jumlah besar karena parameter request akan terdapat di body dari HTTP. |   Tidak dapat mengirimkan data dalam jumlah besar karena parameter request terdapat di URL.
| Request dengan metode POST tidak dapat dibookmark di browser   | Request dengan metode GET dapat dibookmark di browser
| Request yang dibuat dengan metode POST tidak disimpan dalam cache memory browser    | Request yang dibuat dengan metode GET disimpan dalam cache memory browser

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
| XML    | JSON   | HTML |
| ---    | ---    | ---  |
| Merupakan Markup language yang mendefenisikan serangkaian aturan untuk data dalam format yang dapat dibaca oleh mesin dan manusia | Merupakan Format pengiriman data yang dapat diparse oleh browser dan dibaca oleh manusia dengan mudah   | Merupakan markup language yang digunakan untuk membangun struktur dan tampilan halaman web.
| Data disimpan dalam struktur tree dengan namespace untuk kategori data yang berbeda berbeda.    |  Data disimpan dalam pasangan `key` - `value` dengan struktur list of dictionary | Meskipun dapat mengandung data, namun bukan merupakan format yang tepat untuk mengirim data.
| Menggunakan tag untuk mendefinisikan elemen. XML memungkinkan user untuk membuat tag selain dari yang telah disediakan XML | Tidak menggunakan tag, namun menggunakan pasangan `key` - `value` sehingga syntaxnya lebih ringkas dan mudah untuk dibaca | Menggunakan tag untuk mendefinisikan elemen. HTML tidak memiliki fleksibilitas untuk membuat tag sendiri

## Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern
JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern antara lain:
- Ringan dan mudah dibaca

Sintaks JSON merupakan turunan dari Object JavaScript dan mudah diparse oleh browser. Akan tetapi, format JSON berbentuk text yang ringan dan didesain menjadi self-describing, sehingga mudah untuk dibaca dan dimengerti.

- Compatible terhadap berbagai bahasa

Banyak bahasa pemrograman yang mendukung parsing dan pembuatan JSON, contohnya JavaScript, PHP, Python, Ruby, C++, dan Perl, sehingga memungkinkan berbagai aplikasi yang ditulis dalam bahasa yang berbeda untuk bertukar data.

- Mudah di-Serialize dan di-Deserialize

JSON mudah di-serialize (mengubah data dari bentuk objek atau struktur data lain ke JSON) dan di-deserialize (mengubah JSON kembali ke bentuk objek atau struktur data), sehingga memudahkan proses pengiriman dan penerimaan data antara aplikasi web.

- Penyimpanan data dalam bentuk array

Dengan format pasangan key dan value, JSON dapat menyimpan data dalam bentuk array yang menjadikan data lebih terstruktur, transfer data menjadi lebih mudah, dan mudah untuk dibaca.

## Hasil akses URL menggunakan Postman untuk Melihat Data
### HTML
<img width="1280" alt="image" src="https://github.com/rzapriono/bp-mart/assets/107228573/0bd6c851-8da7-4c15-8b16-41567a77f82f">


### XML
<img width="1280" alt="image" src="https://github.com/rzapriono/bp-mart/assets/107228573/943f10a8-d7b4-4ead-8c95-36410633abd0">

### JSON
<img width="1280" alt="image" src="https://github.com/rzapriono/bp-mart/assets/107228573/1a58b0ce-52f9-4b49-9ce8-1d05b5006377">

### XML by ID
<img width="1280" alt="image" src="https://github.com/rzapriono/bp-mart/assets/107228573/db4110a1-95d7-4bea-8284-04254e6134c6">


### JSON by ID
<img width="1280" alt="image" src="https://github.com/rzapriono/bp-mart/assets/107228573/105c9927-9dd2-4d93-846c-794f3400f7f2">

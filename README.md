Aplikasi Adaptable yang sudah di-deploy dapat dilihat di link [bp-mart](https://bp-mart.adaptable.app/main/)

# Arsip Tugas
<details>
<summary>Tugas 2</summary>

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
</details>

<details>
<summary>Tugas 3</summary>

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

<br>
</details>

# Tugas 4
<hr>

## Implementasi Checklist Tugas 4
### Membuat Fungsi Registrasi
1. Pada `views.py` yang ada pada subdirektori `main`, tambahkan import `redirect`, `UserCreationForm`, dan `messages`
```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
2. Buat sebuah fungsi baru bernama `register` yang menerima parameter `request`
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
3. Buat sebuah file baru pada folder `main/templates` dengan nama `register.html`, yang berisi kode html berikut:
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

### Membuat Fungsi Login
1. Buka `views.py` yang ada pada subdirektori `main`,tambahkan import `authenticate` dan `login`
```python
from django.contrib.auth import authenticate, login
```
2. Buatlah fungsi dengan nama `login_user` yang menerima parameter `request`
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

### Membuat Fungsi Logout
1. Buka `views.py` yang ada pada subdirektori `main`,tambahkan import `logout`
```python
from django.contrib.auth import logout
```
2. Buatlah fungsi dengan nama `logout_user` yang menerima parameter `request`
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
3. Buka file `main.html` yang ada pada folder `main/templates`, tambahkan potongan kode berikut untuk membuat button logout
```python
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```

### Membuat routing URL untuk masing - masing `register`, `login`, dan `logout` yang telah ditambahkan
1. Pada `urls.py` yang ada pada subdirektori `main`, import fungsi-fungsi yang telah dibuat sebelumnya

2. Tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimport. Setelah selesai, `urls.py` akan berisi kode berikut:
```python
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

### Menampilkan Detail Informasi Pengguna yang Sedang Logged In seperti Username dan Menerapkan Cookies seperti Last Login pada Halaman Utama Aplikasi.
1. Pada `views.py` yang ada pada subdirektori `main`, dan tambahkan import berikut:
```python
import datetime
```
2. Pada fungsi `login_user`, tambahkan fungsi untuk menambahkan cookie yang bernama `last_login` dengan mengganti kode yang ada pada blok `if user is not None`. Fungsi tersebut berguna untuk melihat kapan terakhir kali pengguna melakukan login. Fungsi `login_user` akan menjadi kode berikut:
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
3. Pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel context. Fungsi `show_main` akan berisi kode berikut:
```python
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': 'Reza Apriono',
        'class': 'PBP D',
        'items': items,
        'items_count': items.count(),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```
4. Ubah fungsi `logout_user` menjadi kode berikut:
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
5. Buka file `main.html` pada `main/templates` dan tambahkan kode berikut untuk menampilkan data last login:
```python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

### Menghubungkan Model `Item` dengan `User`
1. Pada `models.py` yang ada pada subdirektori `main`, tambahkan kode berikut untuk mengimport model:
```python
from django.contrib.auth.models import User
```
2. Tambahkan kode berikut pada ada model `Item`
```python
# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)   # UPDATED!
    ...
```
3. Pada `views.py` yang ada di subdirektori `main`, ubah fungsi `create_product` menjadi seperti berikut:
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
4. Ubah fungsi `show_main` menjadi sebagai berikut:
```python
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP D',
        'items': items,
        'items_count': items.count(),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```
5. Tambahkan beberapa baris import dan kode pada `forms.py`, hingga berisi kode berikut:
```python
from django.forms import ModelForm
from main.models import Item
from django import forms   # NEW!
from django.contrib.auth.models import User   # NEW!

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "price", "purchased_from"]
    
    # Baris baru ini menimpa atau 'override' field user yang otomatis ada dari ModelForm.
    # Gunanya untuk menambahkan atribut tertentu, seperti required=True pada contoh
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)  # NEW 
```
6. Simpan semua perubahan dan lakukan migrasi model dengan command `python manage.py makemigrations`, kemudian aplikasikan migrasi dengan command `python manage.py migrate`.

### Membuat Dua akun Pengguna dengan Masing-Masing Tiga Dummy Data
- user01

- user02

## __Bonus__
### Tombol dan Fungsi untuk Menambahkan `amount` Suatu Objek
1. Pada `views.py` yang terdapat di direktori `main`, buat sebuah fungsi bernama `add_amount` yang menerima parameter request dan id. Fungsi tersebut berfungsi untuk menambahkan amount dari suatu item sebanyak 1 buah.
```python
def add_amount(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Buka file `main.html` yang berada di direktori `main/templates`, kemudian tambahkan kode berikut untuk membuat button yang akan memanggil fungsi `add_amount` kita ditekan.
```html
...
<td>
    <form method="post" action="{% url 'main:add_amount' item.id %}">
        {% csrf_token %}
        <button type="submit">Add</button>
    </form>
</td>
```
Tambahkan kode html tersebut setelah tabel yang menampilkan data dari item-item. Setelah selesai, akan terdapat tombol `add_amount` disamping data dari tiap item

### Tombol dan Fungsi untuk Mengurangi `amount` Suatu Objek
1. Pada `views.py` yang terdapat di direktori `main`, buat sebuah fungsi bernama `reduce_amount` yang menerima parameter request dan id. Fungsi tersebut berfungsi untuk mengurangi amount dari suatu item sebanyak 1 buah.
```python
def reduce_amount(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        if item.amount > 0:
            item.amount -= 1
            item.save()
        if item.amount == 0:
            item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Buka file `main.html` yang berada di direktori `main/templates`, kemudian tambahkan kode berikut untuk membuat button yang akan memanggil fungsi `reduce_amount` kita ditekan.
```html
<td> 
    <form method="post" action="{% url 'main:reduce_amount' item.id %}">
        {% csrf_token %}
        <button type="submit">Reduce</button>
    </form>
    </td>
```
Tambahkan kode tersebut setelah kode html `add_amount` yang telah ditambahkan sebelumnya agar button `reduce_amount` berada di sebelah kanan dari button `add_amount`

### Tombol dan Fungsi untuk Menghapus Suatu Objek dari Inventori
1. Pada `views.py` yang terdapat di direktori `main`, buat sebuah fungsi bernama `delete_item` yang menerima parameter request dan id. Fungsi tersebut berfungsi untuk menghapus suatu item dari database inventori.
```python
def delete_item(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main')) 
```
2. Buka file `main.html` yang berada di direktori `main/templates`, kemudian tambahkan kode berikut untuk membuat button yang akan memanggil fungsi `delete_item` kita ditekan.
```html
<td> 
    <form method="post" action="{% url 'main:delete_item' item.id %}">
        {% csrf_token %}
        <button type="submit">Delete</button>
    </form>
</td>
```
Tambahkan kode tersebut setelah kode html`reduce_amount` yang telah ditambahkan sebelumnya agar button `delete_item` berada di sebelah kanan dari button `reduce_amount`

## Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
Django `UserCreationForm` merupakan build-in module yang meng-inherit class `ModelForm`. Untuk menggunakannya, kita perlu mengimportnya dari `django.contrib.auth.forms`. Django `UserCreationForm` digunakan untuk membuat form register bawaan Django untuk user baru pada web-app.
- Kelebihan:
    * Pengguna baru dapat mendaftar dengan mudah di situs web tanpa mengharuskan kita untuk menulis kode form register user dari awal.
    * Terintegrasi dengan model `User` bawaan Django, sehingga data user langsung tersimpan ke database ketika form berhasil disimpan.
    * Memiliki validasi otomatis terhadap input untuk memastikan apakah input pada tiap field sudah memenuhi persyaratan, seperti validasi kekuatan password.
- Kekurangan:
    * Field yang disediakan `UserCreationForm` terbatas pada 3 field bawaan, yakni `username`, `password1`, dan `password2` (untuk konfirmasi password), sehingga kita harus menambahkan sendiri field lain jika dibutuhkan.
    * Tampilan bawaan dari `UserCreationForm` sangat sederhana dan perlu dilakukan penyesuaian tampilannya terhadap keseluruhan web-app kita.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
|Autentikasi    | Otorisasi |
|---            |---        |
|Autentikasi merupakan proses verifikasi user yang masuk ke dalam sistem web-app| Otorisasi adalah proses penentuan izin atau hak akses yang dimiliki user setelah berhasil diautentikasi.
|Ketika user mencoba masuk ke sistem web-app, proses autentikasi memastikan user untuk mengisi form login dan memberikan username serta password.| Detelah pengguna berhasil login, otorisasi menentukan apakah mereka memiliki izin untuk melihat halaman tertentu, mengedit data, atau melakukan tindakan lain.
|Autentikasi penting untuk memastikan bahwa hanya user yang valid yang dapat masuk ke dalam sistem web-app| Otorisasi penting untuk memastikan bahwa meskipun user telah diautentikasi, mereka hanya memiliki akses terhadap resource atau fitur yang sesuai dengan peran atau izin yang dimiliki user tersebut.
|Contoh dari autentikasi adalah penggunaan dekorator `@login_required` untuk memastikan bahwa hanya pengguna yang telah terautentikasi yang dapat mengakses suatu view.  | Menggunakan dekorator `@permission_required` atau `@user_passes_test` untuk membatasi akses berdasarkan izin atau kondisi lain. |

Autentikasi dan otorisasi adalah fitur kunci dalam mengamankan sistem dan web-app. Keduanya bekerja bersama dan saling melengkapi untuk menciptakan lapisan keamanan yang kuat.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah sejumlah informasi dalam jumlah kecil yang dikirim oleh server web kepada browser dan kemudian dikirimkan kembali oleh browser untuk requests halaman kedepannya. Cookies berisi berbagai macam informasi seperti session ID, user preferences, serta data-data lain yang relevan dan sering digunakan untuk mengingat informasi tentang pengguna antar session. Cookies digunakan untuk autentikasi, user tracking, dan juga menjaga user preferences. 

Cookies memiliki 2 jenis, yakni session cookie dan persistent cookie. Session cookie disimpan di memory browser dan akan dihapus jika browser ditutup, sehingga lebih aman dan tidak bisa digunakan untuk melacak informasi jangka panjang. Sedangkan persistent cookie disimpan di sebuah file pada browser komputer sehingga kurang aman dan bisa digunakan untuk melacak informasi jangka panjang.

Django menggunakan cookies sebagai bagian dari session management system dalam mengelola data user session dengan menggunakan komponen yang disebut "Session Framework". Ketika seorang user melakukan login, Django akan membuat session ID yang unik dan meletakkan session ID cookie pada client. Sementara itu, session data diletakkan pada server. Dengan demikian, hanya session ID yang dapat dilihat oleh user, sedangkan session data aman karena disimpan di dalam server. Django mengaksesnya menggunakan request dan response berdasarkan session ID yang sesuai. 

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara umum penggunaan cookies aman apabila dilakukan dan dikelola secara benar dengan memperhatikan security yang tepat. Meskipun aman, tetap ada potensi resiko kemanan yang perlu diwaspadai, antara lain keamanan data cookies yang terancam dengan Cookie Hijacking atau Man-in-the-Middle Attack, serangan Cross-Site Scripting (XSS) yang dapat menyisipkan kode berbahaya ke cookies, serangan Cross-Site Request Forgery (CSRF), dan privasi dari Third-Pary cookies yang digunakan tanpa sepengetahuan user.

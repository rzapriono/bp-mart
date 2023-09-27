from django.forms import ModelForm
from main.models import Item
from django import forms   # NEW!
from django.contrib.auth.models import User   # NEW!

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "price", "purchased_from", "user"]
    
    # Baris baru ini menimpa atau 'override' field user yang otomatis ada dari ModelForm.
    # Gunanya untuk menambahkan atribut tertentu, seperti required=True pada contoh
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)  # NEW 
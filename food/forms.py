from django import forms
from .models import Product


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

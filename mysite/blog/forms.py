from django import forms
from .models import Category
  
# creating a form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "title",
            "slug",
            "content",
        ]

class ProductForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Masukkan nama product"
        })
    )
from django import forms
from products.models import product
class ProductForm(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'

from django import forms
from products.models import index_product_details

class ProductForm(forms.ModelForm):
    class Meta:
        model = index_product_details
        fields = '__all__'

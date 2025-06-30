from django.shortcuts import render
from products.models import *
# Create your views here.
def ecommerce(request, category=None):
    categories = product_category.objects.all()
    first_category = categories.first()

    if category:
        products = index_product_details.objects.filter(product_category__name=category)
    else:
        products = index_product_details.objects.filter(product_category=first_category) if first_category else []

    return render(request, 'index.html', {'products': products, 'categories': categories, 'first_category': first_category})

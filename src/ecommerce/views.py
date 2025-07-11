from django.shortcuts import render
from products.models import *
# Create your views here.
def ecommerce(request, category=None):
    categories = product_category.objects.all().order_by('order_number')
    first_category = categories.first()

    if category:
        products = index_product_details.objects.filter(product_category__name=category).order_by('display_order')
    else:
        products = index_product_details.objects.filter(product_category=first_category).order_by('display_order') if first_category else []
    
    banner_products = index_product_details.objects.filter(is_banner=True).order_by('banner_order')

    return render(request, 'index.html', {'products': products, 
                                          'categories': categories, 
                                          'first_category': first_category,
                                          'banner_products': banner_products,})

from django.shortcuts import render, get_object_or_404
from products.models import *

# Create your views here.
def full_product(request,product_id):
    product=get_object_or_404(index_product_details, product_id=product_id)
    return render(request,'products/product_detail.html',{'product':product})   
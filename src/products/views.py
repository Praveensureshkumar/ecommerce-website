from django.shortcuts import render, get_object_or_404
from products.models import *

# Create your views here.
def full_product(request,product_id):
    product=get_object_or_404(index_product_details, product_id=product_id)
    product_highlights_list = product.product_highlights.split(",") if product.product_highlights else []
    product_size_list=product.product_size.split(",") if product.product_size else []
    return render(request,'products/product_detail.html',{'product':product,'product_highlights_list':product_highlights_list,'product_size_list':product_size_list})   
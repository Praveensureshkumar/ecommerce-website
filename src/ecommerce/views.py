from django.shortcuts import render
from products.models import *
# Create your views here.
def ecommerce(request):
    products=index_product_details.objects.all()
    return render(request,'index.html',{'products':products})
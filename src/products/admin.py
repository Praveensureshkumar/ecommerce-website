from django.contrib import admin

# Register your models here.
from products.models import *
admin.site.register(product_category)
admin.site.register(index_product_details)
admin.site.register(Slide)

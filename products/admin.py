from django.contrib import admin

# Register your models here.
from products.models import *

class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    
admin.site.register(index_product_details)
admin.site.register(Category)
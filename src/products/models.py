
from django.db import models

# Product category used to group products shown on the site
class product_category(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    category_image = models.ImageField(upload_to='media/', null=True, blank=True)
    order_number = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order_number', 'name']     

    def __str__(self):
        return self.name

# Product details shown on index and product listing pages
class index_product_details(models.Model):
    product_category=models.ForeignKey(product_category,on_delete=models.CASCADE,null=True,blank=True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    product_description = models.TextField(null=True, blank=True)
    product_highlights = models.TextField(null=True, blank=True)
    product_original_price = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    product_offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_size_type = models.CharField(max_length=20,null=True, blank=True)
    product_size = models.CharField(max_length=20,null=True, blank=True)
    product_image = models.ImageField(upload_to='media/', null=True, blank=True)
    is_banner = models.BooleanField(default=False)
    banner_order = models.PositiveIntegerField(null=True, blank=True)
    display_order = models.PositiveIntegerField(default=0) 

    class Meta:
        ordering = ['display_order', 'product_name']

    def __str__(self):
        return self.product_name

# Homepage slide model representing a banner slide on the front page
class Slide(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slides/')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
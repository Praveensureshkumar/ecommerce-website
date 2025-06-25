from django.db import models

class product_category(models.Model):
    name=models.CharField(max_length=200,primary_key=True)

    def __str__(self):
        return self.name

class index_product_details(models.Model):
    product_categorys=models.ForeignKey(product_category,on_delete=models.CASCADE,null=True,blank=True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    product_description = models.TextField(null=True, blank=True)
    product_highlights=models.TextField(null=True, blank=True)
    product_original_price = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    product_offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_size_type=models.CharField(max_length=20,null=True, blank=True)
    product_size=models.CharField(max_length=20,null=True, blank=True)
    product_image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.product_name

class Slide(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='slides/')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
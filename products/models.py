from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class index_product_details(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    product_description = models.TextField(null=True, blank=True)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='index_product_details/', null=True, blank=True)

    def __str__(self):
        return self.product_name

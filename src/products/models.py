from django.db import models

class index_product_details(models.Model):

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='index_product_details/', null=True, blank=True)

    def __str__(self):
        return self.product_name

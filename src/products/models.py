from django.db import models

class product_category(models.Model):
    category=models.CharField(max_length=200,primary_key=True)

class index_product_details(models.Model):
    product_categorys=models.ForeignKey(product_category,on_delete=models.CASCADE,null=True,blank=True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='index_product_details/', null=True, blank=True)

    def __str__(self):
        return self.product_name

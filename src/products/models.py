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
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.product_name

from django.db import models
from products.models import index_product_details  # Explicit import

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartProduct(models.Model):  # Renamed class
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(index_product_details, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.product_name

from django.db import models
from .product import Product

from django.contrib.auth import get_user_model
User = get_user_model()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    is_paid = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"Order({self.product.name} by {self.customer.username})"

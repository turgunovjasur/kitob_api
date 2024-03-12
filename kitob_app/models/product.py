from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    Author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def is_in_stock(self):  # omborda maxsulot bor-yo'qligi. False/True
        return self.stock > 0

    def reduce_stock(self, quantity):  # buyurtma ombordan katta bo'sa = False
        if quantity > self.stock:
            return False

        self.stock -= quantity  # aks holda buyurtmani ombordan ayiradi va saqlaydi. True
        self.save()
        return True

    def increase_stock(self, amount):  # omborga maxsulot qo'shadi va saqlaydi.
        self.stock += amount
        self.save()

    class Meta:
        ordering = ['name']

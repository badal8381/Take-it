import uuid
from django.db import models


class Merchant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False)
    address = models.TextField(max_length=255, blank=False)
    mobile = models.BigIntegerField(blank=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"


# class Customer(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20, blank=False)
#     mobile = models.BigIntegerField(blank=False)
#     email = models.EmailField()
#     address = models.TextField(max_length=255, blank=False)

#     def __str__(self):
#         return f"{self.name}"


class Product(models.Model):
    productid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=255)
    in_stock = models.BooleanField(default=False)
    price = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.name} - {self.merchant}"


class Order(models.Model):
    orderid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey('base.Customer', on_delete=models.CASCADE)
    orderdate = models.DateField(auto_now_add=True)
    ordertime = models.TimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.orderid} - {self.customer.name}"

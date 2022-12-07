import uuid
from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False)
    mobile = models.BigIntegerField(blank=False)
    email = models.EmailField()
    address = models.TextField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.name}"

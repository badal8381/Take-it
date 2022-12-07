from django.contrib import admin
from .models import Merchant, Product, Order

admin.site.register(Merchant)
admin.site.register(Product)
admin.site.register(Order)

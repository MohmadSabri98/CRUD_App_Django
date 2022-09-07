from django.contrib import admin

# Register your models here.
from products.models import product
admin.site.register(product)
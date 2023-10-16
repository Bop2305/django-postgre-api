from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Discount, Product, ProductCategory, ProductInventory, User

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductInventory)
admin.site.register(Discount)
admin.site.register(Product)
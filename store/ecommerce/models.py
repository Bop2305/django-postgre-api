from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

    SEX_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]

    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE
    )
    email = models.EmailField(unique=True, null=True)
    birthdate = models.DateTimeField(null=True, blank=True)
    telephone = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductInventory(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Discount(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    desc =  models.TextField(null=True, blank=True)
    SKU = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
    inventory = models.ForeignKey(ProductInventory, null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    session = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
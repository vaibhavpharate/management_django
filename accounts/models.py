from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Category, null=True ,on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = (
        ("Pending","Pending"),
        ('Out For Delivery','Out For Delivery'),
        ("Delivered","Delivered")
    )
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    order_status = models.CharField(max_length=200,choices=ORDER_STATUS)
    date_added = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.product.name

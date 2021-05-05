from django.contrib import admin
from .models import Tag, Product, Category, Customer, Order

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)

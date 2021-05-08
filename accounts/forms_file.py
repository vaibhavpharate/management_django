from django.forms import ModelForm
from .models import Order, Product, Customer, Category, Tag

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

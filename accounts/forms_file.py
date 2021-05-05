from django.forms import ModelForm
from .models import Order, Product, Customer, Category, Tag

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

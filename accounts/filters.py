import django_filters
from django_filters import DateFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_added",lookup_expr='gte') ## gte => greater than or equal
    end_date = DateFilter(field_name="date_added",lookup_expr='lte') ##  lte => less than or equal
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_added']

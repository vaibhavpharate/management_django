from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="home"),
    path('create_order',views.create_order,name="create_order"),
    path('customer/<int:pk>',views.customer,name="customer"),
]

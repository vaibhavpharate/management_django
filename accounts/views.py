from django.shortcuts import render, redirect
from .models import Order, Customer
from .forms_file import OrderForm


# Create your views here.
def index(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()

    total = Order.objects.all().count()
    pending = Order.objects.filter(order_status="Pending").count()
    delivered = Order.objects.filter(order_status="Delivered").count()

    context = {'orders':orders, 'customers':customer,'total':total,
               'pending':pending,'delivered':delivered}

    return render(request,'accounts/index.html',context)

def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form":form}
    return render(request,'accounts/create_order.html',context)


def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    total = orders.all().count()
    pending = orders.filter(order_status="Pending").count()
    delivered = orders.filter(order_status="Delivered").count()

    context = {'customer':customer,'orders':orders, 'total':total,
               'pending':pending,'delivered':delivered}
    return render(request,'accounts/customer.html',context)

def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'accounts/update_order.html',{'form':form})

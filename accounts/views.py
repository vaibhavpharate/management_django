from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Order, Customer
from .forms_file import OrderForm, CreateUserForm

## Filters
from .filters import OrderFilter

# Create your views here.
@login_required(login_url='login')
def index(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()

    total = Order.objects.all().count()
    pending = Order.objects.filter(order_status="Pending").count()
    delivered = Order.objects.filter(order_status="Delivered").count()

    context = {'orders':orders, 'customers':customer,'total':total,
               'pending':pending,'delivered':delivered}

    return render(request,'accounts/index.html',context)


@login_required(login_url='login')
def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form":form}
    return render(request,'accounts/create_order.html',context)

@login_required(login_url='login')
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()


    order_filter = OrderFilter(request.GET,queryset=orders)

    orders = order_filter.qs

    total = orders.all().count()
    pending = orders.filter(order_status="Pending").count()
    delivered = orders.filter(order_status="Delivered").count()

    context = {'customer':customer,'orders':orders, 'total':total,
               'pending':pending,'delivered':delivered,'filter':order_filter}
    return render(request,'accounts/customer.html',context)

@login_required(login_url='login')
def update_order(request,pk):
    order = Order.objects.get(id=pk)

    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'accounts/update_order.html',
                 {'form':form})

def loginPage(request):
    if request.user.is_authenticated:
        messages.warning(request,"User already logged in")
        return redirect('home')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username is not None:
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successful")
            return redirect("/")
        else:
            messages.warning(request,"Login credentials are not right")


    context = {}
    return render(request,'accounts/login.html')


def logoutUser(request):
    logout(request)
    messages.warning(request,"Logout Successful")
    return redirect('login')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f"Account Created from {username}")
        return redirect('login')
    context = {'form':form}
    return render(request,'accounts/register.html',context)

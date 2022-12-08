from django.shortcuts import render, redirect
from .models import Product, Customer, Order
from .forms import OrderForm

# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()
    
    context = {'customers': customers, 'orders': orders, 
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    
    context = {'products': products}
    return render(request, 'accounts/products.html', context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    
    orders = customer.order_set.all()
    total_orders = orders.count()
    
    
    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders}
    return render(request, 'accounts/customer.html', context)


def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'accounts/update_order.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    context = {'item': order}
    return render(request, 'accounts/delete_order.html', context)
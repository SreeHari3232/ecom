from django.shortcuts import redirect, render
from .models import *
from order.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def checkout(request):
    address = Address.objects.get_or_create(user=request.user)
    address = address[0]
    form = AddressForm(instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            form = AddressForm(instance=address) #updated data
            messages.success(request, "Shipping Address Saved")
    
    orders = Order.objects.filter(user=request.user, ordered=False)
    order_items = orders[0].order_items.all()
    order_total = orders[0].get_totals()
    context = {'form':form, 'order_items':order_items, 'order_total':order_total}
    return render(request, 'payment/checkout.html', context)


@login_required
def placeOrder(request):
    messages.success(request, "Your order has placed successfully...")
    return redirect('home')


@login_required
def orderview(request):
    try:
        orders = Order.objects.filter(user=request.user, ordered=False)
        context = {'orders':orders}
    except:
        messages.warning(request, "You don't have an active order")
        return redirect('home')
    return render(request, 'payment/order.html', context)
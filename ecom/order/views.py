from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from shop.models import Product
from django.contrib import messages

# Create your views here.

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    #To check this product is already added into the cart area or not?
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)#incomplete order
    
    if orders.exists():
        order = orders[0]
        if order.order_items.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity updated")
            return redirect('home')
        else:
            order.order_items.add(order_item[0])
            messages.info(request, "This item is added to your cart")
            return redirect('home')
    else:
        order = Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        messages.info(request, "This item quantity is added to your cart")
        return redirect('home')

@login_required    
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    
    if carts.exists() and orders.exists():
        order = orders[0]
        context = {'carts':carts, 'orders':orders}
        return render(request, 'order/cart.html', context)
    else:
        messages.warning(request, "You don't have any items in cart")
        return redirect("home")
        
@login_required          
def remove_from_cart(request, pk):
    items = get_object_or_404(Product, pk=pk)
    orders = Order.objects.filter(user=request.user, ordered=False)
    
    if orders.exists():
        order = orders[0]
        if order.order_items.filter(item=items).exists():
            order_item = Cart.objects.filter(item=items, user=request.user, purchased=False)[0]
            order.order_items.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed from your cart")
            return redirect('cart')
        else:
            messages.info(request, "This item was not in your cart")
    else:
        messages.info(request, "You don't have an active order")
        return redirect('home')

@login_required  
def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >=1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect('cart')
            else:
                messages.info(request, f'{item.name} is not in your cart')
                return redirect('home')
        else:
              messages.info(request, "You don't have an active order")
              return redirect('home') 

@login_required  
def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f'{item.name} quantity has been updated')
                return redirect('cart')
            else:
                order.order_items.remove(order_item)
                order_item.delete()
                messages.info(request, f"{item.name} item has been removed from your cart")
                return redirect('home')
        else:
              messages.info(request, "You don't have an active order")
              return redirect('home')          
          

          

 
        
            
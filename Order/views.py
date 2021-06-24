# Standard library import
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from  django.contrib import messages

# Local import
from .models import Order, OrderItem
from Cart.models import Cart


@login_required(login_url='account:sign-in')
def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request, '', {'order': order})


@require_POST
@login_required(login_url='account:sign-in')
def create_order(request):
    order = Order.objects.create(user_id=request.user.id)
    messages.success(request, 'سفارش شما با موفقیت ثبت شد', 'success')
    cart = Cart.objects.filter(user_id=request.user.id)
    for c in cart:
        OrderItem.objects.create(user_id=request.user.id, order_id=order.id,
        product_id=c.product_id, quantity=c.quantity)
    return redirect('order:detail', order.id)
# Standard library import
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Local import
from .models import Cart
from Product.models import Product
from Account.models import User
from .forms import CartForm


@login_required(login_url='account:sign-in')
def cart_detail(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    return render(request, '', {'cart': cart})


@login_required(login_url='account:sign-in')
def add_cart(request, id):
    data = Cart.objects.filter(user_id=request.user.id, product_id=id)
    if data:
        check = 'yes'
    else:
        check = 'no'
    
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data['quantity']
            if check == 'yes':
                shop = Cart.objects.filter(
                    user_id=request.user.id, product_id=id)
                shop.quantity += info
                shop.save()
            else:
                Cart.objects.create(
                    user_id=request.user.id, product_id=id, quantity=info)
        return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='account:sign-in')
def cart_remove(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='account:sign-in')
def add_single(request, id):
    cart = Cart.objects.get(id=id)
    product = Product.objects.get(id=cart.product.id)
    if product.amount > cart.quantity:
        cart.quantity += 1
        cart.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='account:sign-in')
def remove_single(request, id):
    cart = Cart.objects.get(id=id)
    if cart.quantity > 2:
        cart.quantity -= 1
        cart.save()
    else:
        cart.delete()
    return redirect(request.META.get('HTTP_REFERER'))
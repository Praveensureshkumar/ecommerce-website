from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Cart, CartProduct
from products.models import index_product_details
from datetime import datetime, timedelta
from django.contrib.auth.models import User

def add_to_cart(request, product_id):
    product = get_object_or_404(index_product_details, product_id=product_id)

    # Get existing cart
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart_id = request.session.get('cart_id')
        cart = Cart.objects.filter(id=cart_id).first()

    # Create new cart if needed
    if not cart:
        cart = Cart.objects.create(user=request.user if request.user.is_authenticated else None)
        request.session['cart_id'] = cart.id

    cart_item, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')
def cart(request):
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart_id = request.session.get('cart_id')
        cart = Cart.objects.filter(id=cart_id).first()

    cart_items = CartProduct.objects.filter(cart=cart) if cart else []
    delivery_date = datetime.today() + timedelta(days=5)
    return render(request, 'orders/cart.html', {'cart_items': cart_items, 'delivery_date': delivery_date})

def remove_cart(request, cart_item_id):
    # Get the correct cart based on user or session
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart_id = request.session.get('cart_id')
        cart = Cart.objects.filter(id=cart_id).first()

    # Get the cart item and ensure it belongs to the current cart
    cart_item = get_object_or_404(CartProduct, id=cart_item_id, cart=cart)
    cart_item.delete()
    return redirect('cart')


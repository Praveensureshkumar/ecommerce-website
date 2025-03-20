from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Cart, CartProduct
from products.models import index_product_details


def cart(request):
    cart = Cart.objects.filter(id=request.session.get('cart_id')).first()
    cart_items = CartProduct.objects.filter(cart=cart) if cart else []  # Correct way to get cart items
    return render(request, 'orders/cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(index_product_details, product_id=product_id)

    # Retrieve existing cart or create a new one
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    if not cart:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id  

    # Add or update the cart item
    cart_item, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Redirect to the cart page

def remove_cart(request, cart_item_id):
    cart_item= get_object_or_404(CartProduct, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')



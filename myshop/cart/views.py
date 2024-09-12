from django.shortcuts import render, redirect

from cart.models import Product


# Create your views here.


def cart_add(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    request.session['cart'] = cart
    return redirect('cart_summary')

def cart_remove(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
    request.session['cart'] = cart
    return redirect('cart_summary')

def cart_summary(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    for product in products:
        cart_items.append({
            'product': product,
            'quantity': cart[str(product.id)]
        })
    return render(request, 'cart/cart_summary.html', {'cart_items': cart_items})

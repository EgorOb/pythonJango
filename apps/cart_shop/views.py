from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import CartItemShop, Cart, Product


class ViewCart(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        print(cart)
        cart_items = CartItemShop.objects.filter(cart__user=request.user)
        data = list(cart_items)
        total_price_no_discount = sum(item.product.price * item.quantity
                                      for item in data)
        total_discount = sum(item.product.price * item.product.discount * item.quantity
                             for item in data if item.product.discount is not None)/100
        total_sum = total_price_no_discount - total_discount
        context = {'cart_items': data,
                   'total_price_no_discount': total_price_no_discount,
                   'total_discount': total_discount,
                   'total_sum': total_sum,
                   }
        return render(request, 'cart_shop/cart.html', context)


def save_product_in_cart(request, product_id):
    cart = request.session.get('cart', {})
    print(cart)
    if not cart:
        cart_items = CartItemShop.objects.filter(cart__user=request.user)
        for item in cart_items:
            cart[item.product.id] = item.quantity

    cart_items = CartItemShop.objects.filter(cart__user=request.user,
                                            product__id=product_id)
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart

    if cart_items:
        cart_item = cart_items[0]
        cart_item.quantity += 1
    else:
        product = get_object_or_404(Product, id=product_id)
        cart_user = get_object_or_404(Cart, user=request.user)
        cart_item = CartItemShop(cart=cart_user, product=product)
    cart_item.save()


class ViewCartBuy(View):
    def get(self, request, product_id):
        save_product_in_cart(request, product_id)
        return redirect('cart_shop:cart')


class ViewCartAdd(View):
    def get(self, request, product_id):
        save_product_in_cart(request, product_id)
        return redirect('home:index')


class ViewCartDel(View):
    def get(self, request, item_id):
        cart = request.session.get('cart', {})
        cart_item = get_object_or_404(CartItemShop, id=item_id)
        cart.pop(str(cart_item.product.id))
        cart_item.delete()
        return redirect('cart_shop:cart')


class ViewWishlist(View):
    def get(self, request):
        return render(request, 'cart_shop/wishlist.html')

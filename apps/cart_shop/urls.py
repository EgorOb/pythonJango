from django.urls import path, include
from .views import ViewCart, ViewWishlist, ViewCartBuy, ViewCartDel, ViewCartAdd, CartViewSet
from rest_framework import routers

app_name = 'cart_shop'

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)


urlpatterns = [
    path('', ViewCart.as_view(), name='cart'),
    path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
    path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
    path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
    path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
]

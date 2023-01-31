from django.urls import path
from .views import ViewShop, ProductSingleView

app_name = 'shop'

urlpatterns = [
    path('', ViewShop.as_view(), name='shop'),
    path('prodict/', ProductSingleView.as_view(), name='product-single'),
]

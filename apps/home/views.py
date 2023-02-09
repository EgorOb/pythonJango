from django.shortcuts import render
from django.views import View
from apps.cart_shop.models import Product
from apps.cart_shop.views import fill_card_in_session, fill_id_card_in_session

class IndexShopView(View):

    def get(self, request):
        cart = fill_card_in_session(request)
        id_cart = fill_id_card_in_session(request)

        data = Product.objects.all()
        context = {'data': data
                   }
        return render(request, 'home/index.html', context)


class AboutView(View):

    def get(self, request):
        return render(request, 'home/about.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'home/contact.html')

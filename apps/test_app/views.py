from django.shortcuts import render

# Create your views here.
from random import random

from django.views import View
from django.http import HttpResponse


class RandomNumber(View):
    def get(self, response):
        html = f"{random()}"
        return HttpResponse(html)
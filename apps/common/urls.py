from django.urls import path

from .views import CurrentDateView, Hello, IndexView

urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('hello/', Hello.as_view()),
   path('', IndexView.as_view())
]
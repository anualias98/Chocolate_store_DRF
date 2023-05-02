from django.urls import path

from .views import ListChocolate, DetailChoco, ChocoCheckoutView
from django.urls import path

from . import views
# from knox import views as knox_views
urlpatterns = [
      path('chocolates/',ListChocolate.as_view(),name = 'list'),
      path('details/<int:pk>', DetailChoco.as_view(), name='detail'),
      path('checkout/<int:pk>', ChocoCheckoutView.as_view(), name='checkout'),
      path('home/',views.home, name='home'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('addtocart/<int:pk>/', add_to_cart, name='addtocart'),
    path('cart/', cart_view, name='cart'),
    path('remove/<int:pk>/', remove_from_cart, name='removecart'),
    path('increase/<str:pk>/', increase_cart, name='increasecart'),
    path('decrease/<str:pk>/', decrease_cart, name='decreasecart'),
]
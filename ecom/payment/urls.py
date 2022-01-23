from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('placeorder/', placeOrder, name='placeorder'),
    path('orderview/', orderview, name='orderview'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
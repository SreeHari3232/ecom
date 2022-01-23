from pyexpat import model
from re import template
from turtle import title
from unicodedata import category
from django.shortcuts import render, redirect
from django.template import context
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'




    
class ProductDetail(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'detail'
   
    
    

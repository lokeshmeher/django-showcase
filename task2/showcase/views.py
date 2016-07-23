from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class Home(ListView):
    def get_queryset(self):
        return Product.objects.all()


class ProductDetail(DetailView):
    model = Product

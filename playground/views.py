from django.db.models import Q
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # Products: inventory < 10 AND price < 20
    queryset  = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    queryset  = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    # Products: inventory < 10 OR NOT price < 20
    queryset  = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20)) # | - OR, & - AND, ~ - NOT

    return render(request, 'hello.html', {'name': 'Rovshen', 'products': list(queryset)})

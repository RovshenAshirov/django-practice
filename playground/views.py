from django.db.models import F
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # Products: inventory = price
    queryset = Product.objects.filter(inventory=F('unit_price'))
    queryset = Product.objects.filter(inventory=F('collection__id'))

    return render(request, 'hello.html', {'name': 'Rovshen', 'products': list(queryset)})

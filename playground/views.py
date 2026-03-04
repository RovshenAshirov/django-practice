from django.db.models import F
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/
    queryset = Product.objects.order_by('title') # ASC
    queryset = Product.objects.order_by('-title') # DESC
    queryset = Product.objects.order_by('unit_price', '-title').reverse()

    product = Product.objects.order_by('unit_price')[0]
    product = Product.objects.earliest('unit_price')

    return render(request, 'hello.html', {'name': 'Rovshen', 'products': list(queryset)})

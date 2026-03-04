from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/
    # keyword=value
    queryset  = Product.objects.filter(unit_price=20)
    # queryset  = Product.objects.filter(unit_price>20) # Don't work
    queryset  = Product.objects.filter(unit_price__gt=20) # greater
    queryset  = Product.objects.filter(unit_price__lt=20) # little
    queryset  = Product.objects.filter(unit_price__range=(20, 30))
    queryset  = Product.objects.filter(collection__id__gt=1)
    # queryset  = Product.objects.filter(collection__id__range=(1, 2, 3)) # error
    queryset  = Product.objects.filter(title__contains='coffee') # like
    queryset  = Product.objects.filter(title__icontains='coffee') # ilike
    queryset  = Product.objects.filter(title__startswith='coffee') # like
    queryset  = Product.objects.filter(updated_at__year=2021) # extract year
    queryset  = Product.objects.filter(description__isnull=True) # is null

    return render(request, 'hello.html', {'name': 'Rovshen', 'products': list(queryset)})

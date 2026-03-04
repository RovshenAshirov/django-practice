from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # book = get_airplane()
    try:
        product = Product.objects.get(id=1) # or pk
        # product = Product.objects.get(pk=0) # Error DoesNotExist
    except ObjectDoesNotExist:
        pass

    # None
    product = Product.objects.filter(pk=0).first()

    # True / False
    exists = Product.objects.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Rovshen'})

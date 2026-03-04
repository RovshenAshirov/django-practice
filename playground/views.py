from django.shortcuts import render

from store.models import Product


def say_hello(request):
    queryset = Product.objects.only('id', 'title')
    queryset = Product.objects.defer('description')

    return render(request, 'hello.html', {'name': 'Rovshen', 'products': list(queryset)})

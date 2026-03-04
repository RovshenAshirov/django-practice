from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # 0, 1, 2, 3, 4
    queryset = Product.objects.all()[:5]
    queryset = Product.objects.all()[5:10]

    return render(request, 'hello.html', {'name': 'Rovshen', 'products': list(queryset)})

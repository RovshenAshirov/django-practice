from django.shortcuts import render

from store.models import Product


def say_hello(request):
    queryset = Product.objects.all()
    # queryset = Product.objects.count()

    # for product in queryset:
    #     print(product)

    # list(queryset)

    # queryset[0:5] # lazy

    # queryset.filter().filter().order_by()

    return render(request, 'hello.html', {'name': 'Rovshen'})

from django.shortcuts import render

from store.models import Product, OrderItem


def say_hello(request):
    queryset = Product.objects.values('id', 'title', 'collection__title')
    queryset = Product.objects.values_list('id', 'title', 'collection__title')

    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct()
    ).order_by('title')

    return render(request, 'hello.html', {'name': 'Rovshen', 'products': list(queryset)})

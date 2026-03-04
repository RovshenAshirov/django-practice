from django.shortcuts import render

from store.models import Product, Order


def say_hello(request):
    # select_related (1)
    # prefetch_related (n)

    # queryset = Product.objects.all()
    # queryset = Product.objects.select_related('collection')
    # # queryset = Product.objects.select_related('collection__some_other_field')
    # queryset = Product.objects.prefetch_related('promotions')
    # queryset = Product.objects.select_related('collection').prefetch_related('promotions')

    orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        # 'products': list(queryset),
        'orders': list(orders),
    })

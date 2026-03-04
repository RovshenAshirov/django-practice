from django.db.models import F, ExpressionWrapper, DecimalField
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # Expression
    # - Value
    # - F
    # - Func
    # - Aggregate
    # - ExpressionWrapper
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(
        discounted_price=discounted_price
    )

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        'results': list(queryset)
    })

from django.db.models import Count, Min
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # Count, Min, Max, Avg, Sum
    result = Product.objects.aggregate(Count('id'))
    result = Product.objects.filter(collection_id=3).aggregate(
        count=Count('id'),
        min_price=Min('unit_price'),
    )

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        'result': result
    })

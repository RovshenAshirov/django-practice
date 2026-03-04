from django.db.models import Count
from django.shortcuts import render

from store.models import Customer


def say_hello(request):
    queryset = Customer.objects.annotate(
        orders_count=Count("order")
    )

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        'results': list(queryset)
    })

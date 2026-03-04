from django.db.models import Value, F
from django.shortcuts import render

from store.models import Customer


def say_hello(request):
    # Expression
    # - Value
    # - F
    # - Func
    # - Aggregate

    # queryset = Customer.objects.annotate(is_new=True) # Error
    queryset = Customer.objects.annotate(
        is_new=Value(True),
        new_id=F('id') + 1
    )

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        'result': list(queryset)
    })

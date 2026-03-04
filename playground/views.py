from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # QuerySet lazy
    # lazy loading
    # It doesn’t send a new SQL query every time.
    queryset = Product.objects.all()
    queryset[0]
    list(queryset)
    list(queryset)
    queryset[0]

    return render(request, 'hello.html', {
        'name': 'Rovshen'
    })

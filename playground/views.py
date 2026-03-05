from django.db import connection
from django.shortcuts import render

from store.models import Product


# @transaction.atomic()
def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')
    queryset = Product.objects.raw('SELECT id, title FROM store_product')
    # no annotate, no filter in queryset

    #######################################

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM store_product')
    cursor.close()

    #######################################

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM store_product')
        # cursor.callproc('get_customers', (1, 2, 'a'))

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        'results': list(queryset)
    })

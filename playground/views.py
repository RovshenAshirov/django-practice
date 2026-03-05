from django.db import transaction
from django.shortcuts import render

from store.models import Order, OrderItem


# @transaction.atomic()
def say_hello(request):
    # ALTER SEQUENCE store_order_id_seq RESTART WITH 1000;
    # ALTER SEQUENCE store_orderitem_id_seq RESTART WITH 1000;
    # ...

    with transaction.atomic():
        order = Order.objects.create(customer_id=1)
        item = OrderItem.objects.create(
            order=order,
            product_id=1,
            quantity=1,
            unit_price=10,
        )

    return render(request, 'hello.html', {
        'name': 'Rovshen'
    })

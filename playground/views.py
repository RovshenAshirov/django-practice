from django.db.models import F, Func, Value
from django.db.models.functions import Concat
from django.shortcuts import render

from store.models import Customer


def say_hello(request):
    # https://docs.djangoproject.com/en/4.2/ref/models/database-functions/
    queryset = Customer.objects.annotate(
        # CONCAT
        # full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT"),
        full_name=Concat("first_name", Value(" "), "last_name")
    )

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        'results': list(queryset)
    })

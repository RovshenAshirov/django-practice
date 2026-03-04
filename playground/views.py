from django.shortcuts import render

from store.models import Product
from tags.models import TagItem


def say_hello(request):
    queryset = TagItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        'tags': list(queryset)
    })

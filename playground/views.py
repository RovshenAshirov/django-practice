from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render

from store.models import Product
from tags.models import TagItem


def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)

    queryset = TagItem.objects.select_related('tag').filter(
        content_type=content_type,
        object_id=1
    )

    return render(request, 'hello.html', {
        'name': 'Rovshen',
        'tags': list(queryset)
    })

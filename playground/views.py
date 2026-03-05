from django.shortcuts import render

from store.models import Product, Collection


def say_hello(request):
    # collection = Collection(pk=11)
    # collection = Collection.objects.get(pk=11)
    # # collection.title = "Games"
    # collection.featured_product = None
    # collection.save()
    # print(collection.id)

    # Collection.objects.update(featured_product=None) # for all
    Collection.objects.filter(pk=11).update(featured_product=None)

    return render(request, 'hello.html', {
        'name': 'Rovshen'
    })

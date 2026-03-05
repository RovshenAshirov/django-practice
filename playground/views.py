from django.shortcuts import render

from store.models import Product, Collection


def say_hello(request):
    # collection = Collection(title="Video Games")
    collection = Collection()
    collection.title = "Video Games"
    collection.featured_product = Product(id=1)
    # collection.featured_product_id = 1
    collection.save()
    print(collection.id)

    # collection = Collection.objects.create(
    #     title="Video Games",
    #     featured_product=Product(id=1),
    # )

    return render(request, 'hello.html', {
        'name': 'Rovshen'
    })

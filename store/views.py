from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from store.models import Product, Collection
from store.serializers import ProductSerializer, CollectionSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').order_by('-updated_at')
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        # send in body: {"title": "a", "unit_price": "1", "collection": "1"}
        # send in body: {"title": "a", "slug": "a", "unit_price": "1", "collection": "1", "inventory": 1}
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # pk = 2
        # send in body: {
        #     "title": "+Island Oasis - Raspberry",
        #     "description": "maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum pellentesque",
        #     "slug": "-",
        #     "inventory": 40,
        #     "unit_price": 84.64,
        #     "price_with_tax": 93.10400000000001,
        #     "collection": 3
        # }
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from store.models import Product, Collection
from store.serializers import ProductSerializer, CollectionSerializer


@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection')
    serializer = ProductSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)


@api_view()
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)


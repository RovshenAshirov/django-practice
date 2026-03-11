from django_filters.rest_framework import FilterSet

from store.models import Product


class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            'unit_price': ['gte', 'lte'],
        }

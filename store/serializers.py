from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    # https://www.django-rest-framework.org/api-guide/fields/
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    # collection = serializers.StringRelatedField()
    # collection = CollectionSerializer()
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail',
    )

    def calculate_tax(self, obj: Product) -> Decimal:
        return obj.unit_price * Decimal(1.1)

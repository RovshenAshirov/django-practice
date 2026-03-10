from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail',
    # )

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_tax', 'collection']
        # fields = '__all__'

    def calculate_tax(self, obj: Product) -> Decimal:
        return obj.unit_price * Decimal(1.1)

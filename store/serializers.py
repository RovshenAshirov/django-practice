from decimal import Decimal

from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.Serializer):
    # https://www.django-rest-framework.org/api-guide/fields/
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, obj: Product) -> Decimal:
        return obj.unit_price * Decimal(1.1)

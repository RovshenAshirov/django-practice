from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    def calculate_tax(self, obj: Product) -> Decimal:
        return obj.unit_price * Decimal(1.1)

    # def create(self, validated_data: dict) -> Product:
    #     product = Product.objects.create(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product
    #     # return super().create(validated_data)
    #
    # def update(self, instance: Product, validated_data: dict) -> Product:
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance
    #     # return super().update(instance, validated_data)

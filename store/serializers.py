from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    # https://www.django-rest-framework.org/api-guide/fields/
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)

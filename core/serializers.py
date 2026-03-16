from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer,
    UserSerializer as BaseUserSerializer
)
from rest_framework import serializers

from store.models import Customer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        # fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'birth_date']

    # def save(self, **kwargs):
    #     user = super().save(**kwargs)
    #     Customer.objects.create(user=user)


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

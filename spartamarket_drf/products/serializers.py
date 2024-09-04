from rest_framework import serializers
from .models import Product
from accounts.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Product

        fields = "__all__"

        read_only_fields = ["author"]


class ProductDetailSerializer(ProductSerializer):
    pass

from rest_framework import serializers
from apps.shop.models import ProductModel


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
from rest_framework import serializers
from apps.shop.models import ShopsModel, ProductModel

class ShopsModelSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset=ProductModel.objects.all(),
        many=True,
        required=False
    )
    class Meta:
        model = ShopsModel
        fields = '__all__'


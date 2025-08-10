from rest_framework import serializers
from apps.shop.models import CategoryModel
from apps.shop.serializers.products.products_model_serializer import ProductModelSerializer
from core.constants import TYPE_SHOPS

class ShopsUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField (read_only = True, required=False)
    name = serializers.CharField(max_length=50, required=False)
    email = serializers.EmailField(required=False)
    country = serializers.CharField(max_length=200, required=False)
    city = serializers.CharField(max_length=200, required=False)
    street = serializers.CharField(max_length=200, required=False)
    house_number = serializers.CharField(max_length=200, required=False)
    products = ProductModelSerializer(many=True, required=False)
    type_shop = serializers.ChoiceField(choices=TYPE_SHOPS, required=False)
    category_supplier = serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all(),
        required=False
    )
    debt_to_supplier = serializers.DecimalField(max_digits=50, decimal_places=2)
    created_at = serializers.DateTimeField(read_only = True)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
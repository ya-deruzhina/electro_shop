from rest_framework import serializers
from apps.shop.models import CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id','name_category','level_category']
                        
        def create(self, validated_data):
            return CategoryModel.objects.get_or_create(**validated_data)

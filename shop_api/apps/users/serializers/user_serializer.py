from rest_framework import serializers
from ..models import User

from django.contrib.auth.hashers import make_password
from apps.shop.serializers import ShopsSerializer

class UserSerializer(serializers.ModelSerializer):
    shop_emloyee_name = serializers.CharField(source='shop_employee.name', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username','email', 'role', 
                  'is_active', 'first_name', 'last_name', 'password','shop_employee', 
                  'shop_emloyee_name')

        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'write_only': True},
            'is_active' : {'write_only': True},
            'shop_employee' : {'write_only': True},
        }


    def create(self, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
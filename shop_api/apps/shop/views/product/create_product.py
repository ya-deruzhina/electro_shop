from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import ProductModel
from apps.shop.serializers import ProductModelSerializer


class CreateProductView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()
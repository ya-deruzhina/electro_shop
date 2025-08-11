from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import ProductModel
from apps.shop.serializers import ProductSerializer


class UpdateProductView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
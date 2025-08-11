from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import ProductModel
from apps.shop.serializers import ProductSerializer


class DeleteProductView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        self.perform_destroy(instance)
        return Response({
            "message": "The object was successfully deleted.",
            "data": data
        }, status=status.HTTP_200_OK)
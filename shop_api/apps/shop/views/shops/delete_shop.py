from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import ShopsModel
from apps.shop.serializers import ShopsSerializer


class DeleteShopsView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShopsSerializer
    queryset = ShopsModel.objects.all()

    
    def delete(self, request, *args, **kwargs):
        user = request.user.username
        if user != 'admin':
            shop_id = request.user.shop_employee.id
            instance = ShopsModel.objects.get(pk=shop_id)
            
            serializer = self.get_serializer(instance)
            data = serializer.data
            self.perform_destroy(instance)

            return Response({
                "message": "The object was successfully deleted.",
                "data": data
            }, status=status.HTTP_200_OK)
                
        else:            
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            self.perform_destroy(instance)
            return Response({
                "message": "The object was successfully deleted.",
                "data": data
            }, status=status.HTTP_200_OK)
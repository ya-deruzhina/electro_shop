from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import ShopsModel
from apps.shop.serializers import ShopsModelSerializer


class CreateShopsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShopsModelSerializer
    queryset = ShopsModel.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.user.username
        if user != 'admin':
            raise ValidationError('User Is Not Admin')
        
        products = request.data.get('products')
        data = dict(request.data)

        for value in data:
            data[value] = data[value][0] 
        
        if products:
            products = set(int(i) for i in products.split(',') if i.strip().isdigit())
            data['products'] = products
        else:
            data.pop('products')

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data)
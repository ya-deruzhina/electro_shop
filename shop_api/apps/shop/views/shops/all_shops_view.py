from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import ShopsModel
from apps.shop.serializers import ShopsSerializer


class ShopsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShopsSerializer


    def get_queryset(self):
        user = self.request.user

        if not user.is_superuser:
            try:
                shop_id = user.shop_employee.id
                queryset = ShopsModel.objects.filter(pk=shop_id)
            
            except AttributeError:
                queryset = ShopsModel.objects.none()

        else:
            queryset = ShopsModel.objects.all()
            
        country = self.request.query_params.get('country')
        if country:
            queryset = queryset.filter(country=country)

        id_product = self.request.query_params.get('id_product')
        if id_product:
            queryset = queryset.filter(products=id_product)
        
        queryset = queryset.order_by('category_supplier__id', 'id')

        return queryset
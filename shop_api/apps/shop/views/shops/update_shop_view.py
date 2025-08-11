from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import ShopsModel, ProductModel
from apps.shop.serializers import ShopsSerializer, ShopsUpdateSerializer



class UpdateShopsView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShopsSerializer
    queryset = ShopsModel.objects.all()

    def update(self, request, *args, **kwargs):
        if request.data.get('debt_to_supplier'):
            raise ValidationError('STOP Debt_To_Supplier Unchangeable')
        
        user = request.user.username
        if user != 'admin':
            shop_id = request.user.shop_employee.id
            instance = ShopsModel.objects.get(pk=shop_id)

        else:        
            instance = self.get_object()
        
        if request.data.get('category_supplier').strip().isdigit():
            category_value = int(request.data.get('category_supplier'))
            data = {'category_supplier':category_value}
            new_data = ShopsUpdateSerializer(instance, data=data)
            new_data.is_valid(raise_exception=True)
            new_data.save()

        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        product_value_add = request.data.get('products_add')
        all_products = ProductModel.objects.values_list('id', flat=True)
        
        if product_value_add.strip().isdigit():
            product_value_add = int(product_value_add)
            if product_value_add in all_products:
                instance.products.add(product_value_add)
            else:
                raise ValidationError('STOP Product Is Not Exist')
        
        product_value_remove = request.data.get('products_remove')
        existing_ids = set(instance.products.values_list('id', flat=True))             
        
        if product_value_remove.strip().isdigit():
            product_value_remove = int(product_value_remove)
            if product_value_remove in existing_ids:
                instance.products.remove(product_value_remove)
            else:
                raise ValidationError('STOP Product Not In Shop')


        return Response(serializer.data)

from django.db.models import Avg

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import ShopsModel
from apps.shop.serializers import ShopsSerializer


class ShopsDebtGTView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShopsSerializer
    
    def get_queryset(self):
        user = self.request.user.username
        if user != 'admin':
            raise ValidationError('User Is Not Admin')
        
        average = ShopsModel.objects.aggregate(avg=Avg('debt_to_supplier'))['avg']
        return ShopsModel.objects.filter(debt_to_supplier__gt=average)
from ..models import ShopsModel
from ..serializers import ShopsModelSerializer


class ShopService:
    model = ShopsModel

    @classmethod
    def create(cls, data):
        serializer = ShopsModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



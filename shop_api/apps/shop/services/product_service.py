from ..models import ProductModel
from ..serializers import ProductModelSerializer


class ProductService:
    model = ProductModel

    @classmethod
    def create(cls, data):
        serializer = ProductModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



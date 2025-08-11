from ..models import CategoryModel
from ..serializers import CategorySerializer


class CategoryService:
    model = CategoryModel

    @classmethod
    def create(cls, data):
        serializer = CategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



from apps.shop.serializers.shops.shop_model_serializer import ShopsModelSerializer
from apps.shop.serializers.shops.shop_update_serializer import ShopsUpdateSerializer
from apps.shop.serializers.shops.shop_view_serializer import ShopsSerializer

from apps.shop.serializers.products.products_view_serializer import ProductSerializer
from apps.shop.serializers.products.products_model_serializer import ProductModelSerializer

from apps.shop.serializers.category.category_serializer import CategorySerializer


all= (
    'ShopsModelSerializer',
    'ShopsUpdateSerializer',
    'ShopsSerializer',
    'ProductSerializer',
    'ProductModelSerializer',
    'CategorySerializer',
    )


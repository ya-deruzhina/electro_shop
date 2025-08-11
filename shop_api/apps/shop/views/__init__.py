from apps.shop.views.shops.all_shops_view import ShopsView
from apps.shop.views.shops.debt_gt_view import ShopsDebtGTView
from apps.shop.views.shops.delete_shop import DeleteShopsView
from apps.shop.views.product.delete_product import DeleteProductView
from apps.shop.views.shops.create_shop_view import CreateShopsView
from apps.shop.views.product.create_product import CreateProductView
from apps.shop.views.product.update_product_view import UpdateProductView
from apps.shop.views.shops.update_shop_view import UpdateShopsView
from apps.shop.views.message.send_message_view import QRcodeSendView


all= (
    'ShopsView',
    'ShopsDebtGTView',
    'DeleteShopsView',
    'DeleteProductView',
    'CreateShopsView',
    'CreateProductView',
    'UpdateProductView',
    'UpdateShopsView',
    'QRcodeSendView'
    )


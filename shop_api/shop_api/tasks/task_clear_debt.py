from shop_api.celery import app
from apps.shop.models import *
from apps.shop.models import ShopsModel
from apps.shop.serializers import ShopsUpdateSerializer

@app.task()
def clear_debt_task (shops_ids):
    print("Begin Task - clear_debt_task")

    for shop_id in shops_ids:        
        try:
            shop = ShopsModel.objects.get(id=shop_id)
            data = {'debt_to_supplier':0}
            serializer = ShopsUpdateSerializer(shop, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
        except:
            continue
    print("End period Task - increase_debt_task")
from shop_api.celery import app
from apps.shop.models import ShopsModel
from apps.shop.serializers import ShopsUpdateSerializer
import random
from celery import shared_task
from decimal import Decimal


@shared_task
def increase_debt_task():
    print("Begin period Task - increase_debt_task")
    shops = ShopsModel.objects.all()
    for shop in shops:
        random_number = Decimal(f"{random.uniform(5, 500):.2f}")
        new_debt = shop.debt_to_supplier + random_number
        data = {'debt_to_supplier':new_debt}

        serializer = ShopsUpdateSerializer(shop, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    print("End period Task - increase_debt_task")
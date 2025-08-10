from apps.shop.models import ProductModel, CategoryModel
from apps.shop.services import ShopService
import random
from core.constants import TYPE_SHOPS

from faker import Faker
fake = Faker()

def get_admin_params(products, category):
    return {
        "name": fake.name(),
        "email": fake.email(),
        "country": fake.country(),
        "city": fake.city(),
        "street": fake.street_address(),
        "house_number": random.randint(1,100),
        "products": products,
        "type_shop":random.choice(TYPE_SHOPS)[0],
        "category_supplier":category,
        "debt_to_supplier": round(random.uniform(10, 1000), 2)
    }


def perform(*args, **kwargs):
    products_all = list(ProductModel.objects.values_list('id', flat=True))
    categories = list(CategoryModel.objects.values_list('id', flat=True))

    for n in range(10):
        products = random.sample(products_all, 3)
        category = random.sample(categories, 1)[0]
    
        ShopService.create(get_admin_params(products, category))

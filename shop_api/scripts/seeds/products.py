from apps.shop.services import ProductService

from faker import Faker
fake = Faker()

def get_admin_params():
    return {
        "name": fake.name(),
        "model": fake.sentence(),
        "launch_date": fake.date_time(),
    }


def perform(*args, **kwargs):
    for n in range(5):
        ProductService.create(get_admin_params())
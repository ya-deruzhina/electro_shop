from apps.users.models import User
from apps.shop.models import ShopsModel
from apps.users.services import UsersService
from faker import Faker
fake = Faker()


def get_user_params(username, shop_employee):
    return {
        "email": fake.email(),
        "shop_employee":shop_employee,
        "first_name":fake.first_name(),
        "last_name":fake.last_name(),        
        "status": User.ACTIVE,
        "role": User.USER,        
        "username": username,
        "password": username,
    }


def perform(*args, **kwargs):
    shops = ShopsModel.objects.all()
    
    for shop in shops:
        username = fake.name()

        if not User.objects.filter(username=username).exists():
            UsersService.create(get_user_params(username, shop))
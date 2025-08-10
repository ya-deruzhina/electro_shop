from apps.shop.services import CategoryService
from apps.shop.models import CategoryModel

data_category = {
    1:'Factory',
    2:'Distributor',
    3:'Dealership center',
    4:'Large retail chain',
    5:'Individual entrepreneur'
}
def perform(*args, **kwargs):
    for data in data_category:
        create_data = {
            "name_category": data_category[data],
            "level_category": data
            
        }
        if not CategoryModel.objects.filter(name_category=data_category[data]).exists():
            CategoryService.create(create_data)
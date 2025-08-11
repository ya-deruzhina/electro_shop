from django.db import models
from .category_model import CategoryModel
from .products_model import ProductModel
from core.constants import TYPE_SHOPS

class ShopsModel (models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.EmailField()
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)
    products = models.ManyToManyField(ProductModel, blank=True)
    type_shop = models.CharField(max_length=50, choices=TYPE_SHOPS)
    category_supplier = models.ForeignKey(CategoryModel, null=True, on_delete=models.SET_NULL)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
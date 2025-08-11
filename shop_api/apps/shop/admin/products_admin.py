from django.contrib import admin
from apps.shop.models import ProductModel

class ProductInline(admin.TabularInline):
    model = ProductModel
    list_display = ["name","model","launch_date","created_at"]

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","model","launch_date","created_at"]
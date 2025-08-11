from django.contrib import admin
from apps.shop.models import CategoryModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name_category", "level_category"]
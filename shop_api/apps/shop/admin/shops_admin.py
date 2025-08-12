from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from apps.shop.models import ShopsModel
from apps.shop.admin.shops_action import remove_dept



@admin.register(ShopsModel)
class ShopsAdmin (admin.ModelAdmin):
    list_display = ["id", "name","category_link","type_shop","debt_to_supplier","created_at"]

    readonly_fields = ['id', 'created_at']
    list_filter = ('city',)
    actions = [remove_dept] 

    def category_link(self, obj):
        if obj.category_supplier:
            url = reverse('admin:shop_categorymodel_change', args=[obj.category_supplier.pk])
            return format_html('<a href="{}">{}</a>', url, obj.category_supplier.name_category)
        return "-"
    category_link.short_description = "Category Supplier"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('category_supplier__level_category', 'type_shop')
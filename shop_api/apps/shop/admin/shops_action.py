from django.contrib import admin
from shop_api.tasks.task_clear_debt import clear_debt_task

@admin.action(description="Remove Debt")
def remove_dept(modeladmin, request, queryset):
    
    if len(queryset) > 20:
        shop_ids = list(queryset.values_list('id', flat=True))
        clear_debt_task.delay(shop_ids)

    for shop in queryset:
        shop.debt_to_supplier = 0
        shop.save()
    modeladmin.message_user(request, f"Removed Debt from {len(queryset)} shops")
from shop_api.tasks.task_send_message import send_message_task
from shop_api.tasks.task_clear_debt import clear_debt_task
from shop_api.tasks.task_increase_debt import increase_debt_task
from shop_api.tasks.task_reduce_debt import reduce_debt_task

from shop_api.celery import app as celery_app

__all__ = ('celery_app',)

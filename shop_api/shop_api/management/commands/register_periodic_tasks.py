from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
import pytz, json

class Command(BaseCommand):
    help = "Register periodic tasks for Celery Beat"

    def handle(self, *args, **kwargs):
        periodic_tasks = [
            {
                "name": "increase-debt-every-3-hours",
                "task": "shop_api.tasks.task_increase_debt.increase_debt_task",
                "interval": {"every": 3, "period": IntervalSchedule.HOURS},
                "args": [],
                "kwargs": {},
            },
            {
                "name": "reduce-debt-daily-6-30-am",
                "task": "shop_api.tasks.task_reduce_debt.reduce_debt_task",
                "crontab": {"minute": 30, "hour": 6, "timezone": pytz.timezone("Europe/Minsk")},
                "args": [],
                "kwargs": {},
            },
        ]

        for task_def in periodic_tasks:
            if "interval" in task_def:
                schedule, _ = IntervalSchedule.objects.get_or_create(**task_def["interval"])
                schedule_field = {"interval": schedule}
            elif "crontab" in task_def:
                cron_defaults = {"minute": "*", "hour": "*", "day_of_week": "*", "day_of_month": "*", "month_of_year": "*"}
                cron_values = {**cron_defaults, **task_def["crontab"]}
                schedule, _ = CrontabSchedule.objects.get_or_create(**cron_values)
                schedule_field = {"crontab": schedule}
            else:
                continue

            PeriodicTask.objects.update_or_create(
                name=task_def["name"],
                defaults={
                    "task": task_def["task"],
                    "args": json.dumps(task_def.get("args", [])),
                    "kwargs": json.dumps(task_def.get("kwargs", {})),
                    "enabled": True,
                    **schedule_field,
                }
            )
        self.stdout.write(self.style.SUCCESS("✅ Periodic tasks registered."))

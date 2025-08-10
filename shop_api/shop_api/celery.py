import os
from celery import Celery
import dotenv
from pathlib import Path
# from shop_api import periodic


path_to_env = Path(__file__).parents[1].joinpath(".env")

dotenv.load_dotenv(dotenv_path=path_to_env)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'development')

app = Celery('shop_api')
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.broker_url = os.getenv('CELERY_BROKER_URL')
# app.autodiscover_tasks()

app.autodiscover_tasks([
    'shop_api.tasks',
])

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print ('Begin task')

# debug_task.delay()

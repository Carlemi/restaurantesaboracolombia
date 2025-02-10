import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Usar variable de entorno con IP
BROKER_URL = os.environ.get('DJANGO_CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
app.conf.update(
    task_always_eager=False,
    broker_url=BROKER_URL,
    result_backend='rpc://',
    worker_pool='eventlet',
)
app.autodiscover_tasks()
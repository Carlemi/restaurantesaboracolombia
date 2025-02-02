import os
from celery import Celery

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Agrega esta línea para usar eventlet como pool de ejecución
app.conf.update(
    task_always_eager=False,
    broker_url='amqp://guest:guest@localhost:5672//',
    result_backend='rpc://',
    worker_pool='eventlet'
)
app.autodiscover_tasks()
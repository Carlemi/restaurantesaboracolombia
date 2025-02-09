import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
<<<<<<< HEAD
# Agrega esta línea para usar eventlet como pool de ejecución
""" app.conf.update(
=======

# Usar variable de entorno con IP
BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'amqp://guest:guest@localhost')

app.conf.update(
>>>>>>> recuperacion
    task_always_eager=False,
    broker_url='amqp://guest:guest@localhost',
    result_backend='rpc://',
    worker_pool='eventlet'
<<<<<<< HEAD
) """
=======
) 

>>>>>>> recuperacion
app.autodiscover_tasks()
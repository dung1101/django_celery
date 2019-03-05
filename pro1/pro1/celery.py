import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro1.settings')

app = Celery('pro1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery import Celery
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrackingDocker.settings')

app = Celery('tracking')

app.config_from_object('django.conf:settings', namespace="CELERY")

app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()
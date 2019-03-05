import time

from celery import shared_task


@shared_task
def wait():
    time.sleep(20)
    return "Hihi"

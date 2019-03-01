from celery import Celery


app = Celery('tasks',
             backend='rpc://',
             broker='pyamqp://guest@localhost//')


def add(x, y):
    return x + y

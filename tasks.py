from celery import Celery


app = Celery('tasks',
             backend='rpc://',
             broker='pyamqp://guest@localhost//')


@app.task
def div(x, y):
    return x / y

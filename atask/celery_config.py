from celery import Celery

NAME = 'atask.tasks'
BROKER_URL = 'redis://localhost/0'
BACK_END = 'redis://localhost/0'

app = Celery(NAME, broker=BROKER_URL, backend=BACK_END, include=['tasks'])

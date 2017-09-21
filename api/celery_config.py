from celery import Celery

BROKER_URL = 'redis://localhost/0'
BACK_END = 'redis://localhost/0'

app = Celery('api', broker=BROKER_URL, backend=BACK_END)
app.conf.task_routes = {
        'atask.*': {'queue': 'atask'},
        'btask.*': {'queue': 'btask'},
}

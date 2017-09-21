from celery import Celery

BROKER_URL = 'redis://localhost/0'
BACK_END = 'redis://localhost/0'

app = Celery('api', broker=BROKER_URL, backend=BACK_END)

"""
This is how we enable routing globally. We just use the name of the signature 
and let celery figure out the queue name. There's a few different ways to do this
"""
app.conf.task_routes = {
        'atask.*': {'queue': 'atask'},
        'btask.*': {'queue': 'btask'},
}

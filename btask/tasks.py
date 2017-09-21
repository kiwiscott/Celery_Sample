from celery_config import app

@app.task()
def ping(x):
    return str(x) + "-BB-AWESOME"


@app.task(name='btask.tasks.ping')
def ping2(x):
    return str(x) + "-BB-AWESOME"

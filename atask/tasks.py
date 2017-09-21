from celery_config import app

@app.task()
def ping(x):
    return str(x) + "-AA-AWESOME"


@app.task(name='atask.tasks.ping')
def ping2(x):
    return str(x) + "-AA-AWESOME"

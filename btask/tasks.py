from celery_config import app

@app.task(name='btask.tasks.ping')
def ping(x):
    return str(x) + "-BB-AWESOME"

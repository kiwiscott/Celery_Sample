from celery_config import app

@app.task(name='atask.tasks.ping')
def ping(x):
    return str(x) + "-A-AWESOME"

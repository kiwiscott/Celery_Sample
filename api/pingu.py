import hug
from celery import signature, group
from celery_config import app ##init app 

@hug.get()
def hello(times: int):
    """PING"""
    steps = list(build_group(times))
    job = group(steps)
    res = job()
    return res.get()


def build_group(times: int):
    for x in range(times):
        name = 'atask.tasks.ping' if x % 2 else 'btask.tasks.ping'
        yield signature(name, args=(str(x),))
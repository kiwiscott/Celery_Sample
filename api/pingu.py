import hug
from celery import signature, group
from celery_config import app  # init app


@hug.get()
def hello(times: int):
    """PING"""
    steps = list(build_group(times))
    job = group(steps)
    res = job()
    return res.get()


@hug.get()
def hellox(times: int):
    """PING"""
    steps = list(build_group_queue_name(times))
    job = group(steps)
    res = job()
    return res.get()


def build_group_queue_name(times: int):
    """
        emonstrates routing via the queue directly - the signature
        declares that queue
    """
    for x in range(times):
        queue = 'atask' if x % 2 else 'btask'
        yield signature('tasks.ping', args=(str(x),), queue=queue)


def build_group(times: int):
    """
    demonstrates routing via the name of the task directly. The 
    router determines the queue based on the task name
    """
    for x in range(times):
        name = 'atask.tasks.ping' if x % 2 else 'btask.tasks.ping'
        yield signature(name, args=(str(x),))


Here I was trying to see how we could split up an application and have different tasks in different workers (easy). From there I was trying to see how to use signatures and tasks to route. There's two basic ways as far as I can tell 
1: Use high level routing - this means that all tasks need to override their name e.g. "@app.task(name='btask.tasks.ping')"
2: Use signatures - this means that all task signatures specify a route

See pingu.py for more information

I needed to Set up Redis

#Virtual Env
python -m venv p36 C:\Users\scott\Documents\code\envs\p36


#call hug API
curl http://localhost:8000/hello?times=1064


#start two celery workers with different queue names 
celery -A celery_config worker -l info -Q atask
celery -A celery_config worker -l info -Q btask

#start hug 
hug -f pingu.py

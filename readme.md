
SEt up Redis 

#Virtual Env
python -m venv p36 C:\Users\scott\Documents\code\envs\p36


#call hug API
curl http://localhost:8000/hello?times=1064


#start two celery workers with different queue names 
celery -A celery_config worker -l info -Q atask
celery -A celery_config worker -l info -Q btask

#start hug 
hug -f pingu.py

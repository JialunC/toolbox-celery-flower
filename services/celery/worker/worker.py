import os
from celery import Celery
from celery.schedules import crontab

broker_url = os.getenv('BROKER_URL')
app = Celery('worker', broker=broker_url, include=['emails.tasks'])
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'emails.debug',
        'schedule': crontab(minute='*/5'),
        'args': ("email body",),
        'options': {'queue': 'queue1'}
    },
}
app.conf.timezone = 'UTC'

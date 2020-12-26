from celery.decorators import task


@task(name='emails.debug')
def debug_task(payload):
    print('Request: {0!r}'.format(payload))

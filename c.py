# from celeryconfig import w
# w.delay()
from celery import shared_task

@shared_task
def d():
    return 'd'


d.delay()
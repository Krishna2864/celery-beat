# from celery import Celery


# app = Celery('tasks', broker='redis://localhost:6379/0')

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'c.d',
#         'schedule': 30.0
        
#     },

# }


# from celery import shared_task

# @shared_task
# def w():
#     return 'damn'

broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True


CELERY_TASK_SERIALIZER='pickle'
CELERY_ACCEPT_CONTENT=['json','yaml', 'pickle']
CELERY_TASK_RESULT_EXPIRES=None
CELERY_RESULT_SERIALIZER='pickle'
CELERY_IMPORTS=("multi_server_workers.tasks")

CELERY_ROUTES = {
            'multi_server_workers.tasks.slowadd': {'queue': 'slow'},
            'multi_server_workers.tasks.add': {'queue': 'regular'},
            'multi_server_workers.tasks.tsum': {'queue': 'regular'},
            'multi_server_workers.tasks.run_chord': {'queue': 'regular'},
            }

BROKER_TRANSPORT = "redis"

BROKER_HOST = "10.135.40.241"  # This is a private ip, only accessible from servers 
BROKER_PORT = 6379
BROKER_VHOST = "0"

CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "10.135.40.241"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0
CELERY_IGNORE_RESULT = False

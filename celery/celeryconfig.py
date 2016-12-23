## Broker settings.
broker_url = 'redis://localhost:6379/0'

# List of modules to import when the Celery worker starts.
imports = ('mycelery.tasks',)

## Using the database to store task state and results.
result_backend = 'redis://localhost:6379/0'
task_serializer = 'json'

timezone = 'Asia/Shanghai'
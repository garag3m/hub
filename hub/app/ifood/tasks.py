from huey import crontab
from huey.contrib.djhuey import periodic_task, task

# @task()
# def request_timeout():
#     print('Hello World!')

# @periodic_task(crontab(minute='*/1'))
# def vai_acabar():
#     print('Every one minute this will be printed by the consumer')
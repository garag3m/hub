from huey import crontab
from huey.contrib.djhuey import periodic_task, task
from app.ifood import models
from datetime import *

@task()
def request_timeout():
    print('Hello World!')

<<<<<<< HEAD

@periodic_task(crontab(minute='*/1'))
def timeout_task():
    queryset = models.Request.objects.all()

    for request in queryset.values():
        requested_at = request['created_at']
        print(requested_at)
        requested_day = int(str(requested_at)[8:10])
        print(requested_day)
        requested_month = int(str(requested_at)[5:7])
        print(requested_month)
        requested_year = int(str(requested_at)[0:4])
        print(requested_year)
        requested_hour = int(str(requested_at)[11:13])
        print(requested_hour)
        requested_minute = int(str(requested_at)[14:16])
        print(requested_minute)

        now = datetime.now()
        print(now)
        now_day = int(str(now)[8:10])
        print(now_day)
        now_month = int(str(now)[5:7])
        print(now_month)
        now_year = int(str(now)[0:4])
        print(now_year)
        now_hour = int(str(now)[11:13])
        print(now_hour)
        now_minute = int(str(now)[14:16])
        print(now_minute)

        if (requested_day-now)
        print(requested_day - now_day)

        # print(str(requested_at)[0:19])
        # print(now)

    # print(requested_at)
    # print(now)
    # print(queryset['status'])
=======
@periodic_task(crontab(minute='*/1'))
def vai_acabar():
    print('Every one minute this will be printed by the consumer')
>>>>>>> 1048e61a8adc48e6c03333e7644b269b6175695b

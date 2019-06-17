from huey import crontab
from huey.contrib.djhuey import periodic_task, task
from app.ifood import models
from datetime import *
from django.core.mail import EmailMessage
from django.http import HttpResponse

@task()
def send_simple_email():
    email = EmailMessage("Hub", "TESTE HUB INTELIGÊNCIA ARTIFICIAL <-autoindexError-> ##404 - 403 IFPB.edu.br {}".format(index), to=['nicolasnekar@gmail.com'])
    email.send()

@periodic_task(crontab(minute='*/1'))
def timeout_task():
    queryset = models.Request.objects.all()

    for request in queryset.values():
        requested_at = request['created_at']
        print(requested_at)
        requested_day = int(str(requested_at)[8:10])
        requested_month = int(str(requested_at)[5:7])
        requested_year = int(str(requested_at)[0:4])
        requested_hour = int(str(requested_at)[11:13])
        requested_minute = int(str(requested_at)[14:16])

        now = datetime.now()
        now_day = int(str(now)[8:10])
        now_month = int(str(now)[5:7])
        now_year = int(str(now)[0:4])
        now_hour = int(str(now)[11:13])
        now_minute = int(str(now)[14:16])
        
        if (request['status'] == 1):
            if ((now_day - requested_day) == 2):
                if ((now_month - requested_month)==0):
                    if ((now_year - requested_year) == 0):
                        if((now_hour - requested_hour) >= 0):
                            if((now_minute - requested_minute) >= 0):
                                    models.Request.objects.filter(id=request['id']).update(status=2)

                                

        # print(str(requested_at)[0:19])
        # print(now)

    # print(requested_at)
    # print(now)
    # print(queryset['status'])

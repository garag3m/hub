from huey import crontab
from huey.contrib.djhuey import periodic_task, task
from app.ifood import models
from datetime import *
from django.core.mail import EmailMessage
from django.http import HttpResponse

@task()
def send_simple_email(title, message, addressee):
    email = EmailMessage(title, message, to=[addressee])
    email.send()

@periodic_task(crontab(minute='*/1'))
def timeout_task():
    queryset = models.Request.objects.all()

    for request in queryset.values():
        requested_at = request['created_at']
        now = datetime.now()
        
        if (request['status'] == 1):
            if ((now.day- requested_at.day) == 2):
                if ((now.month - requested_at.month)==0):
                    if ((now.year - requested_at.year) == 0):
                        if((now.hour - requested_at.hour) >= 0):
                            if((now.minute - requested_at.minute) >= 0):
                                models.Request.objects.filter(id=request['id']).update(status=2)

                                
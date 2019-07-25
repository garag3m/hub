from huey.contrib.djhuey import task
from app.ctrl_p import models
from django.core.mail import EmailMessage

@task()
def send_file_status_email(title, message, addressee):
    email = EmailMessage(title, message, to=[addressee])
    email.send()
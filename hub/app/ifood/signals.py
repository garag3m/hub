from app.ifood.models import Request
from django.db.models.signals import post_save
from app.ifood.tasks import send_simple_email

def create_request(sender, instance, created, **kwargs):
        print("oi")
        send_simple_email()

post_save.connect(create_request, sender=Request)
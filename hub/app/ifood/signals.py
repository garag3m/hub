from app.ifood.models import Request
from django.db.models.signals import post_save
from app.ifood.tasks import send_simple_email

def create_request(sender, instance, created,**kwargs):
        title = "Criação de pedido"
        message="lets see if it works"
        addressee = "adrielhigor@gmail.com"
        send_simple_email(title,message,addressee)

post_save.connect(create_request, sender=Request)
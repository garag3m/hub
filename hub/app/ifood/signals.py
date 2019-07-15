from app.ifood.models import Request
from django.db.models.signals import post_save
from app.ifood.tasks import send_simple_email
from app.core import models

def create_request(sender, instance, created,**kwargs):
        user = instance.teacher
        title = "Criação de pedido"
        message="""
        O pedido de refeição extra foi realizado com sucesso!
        Aguarde a avaliação da requisição. Cordialmente cordenação.
        """
        addressee = user.email
        send_simple_email(title,message,addressee)

post_save.connect(create_request, sender=Request)
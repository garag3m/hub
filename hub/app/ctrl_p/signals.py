from app.ctrl_p.models import File
from django.db.models.signals import post_save
from app.ctrl_p.tasks import send_file_status_email
from app.core import models

def create_file_post_save(sender, instance, created, **kwargs):
    user = instance.user
    adm_address = "hubgarag3m.ifpb@gmail.com"
    addressee = user.email

    if created:
        #Email sent to user whenever a File is sent
        title = "Impressão requisitada com sucesso!"
        message = (f"""
        A requisição de impressão de {instance.name} foi recebida.
        """) 
        send_file_status_email(title, message, addressee)
    else:
        #Email sent to user whenever a File is updated
        title = "Impressão atualizada com sucesso!"
        message = (f"""
        A atualização da impressão de {instance.name} foi recebida.
        """) 
        send_file_status_email(title, message, addressee)

    
post_save.connect(create_file_post_save, sender=File)
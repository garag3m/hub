from app.ifood.models import Request
from django.db.models.signals import post_save
from app.ifood.tasks import send_request_status_email
from app.core import models


def create_request_post_save(sender, instance, created, **kwargs):
    user = instance.teacher
    adm_address = "hubgarag3m.ifpb@gmail.com"#"caest.ifpbcz@gmail.com"
    addressee = user.email
    
    if created:
        #Email sent to user whenever a request is created
        title = "Criação de pedido"
        message = """
        O pedido de refeição extra foi realizado com sucesso!
        Aguarde a avaliação da requisição. Cordialmente cordenação.
        """
        send_request_status_email(title, message, addressee)
        
        #Email sent to admin whenever a request is created
        adm_title = "Um novo pedido recebido"
        adm_message = (f"""
        Um novo pedido de refeição foi feito pelo usuário {user.username}.
        Pedido aguarda avaliação.
        """)
        send_request_status_email(adm_title, adm_message, adm_address)
    else:
        if instance.status == 1:
            print('eu sou 1')
        elif instance.status == 2:
            print('eu sou 2')
        else:
            print('eu sou 3')
        #Email sent to user whenever a request is updated
        # title = "Alteração de pedido"
        # message = """
		# O pedido de refeição extra foi atualizado com sucesso!
		# Aguarde a avaliação da requisição. Cordialmente cordenação.
		# """
        # send_request_status_email(title, message, addressee)

        #Email sent to admin whenever a request is updated
        # adm_title = "Uma nova alteração de pedido recebida"
        # adm_message = (f"""
        # Um pedido de refeição foi atualizado pelo usuário {user.username}.
        # Pedido aguarda avaliação das novas diretrizes.
        # """)
        # send_request_status_email(adm_title, adm_message, adm_address)

post_save.connect(create_request_post_save, sender=Request)

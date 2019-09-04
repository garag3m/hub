from app.cere import models, tasks
from django.db.models.signals import post_save

def create_company_post_save(sender, instance, created, **kwargs):
    tasks.agreement(instance)

def create_document_opinion_post_save(sender, instance, created, **kwargs):
    tasks.document_opinion(instance)



post_save.connect(create_company_post_save, sender=models.Company)
post_save.connect(create_document_opinion_post_save, sender=models.Document_opinion)
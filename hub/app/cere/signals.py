from app.cere import models, tasks
from django.db.models.signals import post_save

def create_company_post_save(sender, instance,created, **kwargs):
    tasks.agreement()

post_save.connect(create_company_post_save, sender=models.Company)
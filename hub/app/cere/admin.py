from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.Address)
admin.site.register(models.Document_opinion)
admin.site.register(models.Stage)
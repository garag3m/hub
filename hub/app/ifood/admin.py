from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Request)
admin.site.register(models.StudentMeal)
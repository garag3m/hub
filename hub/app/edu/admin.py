from django.contrib import admin

from . import models

class StudentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'registration')
    ordering = ('registration',)

# Register your models here.
admin.site.register(models.Student, StudentAdmin)
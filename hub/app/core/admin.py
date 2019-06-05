from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import UUIDUser

admin.site.register(UUIDUser)
from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import UUIDUser, Address

admin.site.register(UUIDUser)
admin.site.register(Address)

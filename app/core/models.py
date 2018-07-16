# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    # core
    cpf = models.CharField(max_length=11, null=True, blank=True, verbose_name="CPF")
    registration = models.CharField(max_length=100, null=True, blank=True, verbose_name="matrícula")

    # picture
    picture = models.ImageField(null=False, blank=True, verbose_name='picture', upload_to='accounts/%Y/%m/%d')
    picture_thumb = ImageSpecField(source='picture', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

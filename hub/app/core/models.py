import uuid

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Permission, GroupManager

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


# Address
# - - - - - - - - - - - - - - - - - - -
class Address(CreateUpdateModel):

    TYPE_CHOICES = (
        (1, 'Profissional'),
        (2, 'Residencial'),
        (3, 'Outros')
    )

    city = models.CharField(max_length=30, verbose_name='Cidade')
    neighborhood = models.CharField(max_length=30, verbose_name='Bairro')
    street = models.CharField(max_length=30, verbose_name='Rua')
    number = models.CharField(max_length=10, verbose_name='Número')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    state = models.CharField(max_length=2, verbose_name='Estado')
    country = models.CharField(max_length=60, verbose_name='País')
    name = models.CharField(max_length=100, verbose_name='Nome')
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name='Tipo de Endereço')

    def __str__(self):
        return self.city + ' ' + self.neighborhood + ' ' + self.street + '-' + self.number

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)

    # picture
    picture = models.ImageField(null=False, blank=True, verbose_name='picture', upload_to='accounts/%Y/%m/%d')
    picture_thumb = ImageSpecField(source='picture', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

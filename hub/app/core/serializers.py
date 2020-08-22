from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from . import models


# Address serializer
# - - - - - - - - - - - - - - - - - - -
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = (
            'pk',
            'city',
            'neighborhood',
            'street',
            'number',
            'cep',
            'state',
            'country',
            'name',
            'type'
        )


# UUIDUser serializer
# - - - - - - - - - - - - - - - - - - -
class UUIDUserSerializer(serializers.HyperlinkedModelSerializer):

    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key

    class Meta:
        model = models.UUIDUser
        fields = ('pk', 'username', 'first_name', 'last_name', 'token')


# UUIDUser simple serializer
# - - - - - - - - - - - - - - - - - - -
class UUIDUserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    # Methods
    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key

    def validate_password(self, value):
        validate_password(value)
        return make_password(value)

    class Meta:
        model = models.UUIDUser
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'password', 'token')


# UUIDUser simple serializer
# - - - - - - - - - - - - - - - - - - -
class UUIDUserSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UUIDUser
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'address')

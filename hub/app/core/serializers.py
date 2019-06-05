from rest_framework import serializers

from . import models


# UUIDUser serializer
# - - - - - - - - - - - - - - - - - - -
class UUIDUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UUIDUser
        fields = ('id', 'username')

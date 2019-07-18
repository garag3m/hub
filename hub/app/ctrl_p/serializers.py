from rest_framework import serializers

from . import models

class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.File
        fields = ('pk', 'user', 'name', 'copy', 'status')
from rest_framework import serializers

from . import models

class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.File
        fields = ('pk', 'user','name', 'copy', 'status')

# class CreateFileSerializer(serializers.ModelSerializer):
#     pk = serializers.UUIDField(read_only=True)
#     name = serializers.CharField(write_only = True)

#     class Meta:
#         model = models.File
#         fields = ('pk') 
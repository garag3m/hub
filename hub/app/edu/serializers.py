from rest_framework import serializers

from . import models


# Student serializer
# - - - - - - - - - - - - - - - - - - -
class StudentSerializer(serializers.ModelSerializer):

    course = serializers.CharField(write_only=True)
    status = serializers.CharField(write_only=True)
    registration = serializers.CharField(write_only=True)

    class Meta:
        model = models.Student
        fields = ('pk', 'name', 'course', 'status', 'registration')

from rest_framework import serializers

from . import models


# Student serializer
# - - - - - - - - - - - - - - - - - - -
class StudentSerializer(serializers.ModelSerializer):

    course = serializers.CharField()
    status = serializers.CharField()
    registration = serializers.CharField()

    class Meta:
        model = models.Student
        fields = ('pk', 'name', 'course', 'status', 'registration', 'is_valid')

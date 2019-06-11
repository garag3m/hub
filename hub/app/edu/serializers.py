from rest_framework import serializers

from . import models


# Student serializer
# - - - - - - - - - - - - - - - - - - -
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = ('pk', 'name', 'course', 'registration')

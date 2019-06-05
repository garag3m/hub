from rest_framework import serializers

from . import models


# Request serializer
# - - - - - - - - - - - - - - - - - - -
class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Request
        fields = ('id', 'students', 'date', 'type', 'status', 'justification_teacher', 'justification_CAEST', 'teacher', 'evaluator')

class StudentMealSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentMeal
        fields = ('student' ,'date', 'type')
from rest_framework import serializers

from . import models

from app.core.models import UUIDUser
from app.core.serializers import UUIDUserSerializer

from app.edu.models import Student
from app.edu.serializers import StudentSerializer


# Request serializer
# - - - - - - - - - - - - - - - - - - -
class RequestSerializer(serializers.ModelSerializer):
    
    students = StudentSerializer(many=True)

    class Meta:
        model = models.Request
        fields = ('pk', 'students', 'date', 'type', 'status', 'justification_teacher', 'justification_CAEST')


class CreateRequestSerializer(serializers.ModelSerializer):

    pk = serializers.UUIDField(read_only=True)
    students = StudentSerializer(many=True, read_only=True)
    student_list = serializers.CharField(write_only=True)
    type = serializers.ChoiceField(choices=models.Request.STATUS)

    def create(self, validated_data):
        students = validated_data.pop('student_list').split(',')
        request = models.Request.objects.create(**validated_data, teacher=self.context['request'].user)
        request.students.set(students)
        return RequestSerializer(request).data
    
    class Meta:
        model = models.Request
        fields = ('pk', 'students', 'student_list', 'date', 'type', 'justification_teacher')


class StudentMealSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = models.StudentMeal
        fields = ('student' ,'date', 'type')
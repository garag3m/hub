from rest_framework import serializers

from . import models

from app.core.models import UUIDUser
from app.core.serializers import UUIDUserSerializer

from rest_framework.utils import model_meta

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
        for pk in students:
            print(request.pk)
            smvalited_data = {'request': request.pk, 'student': pk, 'date': request.date, 'type': request.type}
            StudentMealSerializer.create(self, validated_data)
        return RequestSerializer(request).data

    def update(self, instance, validated_data):
        print(validated_data)
        students = validated_data.get('student_list').split(',')
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr == 'student_list':
                instance.students.set(students)
            else:
                setattr(instance, attr, value)
        instance.save()

        return instance

    # Determine the fields to apply...
    
    class Meta:
        model = models.Request
        fields = ('pk', 'students', 'student_list', 'date', 'type', 'justification_teacher')


class StudentMealSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = models.StudentMeal
        fields = ('student' ,'date', 'type')
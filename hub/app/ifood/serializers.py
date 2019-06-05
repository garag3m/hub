from rest_framework import serializers
from app.edu.serializers import StudentSerializer
from app.core.serializers import UUIDUserSerializer
from app.edu.models import Student
from app.core.models import UUIDUser
from . import models



# Request serializer
# - - - - - - - - - - - - - - - - - - -
class RequestSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    teacher = UUIDUserSerializer()
    evaluator = UUIDUserSerializer()

    class Meta:
        model = models.Request
        fields = ('id', 'students', 'date', 'type', 'status', 'justification_teacher', 'justification_CAEST', 'teacher', 'evaluator')

    def students_builder(self, students, request):
        for student in students:
            st = Student.objects.create(**student)
            request.students.add(st)

    def create(self, validated_data):
        students = validated_data['students']
        del validated_data['students']

        teacher = validated_data['teacher']
        del validated_data['teacher']

        evaluator = validated_data['evaluator']
        del validated_data['evaluator']

        req = models.Request.objects.create(**validated_data)
        self.students_builder(students, req)

        tch = UUIDUser.objects.create(**teacher)
        req.teacher = tch

        evl = UUIDUser.objects.create(**evaluator)
        req.evaluator = evl

        req.save()

        return req

class StudentMealSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = models.StudentMeal
        fields = ('student' ,'date', 'type')
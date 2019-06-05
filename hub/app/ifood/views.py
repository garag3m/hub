from rest_framework import viewsets, permissions
from . import models, serializers

# Request viewset
# - - - - - - - - - - - - - - - - - - -
class RequestViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.RequestSerializer

    def get_queryset(self):
        students = self.request.query_params.get('students', None)
        date = self.request.query_params.get('date', None)
        type = self.request.query_params.get('type', None)
        status = self.request.query_params.get('status', None)
        teacher = self.request.query_params.get('teacher', None)
        queryset = models.Request.objects.all()

        if students:
            queryset = queryset.filter(students=students)
        if date:
            queryset = queryset.filter(date__icontains=date)
        if type:
            queryset = queryset.filter(type__icontains=type)
        if status:
            queryset = queryset.filter(status__icontains=status)
        if teacher:
            queryset = queryset.filter(teacher=teacher)
        return queryset

# StudentMeal viewset
# - - - - - - - - - - - - - - - - - - -
class StudentMealViewSet(viewsets.ModelViewSet):

    queryset = models.StudentMeal.objects.all()
    serializer_class = serializers.StudentMealSerializer
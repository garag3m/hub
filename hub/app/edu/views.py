from rest_framework import viewsets, permissions
from . import models, serializers

# Student viewset
# - - - - - - - - - - - - - - - - - - -
class StudentViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        course = self.request.query_params.get('course', None)
        status = self.request.query_params.get('status', None)
        registration = self.request.query_params.get('registration', None)
        queryset = models.Student.objects.all()

        if name:
            queryset = queryset.filter(name__icontains=name)
        if course:
            queryset = queryset.filter(course__icontains=course)
        if status:
            queryset = queryset.filter(status__icontains=status)
        if registration:
            queryset = queryset.filter(registration=registration)
        return queryset
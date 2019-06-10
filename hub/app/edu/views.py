from rest_framework import viewsets, permissions
from django.db.models import Q
from . import models, serializers

# Student viewset
# - - - - - - - - - - - - - - - - - - -
class StudentViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        name = self.request.query_params.get('name', None)
        course = self.request.query_params.get('course', None)
        status = self.request.query_params.get('status', None)
        registration = self.request.query_params.get('registration', None)
        valid = self.request.query_params.get('valid', None)
        queryset = models.Student.objects.all()
        
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(course__icontains=search) | Q(status__icontains=search) | Q(registration__icontains=search))
        else:
            if name:
                queryset = queryset.filter(name__icontains=name)
            if course:
                queryset = queryset.filter(course__icontains=course)
            if status:
                queryset = queryset.filter(status__icontains=status)
            if registration:
                queryset = queryset.filter(registration=registration)
            if valid:
                queryset = queryset.filter(is_valid=valid)
        return queryset
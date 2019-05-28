from rest_framework import viewsets, permissions

from . import models, serializers

# Student viewset
# - - - - - - - - - - - - - - - - - - -
class StudentViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
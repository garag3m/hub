from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from . import models, serializers

# UUIDUser viewset
# - - - - - - - - - - - - - - - - - - -
class UUIDUserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UUIDUserSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        groups = self.request.query_params.get('groups', None)
        queryset = models.UUIDUser.objects.all()
         
        if username:
            queryset = queryset.filter(username__icontains=username)
        if groups:
            queryset = queryset.filter(groups=groups)
        return queryset
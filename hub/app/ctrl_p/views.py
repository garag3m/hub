from rest_framework import viewsets, permissions, status
from django.shortcuts import render
from django.db.models import Q
from . import models, serializers

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FileSerializer
    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        user = self.request.query_params.get('user', None)
        name = self.request.query_params.get('name', None)
        status = self.request.query_params.get('status', None)
        queryset = models.File.objects.all()

        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(status__icontains=search))
        else:
            if user:
                queryset = queryset.filter(user=user) 
            if name:
                queryset = queryset.filter(name__icontains=name) 
            if status:
                queryset = queryset.filter(status__icontains=status)

        return queryset
        

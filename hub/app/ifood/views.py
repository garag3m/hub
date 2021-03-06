from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from . import models, serializers


# Request viewset
# - - - - - - - - - - - - - - - - - - -
class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RequestSerializer
    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        students = self.request.query_params.get('students', None)
        date = self.request.query_params.get('date', None)
        type = self.request.query_params.get('type', None)
        status = self.request.query_params.get('status', None)
        teacher = self.request.query_params.get('teacher', None)
        queryset = models.Request.objects.all()

        if search:
            queryset = queryset.filter(Q(date__icontains=search) | Q(type__icontains=search) | Q(status__icontains=search))
        else:                                                                                                                                                                        
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
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if (instance.status==1):
            return super(RequestViewSet, self).update(request, *args, **kwargs)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if (instance.status==1):
            return super(RequestViewSet, self).destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            if self.request.user.is_superuser:
                return serializers.RequestSerializer
            return serializers.RequestSerializer
        return serializers.CreateRequestSerializer
    
# StudentMeal viewset
# - - - - - - - - - - - - - - - - - - -
class StudentMealViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.StudentMealSerializer
    
    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        student = self.request.query_params.get('student', None)
        date = self.request.query_params.get('date', None)
        type = self.request.query_params.get('type', None)
        queryset = models.StudentMeal.objects.all()

        if search:
            queryset = queryset.filter(Q(student__icontains=search) | Q(date__icontains=search) | Q(type__icontains=search))
        else:                                                                                                                                                                        
            if student:
                queryset = queryset.filter(students=students)
            if date:
                queryset = queryset.filter(date__icontains=date)
            if type:
                queryset = queryset.filter(type__icontains=type)
        return queryset

    
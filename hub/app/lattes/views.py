from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . import serializers


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = models.Institute.objects.all()
    serializer_class = serializers.InstituteSerializer


class AcademicEducationViewSet(viewsets.ModelViewSet):
    queryset = models.AcademicEducation.objects.all()
    serializer_class = serializers.AcademicEducationSerializer


class ComplementaryEducationViewSet(viewsets.ModelViewSet):
    queryset = models.ComplementaryEducation.objects.all()
    serializer_class = serializers.ComplementaryEducationSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class ProfessionalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = models.ProfessionalPerformance.objects.all()
    serializer_class = serializers.ProfessionalPerformanceSerializer


class TeachingProjectsViewSet(viewsets.ModelViewSet):
    queryset = models.TeachingProjects.objects.all()
    serializer_class = serializers.TeachingProjectsSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer


class AwardsViewSet(viewsets.ModelViewSet):
    queryset = models.Awards.objects.all()
    serializer_class = serializers.AwardsSerializer


class ProductionsViewSet(viewsets.ModelViewSet):
    queryset = models.Productions.objects.all()
    serializer_class = serializers.ProductionsSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventsSerializer


class CTViewSet(viewsets.ModelViewSet):
    queryset = models.CT.objects.all()
    serializer_class = serializers.CTSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    @action(detail=True, methods=['get'])
    def academic_education(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.AcademicEducationSerializer(person.academic_education.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def complementary_education(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.ComplementaryEducationSerializer(person.complementary_education.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def professional_performance(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.ProfessionalPerformanceSerializer(person.professional_performance.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def teaching_projects(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.TeachingProjectsSerializer(person.teaching_projects.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def language(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.LanguageSerializer(person.language.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def award(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.AwardsSerializer(person.award.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def productions(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.ProductionsSerializer(person.productions.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.EventsSerializer(person.events.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def ct(self, request, pk=None):
        person = self.get_object()
        serializer = serializers.CTSerializer(person.ct.all(), many=True)
        return Response(serializer.data)

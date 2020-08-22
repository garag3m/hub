from rest_framework import serializers

from . import models


class InstituteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Institute
        fields = (
            'pk',
            'name',
            'url_homepage',
            'address',
            'get_address'
        )


class AcademicEducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AcademicEducation
        fields = (
            'pk',
            'start_date',
            'conclusion_date',
            'get_conclusion_date',
            'graduation_level',
            'graduation_choice',
            'graduation',
            'institution',
            'get_institution',
            'title',
            'advisor',
            'observations',
            # 'file'
        )


class ComplementaryEducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ComplementaryEducation
        fields = (
            'pk',
            'start_date',
            'conclusion_date',
            'get_conclusion_date',
            'graduation_level',
            'institution',
            'get_institution',
            # 'file'
        )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = (
            'pk',
            'start_date',
            'conclusion_date',
            'get_conclusion_date',
            'title',
            'about',
            # 'file'
        )


class ProfessionalPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfessionalPerformance
        fields = (
            'pk',
            'institution',
            'get_institution',
            'start_date',
            'conclusion_date',
            'get_conclusion_date',
            'bond',
            'occupation',
            'workload',
            'regime',
            'tasks',
            'tasks_list',
            'occupation_area'
        )


class TeachingProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TeachingProjects
        fields = (
            'pk',
            'start_date',
            'conclusion_date',
            'get_conclusion_date',
            'title',
            'about',
            # 'file'
        )


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Language
        fields = (
            'pk',
            'language_name',
            'get_language',
            'reading_level',
            'writing_level',
            'speech_level',
            'understanding_level',
            'reading_choice',
            'writing_choice',
            'speech_choice',
            'understanding_choice'
        )


class AwardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Awards
        fields = (
            'pk',
            'year',
            'award_name',
            # 'file'
        )


class ProductionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Productions
        fields = (
            'pk',
            'type',
            'type_choice',
            'header',
            'reference',
            # 'file'
        )


class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Events
        fields = (
            'pk',
            'choice',
            'type',
            'name',
            'choice_choice',
            'type_choice',
        )


class CTSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CT
        fields = (
            'pk',
            'title',
        )


class PersonSerializer(serializers.ModelSerializer):
    get_picture = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = models.Person
        fields = (
            'pk',
            'get_picture',
            'id_lattes',
            'academic_education',
            'complementary_education',
            'professional_performance',
            'teaching_projects',
            'languages',
            'award',
            'productions',
            'events',
            'ct',
            'get_name',
            'about',
            'get_academic_education',
            'get_complementary_education',
            'get_complementary_education',
            'get_professional_performance',
            'get_teaching_projects',
            'get_languages',
            'get_award',
            'get_productions',
            'get_events',
            'get_ct',
            'other_informations'
        )

from django.contrib import admin

from .models import *


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id_lattes',)


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    pass


@admin.register(AcademicEducation)
class AcademicEducationAdmin(admin.ModelAdmin):
    pass


@admin.register(ComplementaryEducation)
class ComplementaryEducationAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfessionalPerformance)
class ProfessionalPerformanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(TeachingProjects)
class PTeachingProjectsAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Awards)
class AwardAdmin(admin.ModelAdmin):
    pass


@admin.register(Productions)
class ProductionAdmin(admin.ModelAdmin):
    pass


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(CT)
class CTAdmin(admin.ModelAdmin):
    pass

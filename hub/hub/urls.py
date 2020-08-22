"""hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from app.core import views as core
from app.edu import views as edu
from app.ifood import views as ifood
from app.cere import views as cere
from app.ctrl_p import views as ctrl_p
from app.lattes import views as lattes

router = routers.DefaultRouter()

router.register(r'users', core.UUIDUserViewSet, base_name='api-core')
router.register(r'students', edu.StudentViewSet, base_name='api-student')
router.register(r'meals', ifood.StudentMealViewSet, base_name='api-meal')
router.register(r'requests', ifood.RequestViewSet, base_name='api-request')
router.register(r'companys', cere.CompanyViewSet, base_name='api-company')
router.register(r'document-opinions', cere.Document_opinionViewSet, base_name='api-document_opinion')
router.register(r'address', core.AddressViewSet, base_name='api-address')
router.register(r'stages', cere.StageViewSet, base_name='api-stage')
router.register(r'files', ctrl_p.FileViewSet, base_name='api-files')

router.register(r'lattes/institute', lattes.InstituteViewSet, base_name='api-institutes')
router.register(r'lattes/academic-education', lattes.AcademicEducationViewSet, base_name='api-academic-education')
router.register(r'lattes/complementary-education', lattes.ComplementaryEducationViewSet,
                base_name='api-complementary-education')
router.register(r'lattes/task', lattes.TaskViewSet, base_name='api-task')
router.register(r'lattes/professional-performance', lattes.ProfessionalPerformanceViewSet,
                base_name='api-professional-performance')
router.register(r'lattes/teaching-projects', lattes.TeachingProjectsViewSet, base_name='api-teaching-projects')
router.register(r'lattes/languages', lattes.LanguageViewSet, base_name='api-languages')
router.register(r'lattes/awards', lattes.AwardsViewSet, base_name='api-awards')
router.register(r'lattes/productions', lattes.ProductionsViewSet, base_name='api-productions')
router.register(r'lattes/events', lattes.EventsViewSet, base_name='api-events')
router.register(r'lattes/ct', lattes.CTViewSet, base_name='api-ct')
router.register(r'lattes/person', lattes.PersonViewSet, base_name='api-person')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', core.AuthToken.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

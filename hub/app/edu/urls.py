from django.urls import path

from rest_framework import routers

from . import views

app_name = 'edu'

router = routers.DefaultRouter()

router.register(r'student', views.StudentViewSet, base_name='api-student')

urlpatterns = router.urls
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
from app.core.views import UUIDUserViewSet
from app.edu.views import StudentViewSet
from app.ifood.views import RequestViewSet
from app.ifood.views import StudentMealViewSet

router = routers.DefaultRouter()

router.register(r'student', StudentViewSet, base_name='api-student')
router.register(r'request', RequestViewSet, base_name='api-request')
router.register(r'meal', StudentMealViewSet, base_name='api-meal')
router.register(r'user', UUIDUserViewSet, base_name='api-core')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

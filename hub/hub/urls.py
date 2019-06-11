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

router = routers.DefaultRouter()

router.register(r'user', core.UUIDUserViewSet, base_name='api-core')
router.register(r'student', edu.StudentViewSet, base_name='api-student')
router.register(r'meal', ifood.StudentMealViewSet, base_name='api-meal')
router.register(r'request', ifood.RequestViewSet, base_name='api-request')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', core.AuthToken.as_view()),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

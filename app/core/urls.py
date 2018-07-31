# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as core

app_name = 'core'

urlpatterns = [

    # Login
    # https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.views.LoginView
    path('login/', auth_views.LoginView.as_view(template_name='core/user/auth.html'), name='login'),

    # Logout
    # https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.views.LogoutView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Users
    path('usuarios/', core.UsersView.as_view(), name='users-list'),
    path('usuarios/novo/', core.UserCreateView.as_view(), name='user-create'),
    path('usuarios/<uuid:pk>/editar/', core.UserEditView.as_view(), name='user-edit'),
    
    # Dashboard
    path('dashboard/', core.DashboardView.as_view(), name='dashboard'),

]

# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models

# Dashboard
# https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#templateview
# - - - - - - - - - - - - - - - - - - -
class DashboardView(TemplateView):

    template_name = 'core/dashboard.html'


# Users list view
# - - - - - - - - - - - - - - - - - - -
class UsersView(ListView):

    model = models.UUIDUser
    template_name = 'core/user/list.html'


# User create
# - - - - - - - - - - - - - - - - - - -
class UserCreateView(CreateView):

    model = models.UUIDUser
    template_name = 'core/user/form.html'
    success_url = reverse_lazy('core:user-list')
    fields = ['first_name', 'last_name', 'password', 'email', 'cpf', 'registration', 'picture']


# User edit
# - - - - - - - - - - - - - - - - - - -
class UserEditView(UpdateView):

    model = models.UUIDUser
    template_name = 'core/user/update.html'
    success_url = reverse_lazy('core:user-list')
    fields = ['first_name', 'last_name', 'password', 'email', 'cpf', 'registration', 'picture']
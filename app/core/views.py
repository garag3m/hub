# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from . import models

# Dashboard
# https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#templateview
# - - - - - - - - - - - - - - - - - - -
class DashboardView(TemplateView):

    template_name = 'core/dashboard.html'


class UsersView(ListView):

    model = models.UUIDUser
    template_name = 'core/user/list.html'
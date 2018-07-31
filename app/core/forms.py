#coding:utf-8
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UUIDUser

# User: create
class UUIDUserForm(forms.ModelForm):

    def save(self, commit=True):
        user = super(UUIDUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = UUIDUser
        fields = ('username', 'first_name', 'email', 'password')
        labels = {
            'username': 'Login',
            'first_name': 'Nome completo',
            'email': 'Email',
        }
        widgets={
            'password': forms.PasswordInput()
        }

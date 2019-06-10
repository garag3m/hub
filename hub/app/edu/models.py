from django.db import models

from app.core import models as core


# Student
# - - - - - - - - - - - - - - - - - - -
class Student(core.CreateUpdateModel):

    name = models.CharField(max_length=100, verbose_name='Nome')
    course = models.CharField(max_length=100, verbose_name='Curso')
    status = models.CharField(max_length=100, verbose_name='Situação')
    registration = models.CharField(max_length=100, verbose_name='Matrícula', unique=True)

    @property
    def valid(self):
        if self.status == 'Matriculado':
            return True
        else:
            return False

    def __str__(self):
        return f'{self.name} ({self.registration})'

    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'
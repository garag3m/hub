from django.db import models

from app.core import models as core
from app.edu import models as edu


class Request(core.CreateUpdateModel):

    STATUS = (
        (1, 'Em andamento'),
        (2, 'Aprovado'),
        (3, 'Reprovado')
    )

    TYPE = (
        (1, 'Almoço'),
        (2, 'Janta')
    )

    students = models.ManyToManyField(edu.Student, related_name='request')
    date = models.DateField()
    type = models.IntegerField(choices=TYPE, verbose_name='Tipo de refeição')
    status = models.IntegerField(choices=STATUS, verbose_name='Estado do pedido', default=1)
    justification_teacher = models.TextField(verbose_name='Justificativa do professor')
    justification_CAEST = models.TextField(verbose_name='Justificativa da CAEST', blank=True, null=True)
    teacher = models.ForeignKey(core.UUIDUser, on_delete=models.CASCADE, verbose_name='Professor', related_name='request_teacher')
    evaluator = models.ForeignKey(core.UUIDUser, on_delete=models.CASCADE, verbose_name='Avaliador', related_name='request_evaluator', blank=True, null=True)
    
    @property
    def students_string(self):
        string = ''
        for student in self.students.all():
            string += str(student.pk) + ','
        return string

    @property
    def students_amount(self):
        return len(self.students.all())

    @property
    def teacher_name(self):
        return self.teacher.first_name

    @property
    def type_name(self):
        if self.type == 1:
            return 'Almoço'
        elif self.type == 2:
            return 'Janta'

    @property
    def status_name(self):
        if self.status == 1:
            return 'Em andamento'
        elif self.status == 2:
            return 'Aprovado'
        elif self.status == 3:
            return 'Negado'

    @property
    def formated_date(self):
        d = str(self.date)
        return d[8:10] + '/' + d[5:7] + '/' + d[0:4]

    def __str__(self):
        return f'{self.teacher} {self.status}'
                                                                                                                                                                                                                                                                                    
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'


class StudentMeal(core.CreateUpdateModel):

    TYPE = (
        (1, 'Almoço'),
        (2, 'Janta')
    )

    STATUS = (
        (1, 'Presença'),
        (2, 'Ausência')
    )

    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='refeição', null=True)
    student = models.ForeignKey(edu.Student, on_delete=models.CASCADE, related_name='refeição')
    date = models.DateField()
    type = models.IntegerField(choices=TYPE, verbose_name='Tipo de refeição')
    attendance = models.IntegerField(choices=STATUS, verbose_name='Status de presença', null=True, blank=True)

    @property
    def student_name(self):
        return self.student.name

    @property
    def formated_date(self):
        d = str(self.date)
        return d[8:10] + '/' + d[5:7] + '/' + d[0:4]

    @property
    def type_name(self):
        if self.type == 1:
            return 'Almoço'
        elif self.type == 2:
            return 'Janta'

    def __str__(self):
        return f'{self.student} {self.date} {self.type}'

    class Meta:
        unique_together = [['student', 'date', 'type']]
        verbose_name = 'refeição'
        verbose_name_plural = 'refeições'
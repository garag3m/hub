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
    evaluator = models.ForeignKey(core.UUIDUser, on_delete=models.CASCADE, verbose_name='Avaliador',
                                    related_name='request_evaluator', blank=True, null=True)
    
    def __str__(self):
        return f'{self.justification_teacher} {self.status}'

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

class StudentMeal(core.CreateUpdateModel):
    TYPE = (
        (1, 'Almoço'),
        (2, 'Janta')
    )
    student = models.ForeignKey(edu.Student, on_delete=models.CASCADE, related_name='refeição')
    date = models.DateField()
    type = models.IntegerField(choices=TYPE, verbose_name='Tipo de refeição')

    def __str__(self):
        return f'{self.student} {self.date} {self.type}'

    class Meta:
        unique_together = [['student', 'date', 'type']]
        verbose_name = 'refeição'
        verbose_name_plural = 'refeições'
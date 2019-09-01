from django.db import models

from app.core import models as core

# Model referente aos arquivos enviados para impressão
class File(core.CreateUpdateModel):

    STATUS = (
      (1,'Aguardando Impressão'),
      (2,'Impressão Concluída'),
      (3,'Impressão Recusada')
    )

    user = models.ForeignKey(core.UUIDUser, on_delete=models.CASCADE, related_name='users', verbose_name='Usuário')
    name = models.CharField(max_length=20, verbose_name='Nome')
    copy = models.IntegerField(verbose_name='Número de Cópias')
    file = models.FileField(upload_to='documents/', verbose_name='Arquivo')
    status = models.IntegerField(choices=STATUS, verbose_name='Status de Impressão', default=1)

    def __str__(self):
      return self.name

    class Meta:
      verbose_name = 'Arquivo'
      verbose_name_plural = 'Arquivos'



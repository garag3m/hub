from django.db import models

from app.core import models as core

# Model referente aos arquivos enviados para impressão
class File(core.CreateUpdateModel):

<<<<<<< HEAD
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
=======
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

  @property
  def user_name(self):
    return self.user.first_name

  @property
  def status_name(self):
    if self.status == 1:
      return 'Aguardando Impressão'
    elif self.status == 2:
      return 'Impressão Concluída'
    elif self.status == 3:
      return 'Impressão Recusada'

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Arquivo'
    verbose_name_plural = 'Arquivos'
>>>>>>> 57d747d39991f8c173d213bc0ce6e9064f0e61c3



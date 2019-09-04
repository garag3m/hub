from django.db import models

from app.core import models as core
from app.edu import models as edu

# Create your models here.

class Address(core.CreateUpdateModel):
    city= models.CharField(max_length=30, verbose_name='Cidade') 
    neighborhood= models.CharField(max_length=30, verbose_name='Bairro')
    street= models.CharField(max_length=30, verbose_name='Rua')
    number= models.CharField(max_length=10, verbose_name='Número')
    cep= models.CharField(max_length=9, verbose_name='CEP')
    state= models.CharField(max_length=2, verbose_name='Estado')

    def __str__(self):
        return self.city + ' ' + self.neighborhood + ' ' + self.street + '-' + self.number

    class Meta:
        verbose_name= 'Endereço'
        verbose_name_plural='Endereços'

class Company(core.CreateUpdateModel):
    name= models.CharField(max_length=100, verbose_name='Nome')
    cnpj= models.CharField(max_length=17, verbose_name='CNPJ')
    address= models.ForeignKey(Address, on_delete=models.CASCADE, null=True, verbose_name='Endereço')
    owner= models.CharField(max_length=100, verbose_name='Proprietário')
    agreement_number=models.IntegerField(blank=True,verbose_name='Número do convênio')
    cpf_owner=models.CharField(max_length=14,verbose_name='CPF do proprietário')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Empresa'
        verbose_name_plural='Empresas'


class Document_opinion(core.CreateUpdateModel):
    STATUS = (
        (1, 'Deferido'),
        (2, 'Indeferido')
    )

    date= models.DateField(verbose_name='Data')
    process_number= models.IntegerField(unique=True, verbose_name='N° de processo')
    status= models.IntegerField(choices= STATUS, verbose_name='Status')
    company= models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')

    @property
    def formated_date(self):
        d = str(self.date)
        return d[8:10] + '/' + d[5:7] + '/' + d[0:4]

    @property
    def company_name(self):
        return self.company.name

    @property
    def status_name(self):
        if self.status == 1:
            return 'Deferido'
        elif self.status == 2:
            return 'Indeferido'

    def __str__(self):
        return str(self.process_number) + ' ' + self.company.name

    class Meta:
        verbose_name_plural= 'Parecer'
        verbose_name_plural='Pareceres'


class Stage(core.CreateUpdateModel):

    SUPPORT = (
        (1, 'NÃO'),
        (2, 'SIM')
    )

    company= models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    advisor= models.CharField(max_length=100, verbose_name='Orientador')
    supervisor= models.CharField(max_length=100, verbose_name='Supervisor')
    sector= models.CharField(max_length=50, verbose_name='Setor')
    start_date= models.DateField(verbose_name='Data de início')
    end_date= models.DateField(verbose_name='Data final')
    week_hours= models.IntegerField(verbose_name='Horas semanais')
    total_hours= models.IntegerField(verbose_name='Horas totais')
    days= models.CharField(max_length=100, verbose_name='Dias semanais')
    begins=models.CharField(max_length=20, verbose_name='Hora de início')
    ends=models.CharField(max_length=20, verbose_name='Hora final')
    document_secure= models.CharField(max_length=20, verbose_name='Seguro')
    support= models.IntegerField(choices= SUPPORT, verbose_name='auxílio')
    student = models.ForeignKey(edu.Student, on_delete=models.CASCADE, verbose_name='Estudante')

    @property
    def company_name(self):
        return self.company.name

    @property
    def support_label(self):
        if self.support == 1:
            return 'Não'
        elif self.support == 2:
            return ''

    class Meta:
        verbose_name= 'Estágio'
        verbose_name_plural='Estágios'



    
    

    

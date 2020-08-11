import uuid

from django.db import models
from app.core import models as core


def file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Institute(core.CreateUpdateModel):
    name = models.CharField(max_length=100, verbose_name='Instituição')
    url_homepage = models.URLField(blank=True, null=True, verbose_name='URL da página do Instituto')
    adress = models.ForeignKey(core.Address, on_delete=models.CASCADE, verbose_name='Endereco')

    class Meta:
        verbose_name = 'Instituição de Ensino'
        verbose_name_plural = 'Instituições de Ensino'

    def __str__(self):
        return self.name


class AcademicEducation(core.CreateUpdateModel):

    GRADUATION_CHOICES = (
        (1, 'Técnico'),
        (2, 'Graduação'),
        (3, 'Especialização'),
        (4, 'Mestrado'),
        (5, 'Doutorado'),
        (6, 'Pós Doutorado')
    )

    start_date = models.DateField(verbose_name='Data de Início')
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', blank=True, null=True)
    graduation_level = models.IntegerField(choices=GRADUATION_CHOICES, verbose_name='Nível de Graduação')
    graduation = models.CharField(max_length=100, verbose_name='Graduação', null=True)
    institution = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name='Instituição')
    title = models.CharField(max_length=100, blank=True, verbose_name='Título da Publicação')
    advisor = models.CharField(max_length=100, verbose_name='Orientador', blank=True)
    observations = models.TextField(max_length=250, verbose_name='Observações', blank=True)
    file = models.FileField(blank=True)

    class Meta:
        verbose_name = 'Formação Acadêmica/Titulação'

    def __str__(self):
        return f'{self.start_date} - {self.conclusion_date}: {self.graduation_level} em {self.graduation}\n' \
               f'{self.institution}\norientado(a) por {self.advisor}.'


class ComplementaryEducation(core.CreateUpdateModel):
    start_date = models.DateField(verbose_name='Data de Início')
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', blank=True, null=True)
    graduation_level = models.CharField(max_length=100, verbose_name='Graduação')
    institution = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name='Instituição')
    file = models.FileField(blank=True)

    class Meta:
        verbose_name = 'Formação Complementar'

    def __str__(self):
        return f'{self.start_date} - {self.conclusion_date}: {self.graduation_level} em {self.institution}'


class Task(core.CreateUpdateModel):
    start_date = models.DateField(verbose_name='Data de Início')
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    about = models.TextField(max_length=250, verbose_name='Sobre')
    file = models.FileField(blank=True)

    def __str__(self):
        return f'{self.start_date} - {self.conclusion_date} = {self.title}' \
               f'{self.about}'


class ProfessionalPerformance(core.CreateUpdateModel):
    institution = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name='Instituição')
    start_date = models.DateField(verbose_name='Data de Início')
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', blank=True, null=True)
    bond = models.CharField(max_length=100, verbose_name='Vínculo')
    occupation = models.CharField(max_length=100, verbose_name='Enquadramento Funcional')
    workload = models.CharField(max_length=8, verbose_name='Carga Horária')
    regime = models.CharField(max_length=50, verbose_name='Regime', blank=True)
    tasks = models.ManyToManyField(Task, verbose_name='Atividade', blank=True)

    def __str__(self):
        return f'{self.start_date} - {self.conclusion_date} = Vínculo: {self.bond}, ' \
               f'Enquadramento Funcional: {self.occupation}, Carga Horária: {self.workload}, ' \
               f'Regime: {self.regime}'


class TeachingProjects(core.CreateUpdateModel):
    start_date = models.DateField(verbose_name='Data de Início')
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    about = models.TextField(max_length=250, verbose_name='Sobre')
    file = models.FileField(blank=True)

    def __str__(self):
        return f'{self.start_date} - {self.conclusion_date} = {self.title}' \
               f'{self.about}'


class OccupationArea(core.CreateUpdateModel):
    area = models.CharField(max_length=100, verbose_name='Área de Atuação')

    def __str__(self):
        return self.area


class Languages(core.CreateUpdateModel):
    language = models.CharField(max_length=20, verbose_name='Idioma')

    def __str__(self):
        return self.language


class UserLanguage(core.CreateUpdateModel):

    LEVEL_CHOICES = (
        (1, 'Bom'),
        (2, 'Razoável'),
        (3, 'Baixo')
    )

    language = models.ForeignKey(Languages, on_delete=models.CASCADE, verbose_name='Idioma')
    reading_level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Nível de Leitura')
    writing_level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Nível de Escrita')
    speech_level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Nível de Comunicação')
    understanding_level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Nível de Compreensão')

    def __str__(self):
        return f'{self.language}: {self.understanding_level}, {self.speech_level}, {self.reading_level}, ' \
               f'{self.writing_level}'


class Awards(core.CreateUpdateModel):
    year = models.DateField()
    award_name = models.CharField(max_length=100, verbose_name='Prêmio')
    file = models.FileField()

    def __str__(self):
        return self.award_name


class References(core.CreateUpdateModel):
    reference = models.CharField(max_length=400, verbose_name='Referência Bibliográfica da Produção')

    def __str__(self):
        return self.reference


class Productions(core.CreateUpdateModel):

    TYPE_CHOICES = (
        (1, 'Produção Bibliográfica'),
        (2, 'Produção Técnica'),
        (3, 'Demais tipos de Produção')
    )

    header = models.CharField(max_length=100, verbose_name='Cabeçalho (ex: '
                                                           '"Livros publicados/organizados ou edições")')
    reference = models.ManyToManyField(References, verbose_name='Referência Bibliográfica da Produção')
    file = models.FileField(blank=True)

    class Meta:
        verbose_name = 'Produção'
        verbose_name_plural = 'Produções'

    def __str__(self):
        return f'{self.header}'


class Events(core.CreateUpdateModel):

    CHOICES = (
        (1, 'Participei'),
        (2, 'Organizei')
    )

    TYPE_CHOICES = (
        (1, 'Evento'),
        (2, 'Congresso'),
        (3, 'Exposição'),
        (4, 'Feira')
    )

    choice = models.IntegerField(choices=CHOICES, verbose_name='Participação/Organização')
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name='Tipo do Evento')
    name = models.CharField(max_length=100, verbose_name='Nome do Evento/Congresso/Exposição/Feira')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return f'{self.name}. ({self.type})'


class CT(core.CreateUpdateModel):
    title = models.CharField(max_length=100, verbose_name='Apresentações de Trabalho')

    def __str__(self):
        return self.title


class Pessoa(core.CreateUpdateModel):
    id_lattes = models.CharField(max_length=150, verbose_name='ID Lattes')
    sobre = models.TextField(max_length=1200, verbose_name='Sobre')
    user = models.ForeignKey(core.UUIDUser, on_delete=models.CASCADE, null=True, verbose_name='Usuário')
    formacao = models.ManyToManyField(AcademicEducation, verbose_name='Formação Acadêmica/Titulação')
    formacao_complementar = models.ManyToManyField(ComplementaryEducation, verbose_name='Formação Complementar',
                                                   blank=True)
    atuacao_profissional = models.ManyToManyField(ProfessionalPerformance, verbose_name='Atuação Profissional')
    projetos_ensino = models.ManyToManyField(TeachingProjects, verbose_name='Projetos de Ensino', blank=True)
    area_atuacao = models.ManyToManyField(OccupationArea, verbose_name='Área de atuação', blank=True)
    language = models.ManyToManyField(UserLanguage, verbose_name='Idiomas', blank=True)
    award = models.ManyToManyField(Awards, verbose_name='Prêmio', blank=True)
    productions = models.ManyToManyField(Productions, verbose_name='Produções', blank=True)
    events = models.ManyToManyField(Events, verbose_name='Evento', blank=True)
    ct = models.ManyToManyField(CT, verbose_name='Educação e Popularização de C & T', blank=True)
    other_informations = models.TextField(max_length=250, verbose_name='Outras informações relevantes', blank=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

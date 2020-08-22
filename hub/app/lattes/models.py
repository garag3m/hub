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
    address = models.ForeignKey(core.Address, on_delete=models.CASCADE, verbose_name='Endereco')

    class Meta:
        verbose_name = 'Instituição de Ensino'
        verbose_name_plural = 'Instituições de Ensino'

    @property
    def get_address(self):
        return self.address.__str__()

    def __str__(self):
        return self.name


class AcademicEducation(core.CreateUpdateModel):

    GRADUATION_CHOICES = (
        (0, 'Técnico'),
        (1, 'Graduação'),
        (2, 'Especialização'),
        (3, 'Mestrado'),
        (4, 'Doutorado'),
        (5, 'Pós Doutorado')
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

    @property
    def graduation_choice(self):
        return self.GRADUATION_CHOICES[self.graduation_level][1]

    @property
    def get_conclusion_date(self):
        if self.conclusion_date is None:
            return 'Atual'
        else:
            return self.conclusion_date

    @property
    def get_institution(self):
        return self.institution.__str__()

    def __str__(self):
        return f'{self.start_date} - {self.get_conclusion_date}: {self.graduation_choice} em {self.graduation}\n' \
               f'{self.institution}\norientado(a) por {self.advisor}.'

    class Meta:
        verbose_name = 'Formação Acadêmica/Titulação'


class ComplementaryEducation(core.CreateUpdateModel):
    start_date = models.DateField(verbose_name='Data de Início')
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', blank=True, null=True)
    graduation_level = models.CharField(max_length=100, verbose_name='Graduação')
    institution = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name='Instituição')
    file = models.FileField(blank=True)

    class Meta:
        verbose_name = 'Formação Complementar'

    @property
    def get_conclusion_date(self):
        if self.conclusion_date is None:
            return 'Atual'
        else:
            return self.conclusion_date

    @property
    def get_institution(self):
        return self.institution.__str__()

    def __str__(self):
        return f'{self.start_date} - {self.get_conclusion_date}: {self.graduation_level} em {self.institution}'


class Task(core.CreateUpdateModel):
    start_date = models.DateField(verbose_name='Data de Início')
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    about = models.TextField(max_length=250, verbose_name='Sobre')
    file = models.FileField(blank=True)

    @property
    def get_conclusion_date(self):
        if self.conclusion_date is None:
            return 'Atual'
        else:
            return self.conclusion_date

    def __str__(self):
        return f'{self.start_date} - {self.get_conclusion_date} = {self.title}' \
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
    occupation_area = models.CharField(max_length=100, verbose_name='Área de Atuação', null=True)

    @property
    def get_conclusion_date(self):
        if self.conclusion_date is None:
            return 'Atual'
        else:
            return self.conclusion_date

    @property
    def get_institution(self):
        return self.institution.__str__()

    @property
    def tasks_list(self):
        lista = []
        for x in self.tasks.all():
            lista.append(f'{x.title}: {x.about}, ')
        return lista

    def __str__(self):
        return f'{self.start_date} - {self.get_conclusion_date} = Vínculo: {self.bond}, ' \
               f'Enquadramento Funcional: {self.occupation}, Carga Horária: {self.workload}, ' \
               f'Regime: {self.regime}, Área de Atuação: {self.occupation_area}'


class TeachingProjects(core.CreateUpdateModel):
    start_date = models.DateField(verbose_name='Data de Início')
    conclusion_date = models.DateField(verbose_name='Data de Conclusão', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    about = models.TextField(max_length=250, verbose_name='Sobre')
    file = models.FileField(blank=True)

    @property
    def get_conclusion_date(self):
        if self.conclusion_date is None:
            return 'Atual'
        else:
            return self.conclusion_date

    def __str__(self):
        return f'{self.start_date} - {self.get_conclusion_date} = {self.title}' \
               f'{self.about}'


class Language(core.CreateUpdateModel):

    LEVEL_CHOICES = (
        (0, 'Bem'),
        (1, 'Razoávelmente'),
        (2, 'Mal')
    )

    LANGUAGES = (
        (0, 'Português'),
        (1, 'Inglês'),
        (2, 'Espanhol'),
        (3, 'Francês'),
        (4, 'Alemão'),
        (5, 'Japonês'),
        (6, 'Chinês'),
        (7, 'Russo'),
        (8, 'Turco'),
        (9, 'Árabe'),
        (10, 'Norueguês')
    )

    language_name = models.IntegerField(choices=LANGUAGES, verbose_name='Idioma')
    reading_level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Nível de Leitura')
    writing_level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Nível de Escrita')
    speech_level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Nível de Comunicação')
    understanding_level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Nível de Compreensão')

    @property
    def get_language(self):
        return self.LANGUAGES[self.language_name][1]

    @property
    def reading_choice(self):
        return self.LEVEL_CHOICES[self.reading_level][1]

    @property
    def writing_choice(self):
        return self.LEVEL_CHOICES[self.writing_level][1]

    @property
    def speech_choice(self):
        return self.LEVEL_CHOICES[self.speech_level][1]

    @property
    def understanding_choice(self):
        return self.LEVEL_CHOICES[self.understanding_level][1]

    def __str__(self):
        return f'{self.get_language} = Entende {self.understanding_choice}, Fala {self.speech_choice}, ' \
               f'Lê {self.reading_choice}, Escreve {self.writing_choice}\n'


class Awards(core.CreateUpdateModel):
    year = models.DateField()
    award_name = models.CharField(max_length=100, verbose_name='Prêmio')
    file = models.FileField(blank=True)

    def __str__(self):
        return self.award_name


class Productions(core.CreateUpdateModel):

    TYPE_CHOICES = (
        (0, 'Produção Bibliográfica'),
        (1, 'Produção Técnica'),
        (2, 'Demais tipos de Produção')
    )

    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name='Tipo de Produção')
    header = models.CharField(max_length=100, verbose_name='Cabeçalho (ex: '
                                                           '"Livros publicados/organizados ou edições")')
    reference = models.CharField(max_length=400, verbose_name='Referência Bibliográfica da Produção')
    file = models.FileField(blank=True)

    @property
    def type_choice(self):
        return self.TYPE_CHOICES[self.type][1]

    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = 'Produção'
        verbose_name_plural = 'Produções'


class Events(core.CreateUpdateModel):

    CHOICES = (
        (0, 'Participei'),
        (1, 'Organizei')
    )

    TYPE_CHOICES = (
        (0, 'Evento'),
        (1, 'Congresso'),
        (2, 'Exposição'),
        (3, 'Feira')
    )

    choice = models.IntegerField(choices=CHOICES, verbose_name='Participação/Organização')
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name='Tipo do Evento')
    name = models.CharField(max_length=100, verbose_name='Nome do Evento/Congresso/Exposição/Feira')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    @property
    def type_choice(self):
        return self.TYPE_CHOICES[self.type][1]

    @property
    def choice_choice(self):
        return self.CHOICES[self.choice][1]

    def __str__(self):
        return f'{self.name}. ({self.type_choice})'


class CT(core.CreateUpdateModel):
    title = models.CharField(max_length=100, verbose_name='Apresentações de Trabalho')

    def __str__(self):
        return self.title


class Person(core.CreateUpdateModel):
    id_lattes = models.CharField(max_length=150, verbose_name='ID Lattes')
    about = models.TextField(max_length=1200, verbose_name='Sobre')
    user = models.ForeignKey(core.UUIDUser, on_delete=models.CASCADE, null=True, verbose_name='Usuário')
    academic_education = models.ManyToManyField(AcademicEducation, related_name='academic_education',
                                                verbose_name='Formação Acadêmica/Titulação')
    complementary_education = models.ManyToManyField(ComplementaryEducation, related_name='complementary_education',
                                                     verbose_name='Formação Complementar', blank=True)
    professional_performance = models.ManyToManyField(ProfessionalPerformance, related_name='professional_performance',
                                                      verbose_name='Atuação Profissional')
    teaching_projects = models.ManyToManyField(TeachingProjects, related_name='teaching_projects',
                                               verbose_name='Projetos de Ensino', blank=True)
    languages = models.ManyToManyField(Language, related_name='language', verbose_name='Idiomas', blank=True)
    award = models.ManyToManyField(Awards, related_name='award', verbose_name='Prêmio', blank=True)
    productions = models.ManyToManyField(Productions, related_name='productions', verbose_name='Produções', blank=True)
    events = models.ManyToManyField(Events, related_name='events', verbose_name='Evento', blank=True)
    ct = models.ManyToManyField(CT, related_name='ct', verbose_name='Educação e Popularização de C & T', blank=True)
    other_informations = models.TextField(max_length=250, verbose_name='Outras informações relevantes', blank=True)

    @property
    def get_picture(self):
        return self.user.picture

    @property
    def get_name(self):
        return self.user.username

    @property
    def get_academic_education(self):
        string = ''
        for academic_education in self.academic_education.all():
            string += str(academic_education) + ','
        return string

    @property
    def get_complementary_education(self):
        string = ''
        for complementary_education in self.complementary_education.all():
            string += str(complementary_education) + ','
        return string

    @property
    def get_professional_performance(self):
        string = ''
        for x in self.professional_performance.all():
            string += str(x) + ','
        return string

    @property
    def get_teaching_projects(self):
        string = ''
        for x in self.teaching_projects.all():
            string += str(x) + ','
        return string

    @property
    def get_occupation_area(self):
        string = ''
        for x in self.occupation_area.all():
            string += str(x) + ','
        return string

    @property
    def get_languages(self):
        string = ''
        for x in self.languages.all():
            string += str(x)
        return string

    @property
    def get_award(self):
        string = ''
        for x in self.award.all():
            string += str(x) + ','
        return string

    @property
    def get_productions(self):
        string = ''
        for x in self.productions.all():
            string += str(x) + ','
        return string

    @property
    def get_events(self):
        string = ''
        for x in self.events.all():
            string += str(x) + ','
        return string

    @property
    def get_ct(self):
        string = ''
        for x in self.ct.all():
            string += str(x) + ','
        return string

    def __str__(self):
        return 'CU'

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

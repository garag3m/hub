# Garag3m: hub

Projeto base e integrador dos demais projetos desenvolvidos pela Garag3m.

## Apps

O projeto é composto pela aplicação *core* composta basicamente pelas classes *CreateUpdateModel* e *UUIDUser*.  

### CreateUpdateModel

Classe composta basicamente pelos atributos de data de criação (created_at) e data da última atualização (updated_at). Além disso ela defini o *id* como sendo um UUID.

```python
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True
```

### UUIDUser

Classe que herda da classe AbstractUser, sendo utilizada para sobrescrever a classe User do Django. Como diferencial ela possui apenas os atributos de cpf, matrícula e imagem do profile do usuário.

```python
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    # core
    cpf = models.CharField(max_length=11, null=True, blank=True, verbose_name="CPF")
    registration = models.CharField(max_length=100, null=True, blank=True, verbose_name="matrícula")

    # picture
    picture = models.ImageField(null=False, blank=True, verbose_name='picture', upload_to='accounts/%Y/%m/%d')
    picture_thumb = ImageSpecField(source='picture', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
```

Você pode ver no arquivo settings.py a definição da classe UUIDUser como classe de usuário padrão.

```python
AUTH_USER_MODEL = 'core.UUIDUser'
```
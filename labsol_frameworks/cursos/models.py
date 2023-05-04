from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField('Nombre',max_length=150)
    apellido_paterno = models.CharField('apellido paterno',max_length=150)
    apellido_materno = models.CharField('apellido materno',max_length=150)
    avatar = models.ImageField('Foto de perfil', upload_to='perfiles',blank=True )
    fecha_nacimiento = models.DateField()
    nivel_profecional=models.CharField('Nivel Profecional',max_length=50)
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)


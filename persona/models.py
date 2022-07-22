from django.db import models
from ckeditor.fields import RichTextField
from departamento.models import Departamento
# Create your models here.

class Habilidad(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id)+' - '+self.habilidad


class Empleado(models.Model):
    """Modelo para Tabla Empleado"""
    """Definiendo Trabajos"""
    JOBS = (
        ('0','Contrador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('4','Otro'),
    )

    first_name = models.CharField('Nombre',max_length=60)
    last_name = models.CharField('Apellidos',max_length=60)
    full_name = models.CharField('Nombres Completos',max_length=120,blank=True)
    job = models.CharField('Trabajo',max_length=20,choices=JOBS)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/empleado', blank = True, null=True)
    habilidades = models.ManyToManyField(Habilidad)
    hoja_vida = RichTextField()

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        unique_together = ('first_name','last_name')

    def __str__(self) -> str:
        return str(self.id)+' - '+self.first_name+' - '+ self.last_name


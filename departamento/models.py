from django.db import models

# Create your models here.

class Departamento(models.Model):
    """Modelo para Tabla Departamento"""
    name = models.CharField('Nombre',max_length=50)
    short_name = models.CharField('Abreviatura',max_length=20,unique=True)
    anulate = models.BooleanField('Anulado',default=False)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        unique_together = ('name','short_name')

    def __str__(self) -> str:
        return str(self.id) +' - '+self.name +' - '+ self.short_name




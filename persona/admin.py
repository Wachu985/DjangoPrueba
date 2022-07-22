from django.contrib import admin
from .models import Empleado,Habilidad

# Register your models here.

admin.site.register(Habilidad)

class EmpleadoAdmin(admin.ModelAdmin):
    """Elementos de la Tabla"""
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name',
    )
    """Definiendo Funcion Extra para Elementos Extras"""
    def full_name(self,obj):
        print(obj)
        return obj.first_name +' '+obj.last_name

    """Buscador"""
    search_fields = ('first_name',)

    """"Filtro"""
    list_filter = ('job','habilidades')

    """Filtro Horizontal para Capos Muchos a Muchos"""
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin)
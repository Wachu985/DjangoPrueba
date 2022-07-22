from django.contrib import admin
from django.urls import path
from .views import (ListAllEmpleados,
                ListByAreaEmpleados,
                ListByJobEmpleados,
                ListEmpleadosByKeyW,
                ListHabilidadesEmpleados,
                EmpleadoDetailView,
                EmpleadoCreateView,
                SuccessView,
                EmpleadoUpdateView,
                EmpleadoDeleteView,
                InicioView,
                ListAllEmpleadosAdmin,
)

"""Nombre de la APP"""
app_name = 'persona_app'

urlpatterns = [
    path('',InicioView.as_view(), name='inicio'),
    path('empleados/listar',ListAllEmpleados.as_view(),name='listar_all'),
    path('empleados/listar-by-area/<short_name>',ListByAreaEmpleados.as_view(),name='listar_area'),
    path('empleados/listar-by-job/<job>',ListByJobEmpleados.as_view()),
    path('empleados/buscar/',ListEmpleadosByKeyW.as_view()),
    path('empleados/listhabilidades/',ListHabilidadesEmpleados.as_view()),
    path('empleados/detail/<pk>',
        EmpleadoDetailView.as_view(),
        name='detalle'
    ),#EL ID Debe ser en pk Por que Reconoce como una llave Primaria
    path('empleados/registrar/',EmpleadoCreateView.as_view(),name='registrar'),
    path('empleados/success/',SuccessView.as_view(),name = 'correcto'),
    path('empleados/editar/<pk>/',EmpleadoUpdateView.as_view(),name = 'modificar'),
    path('empleados/eliminar/<pk>/',EmpleadoDeleteView.as_view(),name = 'eliminar'),
    path('empleados/listar_admin/',ListAllEmpleadosAdmin.as_view(),name = 'listar_admin'),
]

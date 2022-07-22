from django.contrib import admin
from django.urls import path
from . import views
"""Nombre de la APP"""
app_name = 'departamento_app'

urlpatterns = [
    path('departamento/new',views.NewDepartamentoView.as_view(),name='new_departamento'),
    path('departamento/listar',views.ListarDepartamentoListView.as_view(),name='listar_depa'),
]
from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('pruebalist/', views.PruebaListView.as_view()),
    path('lista/', views.ListarListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(),name='create'),
    path('resumen/', views.ResumeFundation.as_view(),name='resumen'),
]
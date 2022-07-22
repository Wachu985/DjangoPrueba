from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumeFundation(TemplateView):
    template_name = "home/resume_fundation.html"



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'lista'
    queryset = [1,2,3,4,5,6,7,8,9,0]


class ListarListView(ListView):
    template_name = "home/lista_prueba.html"
    context_object_name = 'lista'
    model = Prueba


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'


    



    
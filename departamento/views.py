from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView,DetailView
from .forms import DepartamentoForm
from .models import Departamento
from persona.models import Empleado
from django.urls import reverse_lazy

# Create your views here.


class ListarDepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/listar.html"
    paginate_by = 5


"""Definimos la Vista del Form Conjunto"""
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = DepartamentoForm
    success_url = reverse_lazy('persona_app:correcto')

    """Definimos el Metodo Form Valid"""
    def form_valid(self, form):
        """Creando Departamento"""
        departamento = form.cleaned_data['departamento']
        short_name = form.cleaned_data['short_name']
        depa = Departamento(
            name = departamento,
            short_name = short_name,
        )
        depa.save()
        """Creando Objeto Empleado"""
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name =apellido,
            full_name = nombre+' '+apellido, 
            job = '1',
            departamento = depa  
        )
        return super(NewDepartamentoView,self).form_valid(form)
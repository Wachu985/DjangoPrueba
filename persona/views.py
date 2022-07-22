from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
#Models
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

"""Vista de Inicio"""
class InicioView(TemplateView):
    template_name = "home.html"


"""Lista a Todos los Empleados"""
class ListAllEmpleados(ListView):
    """Definimos Template"""
    template_name = "persona/listar.html"
    """Definiendo los Archivos q se van a mostrar"""
    paginate_by = 5
    ordering = 'id'

    def get_queryset(self):
        palabraclave = self.request.GET.get('kword',)
        """Verifica que la palabra clave se encuentre en el nombre"""
        if palabraclave == None:
            lista = Empleado.objects.all()
        else:
            lista = Empleado.objects.filter(
                first_name__icontains = palabraclave
            )
        return lista


class ListAllEmpleadosAdmin(ListView):
    """Definimos Template"""
    template_name = "persona/listar_admin.html"
    """Definiendo los Archivos q se van a mostrar"""
    paginate_by = 5
    model =  Empleado
    ordering = 'id'


"""Lista Empleados de un Area"""
class ListByAreaEmpleados(ListView):
    """Definimos Template"""
    template_name = "persona/listar_area.html"

    """Aplicando Filtros"""
    def get_queryset(self):
        """Recogiendo los Valores que Vienen por URL"""
        area = self.kwargs['short_name']
        """Creacion del Filtro"""
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista


class ListByJobEmpleados(ListView):
    """Definimos Template"""
    template_name = "persona/listar_job.html"

    """Aplicando Filtros"""
    def get_queryset(self):
        """Recogiendo los Valores que Vienen por URL"""
        area = self.kwargs['job']
        jobs  ={'Contrador':'0',
            'Administrador':'1',
            'Economista':'2',
            'Otro':'4'
        }
        lista = Empleado.objects.filter(
            job = jobs[area]
        )
        return lista


"""Busqueda por Parametros de una Caja de Texto"""
class ListEmpleadosByKeyW(ListView):
    """Lista Empleados por Palabra Clave"""
    template_name = "persona/buscarbykey.html"

    """Reciviendo los Valores desde un Input"""
    def get_queryset(self):
        palabraclave = self.request.GET.get('kword',)
        print(palabraclave)
        lista = Empleado.objects.filter(
            first_name = palabraclave
        )
        return lista


"""Relacion Many to Many"""
class ListHabilidadesEmpleados(ListView):
    template_name = "persona/listhabilidades.html"

    def get_queryset(self):
        claveid = self.request.GET.get('id',)
        if claveid == None:
            return []
        empleado = Empleado.objects.get(id=claveid)
        lista = empleado.habilidades.all()
        return lista
    

"""Creando un Detalle View"""
class EmpleadoDetailView(DetailView):
    template_name = "persona/detail_empleado.html"
    model = Empleado
    """Mandar Variable que no estan en el Modelo"""
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes' 
        return context



class SuccessView(TemplateView):
    template_name = "persona/success.html"



""""Create View"""
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    """Se Redirecciona a si Mismo"""
    success_url = reverse_lazy('persona_app:listar_all')

    """Si el los Valores son Validos Entra a Este Metodo"""
    def form_valid(self, form):
        """Logica del Codigo"""
        """Se Guardan en la DB los Elementos que vienen del FORM"""
        empleado = form.save(commit=False)
        """Se Modifica el Elemento de la DB"""
        empleado.full_name = empleado.first_name+' '+ empleado.last_name
        """Se Guardan el Nuevo Elemento en la DB"""
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


"""Update View"""
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/editar_empleado.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:listar_admin')

    """Modificar valores Antes de validarlos"""
    def post(self, request, *args, **kwargs):
        """Recuperando valores de POST"""
        request.POST['last_name']
        print("************************Antes de Validar*************")
        return super().post(request, *args, **kwargs)

    """Si el los Valores son Validos Entra a Este Metodo"""
    def form_valid(self, form):
        """Logica del Codigo"""
        print("************************Es Valido*************")
        return super(EmpleadoUpdateView,self).form_valid(form)


"""Delete View"""
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:listar_admin')

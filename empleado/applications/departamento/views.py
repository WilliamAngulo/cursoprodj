from applications import departamento
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

from django.views.generic import ListView



class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    # paginate_by = 4
    context_object_name = 'departamento' # esto lo hago para utilizar departamento en lugar de object_list en el archivo html
                                         # si no declaro la variale context_object_name tendre que usar object_list en el archivo html 


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
  
    def form_valid(self, form):

        departamento_creado = Departamento(
        name = form.cleaned_data['nombre_departamento'],
        shor_name = form.cleaned_data['short_name_dpto']
    )
        departamento_creado.save()

        """If the form is valid, save the associated departamento."""
        print('######################### departamento  FORM_VALID  ############################')
        nombre_encargado = form.cleaned_data['nombre_encargado']
        apellidos_encargado = form.cleaned_data['apellidos_encargado']
        Empleado.objects.create(
            first_name=nombre_encargado,
            last_name=apellidos_encargado,
            job='1',
            departamento = departamento_creado
        )
   
        return super(NewDepartamentoView,self).form_valid(form)

class ListAllDepartamentos(ListView):
    # Dato curioso intencionalmente elimine template_name, por defecto buscara el archivo templates.persona.empleado_list.html
    #template_name = "persona/empleado_list.html"
    template_name = "departamento/lista_all.html"
    paginate_by = 4  # para ver la pagina 3 hacemos 127.0.0.1:800/listar-todo-empleados/?page=3
                     # Cuando ListView se encuentra un paginate_by automaticamente crea un objeto paginator
    ordering = 'name'
    # model = Empleado  # inhabilito esta linea porque voy a usar el metodo get_queryset y no tengo qque especificar el modelo aqui.
    #context_object_name = 'lista'  # no es necesario porque ya ListView provee self.object_list disponible en una pagina html mediante  {{object_list}}

    # Esto me lo copie de la class ListEmpleadosByKword para buscar un empleado desde la html: http://127.0.0.1:8000/listar-todo-departamentos/
    def get_queryset(self):
        # print('#################')
        palabra_clave = self.request.GET.get("kword", '') # request es un object que contiene las solicitudes que se han enviado a un servidor
                                                          #Interceptamos el metodo GET. Django ha ordenado internamente en metodos y submetodos
                                                          # recuperame (get) el valor con el identificador 'kword' . Esto debe ser una tupla  
        
        # lista = Empleado.objects.filter(
        #     # departamento__name = 'Ventas al detal'
        #     #departamento__name = area
        #     #first_name = palabra_clave
        #     last_name = palabra_clave
        # )
        
        lista = Departamento.objects.filter(name__icontains=palabra_clave)

        print('lista filtrada: ', lista)
        return lista



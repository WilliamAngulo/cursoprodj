from typing import Collection
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView,TemplateView,
    UpdateView,DeleteView
)
from .models import Empleado
from django.http import HttpResponseRedirect
from .forms import EmpleadoForm

class InicioView(TemplateView):
    ''' Vista de carga la hoja de inicio'''
    template_name = "inicio.html"


# listar todos los empleado de la empresa
class ListAllEmpleados(ListView):
    # Dato curioso intencionalmente elimine template_name, por defecto buscara el archivo templates.persona.empleado_list.html
    #template_name = "persona/empleado_list.html"
    template_name = "persona/lista_all.html"
    paginate_by = 4  # para ver la pagina 3 hacemos 127.0.0.1:800/listar-todo-empleados/?page=3
                     # Cuando ListView se encuentra un paginate_by automaticamente crea un objeto paginator
    ordering = 'first_name'
    # model = Empleado  # inhabilito esta linea porque voy a usar el metodo get_queryset y no tengo qque especificar el modelo aqui.
    #context_object_name = 'lista'  # no es necesario porque ya ListView provee self.object_list disponible en una pagina html mediante  {{object_list}}

    # Esto me lo copie de la class ListEmpleadosByKword para buscar un empleado desde la html: http://127.0.0.1:8000/listar-todo-empleados/
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
        
        lista = Empleado.objects.filter(full_name__icontains=palabra_clave)

        print('lista filtrada: ', lista)
        return lista


# Listar empleados desde el menu Administracion
class ListEmpleadosAdmin(ListView):
    template_name = "persona/lista_empleados.html"
    paginate_by = 10  # para ver la pagina 3 hacemos 127.0.0.1:800/listar-todo-empleados/?page=3
                     # Cuando ListView se encuentra un paginate_by automaticamente crea un objeto paginator
    ordering = 'first_name'
    model = Empleado  # inhabilito esta linea porque voy a usar el metodo get_queryset y no tengo qque especificar el modelo aqui.
    context_object_name = 'lista'  # no es necesario porque ya ListView provee self.object_list disponible en una pagina html mediante  {{object_list}}

   

# listar todos los empleados que pertenecen a un area de la empresa
class ListByArea(ListView):
    #model = Empleado
    template_name = "persona/list_by_area.html"
    context_object_name = 'empleados'
    # queryset = Empleado.objects.filter(
    #     departamento__name = 'Control administrativo'
    # )

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        area = self.kwargs['shor_name'] # kwargs (keyword arguments)es un metodo de django para recoger lo que envien por url
        queryset = Empleado.objects.filter(
            # departamento__name = 'Ventas al detal'
            #departamento__name = area
            departamento__shor_name = area
        )
        return queryset 




#####################################################################################

# listar todos los empleados que pertenecen a un cargo en particular en la empresa 

class ListByJob(ListView):
    template_name = "persona/list_by_job.html"
    model = Empleado
    context_object_name ='empleados'
    def get_queryset(self):
        job = self.request.GET.get("job", '')
        print(job)
        empleado = Empleado.objects.filter(job=job)  # revisar https://docs.djangoproject.com/en/3.2/topics/db/queries/
        print(empleado)
        return empleado
      
      

#######################################################################################


# Listar empleados por palabra clave
class ListEmpleadosByKword(ListView):
    template_name = "persona/by_kword.html"
    #model = MODEL_NAME
    context_object_name ='empleados'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '') # request es un object que contiene las solicitudes que se han enviado a un servidor
                                                          #Interceptamos el metodo GET. Django ha ordenado internamente en metodos y submetodos
                                                          # recuperame (get) el valor con el identificador 'kword' . Esto debe ser una tupla  
        
        lista = Empleado.objects.filter(
            # departamento__name = 'Ventas al detal'
            #departamento__name = area
            #first_name = palabra_clave
            last_name = palabra_clave
        )
        print('lista filtrada: ', lista)
        return lista
        
##########################################################################################

class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name ='habilidades'
    def get_queryset(self):
        id = self.request.GET.get('id', '')
        print(id)
        empleado = Empleado.objects.get(id=id)        
        #print(empleado.habilidades.all())
        return empleado.habilidades.all()
        
#########################################################################################
    
class EmpleadoDetailView(DetailView):
    model = Empleado             
    template_name = "persona/detail_empleado.html" # en este file podemos llamar {{object}} o {{empleado}} ojo: en minuscula
                                                   # y sus atributos, por ejemplo object.first_name   {{object.first_name}}
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
        print(context)
        # Bloque que representa la determinacion
        #          del empleado del mes
        dedicacion = 4/5
        planificacion = 5/5
        responsabilidad = 4/5
        compromiso = 4/5
        a = dedicacion + planificacion + responsabilidad + compromiso
        context['titulo'] = 'Empleado del mes'
        context['a'] = a
        return context

####################################################################


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado  #
    #fields = ('__all__')
    # fields = ['first_name','last_name','job','departamento', 'habilidades','avatar']  # ya no necesito los fields porque voy a trabajar con formularios
    form_class = EmpleadoForm  # ahora el modelo de formulario EmpleadoForm define los fields que mostrare en los html

    #success_url = '.'  # The URL to redirect to after successful registration. A string containing a (relative) URL, or a string
                       #  name of a URL pattern, or a 3-tuple of arguments suitable for passing to Django’s redirect shortcut. 
                       # Can be overridden on a per-request basis (see below). Default value is None, so that per-request customization is used instead.
                       # '.' nos recarga la misma pagina, es decir add.html
    
    #success_url = '/success'  # con esto redirecciono a la url definida en  path('success/',SuccessView.as_view()),
                               # esta forma de redireccionar no es muy elegante. La alternativa es reverse_lazy disponile en django.urls
    # success_url = reverse_lazy('persona_app:correcto') # atencion - No debe haer espacios en blanco, Django lo consideraria como una cadena con espacio
    success_url = reverse_lazy('persona_app:empleados_admin')
    # vamos a interceptar la creacion de un nuevo empleado sobre escribiendo la clase EmpleadoCreateView
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #self.object = form.save()
        #print(self.object)
        empleado = form.save(commit=False) # Commit=False para que no salve, me permite modificar algo antes de salvar
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        print(empleado.full_name)
        empleado.save()        
        return super(EmpleadoCreateView,self).form_valid(form)
        
####################################################################


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    # fields = ['first_name','last_name','job','departamento', 'habilidades']
    form_class = EmpleadoForm
    # success_url = reverse_lazy('persona_app:correcto')
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        # empleado = self.get_object()
        print('#########################  METODO POST  ############################')
        print('#####################################################################')
        # print(request.POST)
        print(
            request.POST['first_name'],request.POST['last_name'],
            request.POST['job'],request.POST['departamento'],
            request.POST['habilidades']
            )
        return super(EmpleadoUpdateView,self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #self.object = form.save()
        #print(self.object)
        # empleado = form.save(commit=False) # Commit=False para que no salve, me permite modificar algo antes de salvar
        # empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # print(empleado.full_name)
        # empleado.save()
        print('#########################  FORM_VALID  ############################')
        print('#####################################################################')        
        return super(EmpleadoUpdateView,self).form_valid(form)

####################################################################################

class EmpleadoDeleteView(DeleteView):
    
    # Esta es una forma de borrar un registro, obviamente activando la linea: success_url = reverse_lazy('persona_app:correcto') 
    template_name = "persona/delete.html"
    model = Empleado
    # success_url = reverse_lazy('persona_app:correcto')

    # esta es la segnda forma de borrar un registro
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        #self.object = self.get_object()
        empleado = self.get_object()
        print(empleado)
        #success_url = self.get_success_url()
        # success_url = reverse_lazy('persona_app:correcto')
        success_url = reverse_lazy('persona_app:empleados_admin')
        empleado.delete()
        return HttpResponseRedirect(success_url)    

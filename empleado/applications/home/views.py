# VISTAS BASADAS EN CLASES
from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView,
    CreateView
)
from . models import Prueba
from .forms import PruebaForm

class PruebaView(TemplateView):
    #template_name = 'prueba.html' # Django buscara el archivo prueba.html en el folder home.templates. En home porque alli esta este views.py
    template_name = 'home/prueba.html' # se refiere a prueba.html que esta en la carpeta empleado/templates/home/prueba.html
    # recordar que TEMPLATES = [ en settings.base.py fue configurado para que Django vea la carpeta empleados.templates
    # cuando llamamos 127.0.0.1.8000/prueba/ no tenemos que decir 127.0.0.1.8000/templates/prueba/  de eso se envcargo unipath
    
class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html' # se refiere a prueba.html que esta en la carpeta empleado/templates/home/prueba.html




class PruebaListView(ListView):
    template_name = "home/lista.html"
    #model = MODEL_NAME  # todavia no hemos trabjado con bases de datos
    context_object_name = 'listaNumeros' # cuando en la pagina indicada por tamplate_name (lista.html) yo coloque {{listaNumero}} 
    queryset = ['0','10','20','30']      #Django colocara alli el valor de queryset
    

class ListarPruebaListView(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista' # cuando en la pagina indicada por tamplate_name (lista_prueba.html) yo coloque {{lista}} 
                                  # Dango sabra que {{lista}} lo obtendra de cada objeto del modelo Prueba
 
class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    #fields = ['titulo','subtitulo','cantidad']  # esta linea la inhabilitamos para dar paso al form_class =  PruebaForm
    form_class = PruebaForm
    success_url = '/'       # ciando se haya completado el proceso, que se vaya a la pagina principal (127:0.0.1.8000)
     

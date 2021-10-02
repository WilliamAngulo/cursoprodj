from django.contrib import admin
from django.urls import path

# def DesdeAppPersona(self):
#     print('###############################Desde la App Persona######################################' )
    
# urlpatterns = [
#     path('persona/', DesdeAppPersona), # Django ejecutara la funcion DesdeAppDepartamento si en el navegador colocamos la cadena 'http://127.0.0.1:8000/persona/'
# ]

from . views import (ListAllEmpleados,ListByArea,ListByJob,
                    ListEmpleadosByKword,ListHabilidadesEmpleado,
                    EmpleadoDetailView,EmpleadoCreateView,
                    SuccessView,EmpleadoUpdateView,
                    EmpleadoDeleteView,
                    InicioView,
                    ListEmpleadosAdmin

)

app_name = "persona_app" # este es una etiqueta para ubicar el bloque urls de la aplicacion persona

urlpatterns = [
    path('',InicioView.as_view(),name='inicio'),
    path('buscar_empleado/', ListEmpleadosByKword.as_view(),name='buscar_empleado'), # Django ejecutara PruebaView(TemplateView) si en el navegador colocamos la cadena 'http://127.0.0.1:8000/prueba/'
    path('listar-todo-empleados/', ListAllEmpleados.as_view(),name='empleados_all'), # Django ejecutara ListAllEmpleados(ListView) si en el navegador colocamos la cadena 'http://127.0.0.1:8000/listar-todo-empleados/'
    path('lista_by_area/<shor_name>/',ListByArea.as_view(),name='empleados_area'),
    path('lista_by_job/',ListByJob.as_view()),
    path('lista_habilidades_empleado/',ListHabilidadesEmpleado.as_view()),
    path('ver_empleado/<pk>/',EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add_empleado/',EmpleadoCreateView.as_view(), name='empleado_add'),
    # path('success/',SuccessView.as_view()),
    path(
        'success/',SuccessView.as_view(),
        name='correcto'      #con name puedo hacer mencion a la url "/success" desde cualquier success_url
    ),                           
    path('update_empleado/<pk>/',EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('eliminar_empleado/<pk>/',EmpleadoDeleteView.as_view(),name='eliminar_empleado'),
    path('lista_empleados_admin/',ListEmpleadosAdmin.as_view(),name='empleados_admin'),
        
]



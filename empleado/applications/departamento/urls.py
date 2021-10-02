from django.contrib import admin
from django.urls import path
from . import views

def DesdeAppDepartamento(self):
    print('###############################Desde la App Departamento######################################' )

app_name = "departamento_app"

urlpatterns = [
    path('departamento/', DesdeAppDepartamento), # Django ejecutara la funcion DesdeAppDepartamento si en el navegador colocamos la cadena 'http://127.0.0.1:8000/departamento/'
    path('new_departamento/', views.NewDepartamentoView.as_view(),name='nuevo_departamento'),
    path('departamento_lista/', views.DepartamentoListView.as_view(),name='departamento_list'),

]

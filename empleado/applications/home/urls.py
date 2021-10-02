from django.contrib import admin
from django.urls import path
from . views import (
    PruebaView,PruebaListView,ListarPruebaListView,
    PruebaCreateView,
    ResumeFoundationView,
)

#app-name = "home_app"

urlpatterns = [
    path('prueba/', PruebaView.as_view()), # Django ejecutara PruebaView(TemplateView) si en el navegador colocamos la cadena 'http://127.0.0.1:8000/prueba/'
    path('lista/', PruebaListView.as_view()), ## Django ejecutara PruebaListView(ListView) si en el navegador colocamos la cadena 'http://127.0.0.1:8000/lista/'
    path('lista_prueba/',ListarPruebaListView.as_view()),
    path('add/',PruebaCreateView.as_view(), name ='prueba_agregar'),
    path('resume_foundation/',ResumeFoundationView.as_view(), name ='resume_foundation'),
]


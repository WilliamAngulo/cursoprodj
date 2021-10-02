"""empleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

    
urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluiremos las urls de la app departamento
    path('', include('applications.departamento.urls')), # Django incluye las diferentes urls declaradas en applications.departamento.urls.py a 'http://127.0.0.1:8000/XXXXXXXX/'
    path('', include('applications.persona.urls')), # Django incluye las diferentes urls declaradas en applications.departamento.urls.py a 'http://127.0.0.1:8000/XXXXXXXX/'
    path('', include('applications.home.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path

# def PruebaUrl(self):
#     print("********************************* Hola Testing URLS*****************************")
    
# urlpatterns = [
#     path('admin/', admin.site.urls), # Django ejecutara admin.site.urls si en el navegador colocamos la cadena 'http://127.0.0.1:8000/admin/'
#     path('prueba/', PruebaUrl), # Django ejecutara PruebaUrl si en el navegador colocamos la cadena 'http://127.0.0.1:8000/prueba/'
# ]

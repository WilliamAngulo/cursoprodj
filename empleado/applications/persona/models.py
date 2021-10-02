from django.db import models
from django.db.models.fields.files import ImageField, ImageFieldFile
from django.db.models.fields.related import ForeignKey
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Creamos la tabla Habilidades
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50,unique=True)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural ='Habilidades del personal'

    def __str__(self):  
        """Unicode representation of Departamento"""
        return str(self.id) + "-"  + self.habilidad # cuando pidan empleado.habilidades voy a mandar id - habilidad, si solo quieren la
                                                    # habilidad deben pedir elemento.habilidades.habilidad
        



""" Modelo para la tabla empleado"""
class Empleado(models.Model):
    job_choices = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Analista'),
        ('4','Otros'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres_completos', max_length=120,blank=True)
    job = models.CharField('Trabajo', max_length=1,choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #avatar = models.ImageField(, upload_to='empleado', height_field=None, width_field=None, max_length=None)
    avatar = models.ImageField(upload_to='empleado', blank=True,null=True)
    habilidades = models.ManyToManyField(Habilidades) # el argumento Habilidades es la tabla con la que hay una relacion many-to-many
    hoja_vida = RichTextField()

    class Meta: # Esta clase la definimos para personalizar la presendacion en el Django administrator (127.0.0.1:8000/admin/)
        verbose_name = "Nombre del empleado"
        verbose_name_plural ='Empleados nacionales'
        ordering = ['last_name','first_name']
            
    def __str__(self):
        """Unicode representation of persona"""
        return str(self.id) + ' / ' + self.first_name + ' / ' + self.last_name + ' / ' + self.job


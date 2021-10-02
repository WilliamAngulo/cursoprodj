from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50,editable=True)
    shor_name = models.CharField('Nombre Corto', max_length=50,unique=True)
    anulate = models.BooleanField('Anulado', default=False)


    class Meta: # Esta clase la definimos para personalizar la presendacion en el Django administrator (127.0.0.1:8000/admin/)
        verbose_name = "Nombre del Departamento"
        verbose_name_plural ='Departamentos de la empresa'
        ordering = ['name']
        unique_together = ('name', 'shor_name') 
    
    def __str__(self):
        """Unicode representation of Departamento"""
        return self.name + ' / ' + self.shor_name



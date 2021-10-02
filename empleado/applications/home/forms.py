from typing import ClassVar
from django import forms
from django.db.models import fields
from .models import Prueba


# Creacion de un formulario para mostrar en el template html
class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        #fields = ('__all__')
        fields = ('titulo', 'subtitulo', 'cantidad')

        widgets = {                                                       # revisar https://docs.djangoproject.com/en/3.2/topics/forms/ 
            'titulo' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese texto aqui'
                }
            )                              
        }

    def clean_cantidad(self):
        #cantidad = self.cleaned_data.get('cantidad')
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad     


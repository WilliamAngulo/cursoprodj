from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = (            # los fields nos permite mostrar los campos que queramos mostrar en la pagina .html
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
        )

        widgets = {
            'habilidades' : forms.CheckboxSelectMultiple()
        }

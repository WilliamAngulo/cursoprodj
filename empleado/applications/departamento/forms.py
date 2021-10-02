from django import forms

class NewDepartamentoForm(forms.Form):
    nombre_encargado = forms.CharField(max_length=50, required=True)   # nombre: nombre del empleado a cargo del departamento a crear
    apellidos_encargado = forms.CharField(max_length=50, required=True)  # required=True es equivalente a no ponerlo, es decir es obligatorio
    nombre_departamento = forms.CharField(max_length=30)
    short_name_dpto = forms.CharField(max_length=20)
     
from django.contrib import admin
from . models import Empleado,Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job', 
        'departamento',
        'full_name', # Este atributo no es parte del modelo de persona
        'id',
    )
    def full_name(self,obj):
        #print(obj) # imprime lo que pusimos en def __str__(self) del modelo Empleado:  return(self.id) + ' / ' + self.first_name + ' / ' + self.last_name
        #print(obj.first_name,obj.last_name,obj.job,obj.departamento)
        return obj.first_name + ' '+obj.last_name
        
    
    search_fields = ('first_name',) # Crea un campo search en el Django administration
    list_filter = ('job','habilidades','departamento')  # Crea una ventana para filtrar por tipo de trabajo,habilidad y deppartamento en el Django administration
    filter_horizontal = ('habilidades',) # Crea un campo search para campos atributos Many-To-Many en el Django administration

admin.site.register(Empleado,EmpleadoAdmin)
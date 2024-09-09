from django.contrib import admin
from porque.models import Porque

# Register your models here.


class PorqueAdmin(admin.ModelAdmin):

    list_display = [
            'area', 'linea', 'subcategoria', 'miembros_equipo', 'pilar', 
            'impacto', 'kpi_iceo', 'kpi_secundario', 'fecha_inicio', 'fecha_cierre'
        ]



admin.site.register(Porque, PorqueAdmin)
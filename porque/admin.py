from django.contrib import admin
from porque.models import Porque, MiembroEquipo

# Register your models here.


class PorqueAdmin(admin.ModelAdmin):
    list_display = ('area', 'subarea', 'maquina', 'mostrar_miembros_equipo', 'pilar', 
                    'impacto', 'kpi_iceo', 'kpi_secundario', 'fecha_inicio', 'fecha_cierre')

    def mostrar_miembros_equipo(self, obj):
        return ", ".join([miembro.nombre for miembro in obj.miembros_equipo.all()])
    mostrar_miembros_equipo.short_description = 'Miembros del Equipo'

admin.site.register(Porque, PorqueAdmin)


@admin.register(MiembroEquipo)
class MiembroEquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')  # Puedes ajustar las columnas que quieras mostrar


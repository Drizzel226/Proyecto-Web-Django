from django.contrib import admin
from porque.models import Porque, MiembroEquipo

class PorqueAdmin(admin.ModelAdmin):
    list_display = (
        'categoria', 'subcategoria', 'area', 'subarea', 'maquina', 'mostrar_miembros_equipo', 
        'pilar', 'impacto', 'kpi_iceo', 'kpi_secundario', 'fecha_inicio', 'fecha_cierre',
        'que_ocurre', 'como_ocurre', 'donde_ocurre', 'cuando_ocurre', 'quien_presente', 
        'senal_antes', 'descripcion_senal', 'falla_funcional', 'imagen_falla_funcional'
    )

    def mostrar_miembros_equipo(self, obj):
        return ", ".join([miembro.nombre for miembro in obj.miembros_equipo.all()])
    mostrar_miembros_equipo.short_description = 'Miembros del Equipo'

admin.site.register(Porque, PorqueAdmin)

@admin.register(MiembroEquipo)
class MiembroEquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')

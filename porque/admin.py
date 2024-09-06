from django.contrib import admin
from porque.models import Porque

# Register your models here.


class PorqueAdmin(admin.ModelAdmin):

    list_display = ("nombre", "email", "asunto", "mensaje", "categoria", "prioridad", "seguimiento")



admin.site.register(Porque, PorqueAdmin)
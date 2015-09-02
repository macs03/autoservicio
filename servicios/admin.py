from django.contrib import admin
from servicios.models import Servicios, Servicios_Realizados, Tipo_Servicio
# Register your models here.

admin.site.register(Servicios)
admin.site.register(Servicios_Realizados)
admin.site.register(Tipo_Servicio)

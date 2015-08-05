from django.contrib import admin
from empleados.models import Empleados, Control_Empleados , Cestatickets ,Constantes_Administracion, Quincenas , Bancos, TipoEgreso
# Register your models here.
admin.site.register(Empleados)
admin.site.register(Control_Empleados)
admin.site.register(Cestatickets)
admin.site.register(Constantes_Administracion)
admin.site.register(Quincenas)
admin.site.register(Bancos)
admin.site.register(TipoEgreso)
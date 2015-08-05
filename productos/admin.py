from django.contrib import admin
from productos.models import Productos, Factura, Egresos
# Register your models here.

admin.site.register(Productos)
admin.site.register(Factura)
admin.site.register(Egresos)
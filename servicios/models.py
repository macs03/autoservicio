from django.db import models
from clientes.models import Clientes
from empleados.models import Empleados, Constantes_Administracion
from django.forms import ModelForm
# Create your models here.
class Servicios(models.Model):
	nombre = models.CharField(max_length = 250)
	tipo = models.CharField(max_length= 100)

	def __str__(self):
		return self.nombre


class Tipo_Servicio(models.Model):
    tipo = models.CharField(max_length=100)
    valor = models.IntegerField()

    def __str__(self):
        return "%s - %d" % (self.tipo, self.valor)

class Servicios_Realizados(models.Model):
    servicio = models.ForeignKey(Servicios)
    vehiculo_cliente = models.ForeignKey(Clientes)
    fecha = models.DateField()
    costo = models.ForeignKey(Constantes_Administracion)
    km_servicio = models.IntegerField()
    empleado = models.ForeignKey(Empleados)
    tipo_servicio = models.ForeignKey(Tipo_Servicio)

    def __str__(self):
        return "%s - %s - %s " % (self.vehiculo_cliente, self.fecha, self.costo)


class ServiciosForm(ModelForm):
	class Meta:
		model = Servicios
		fields = ('nombre', 'tipo')

class Servicios_RealizadosForm(ModelForm):
	class Meta:
		model = Servicios_Realizados
		fields = ('servicio', 'vehiculo_cliente', 'fecha', 'costo','km_servicio', 'empleado','tipo_servicio')
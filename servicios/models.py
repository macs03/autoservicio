from django.db import models
from vehiculos.models import Vehiculo_Clientes
from empleados.models import Empleados 
from django.forms import ModelForm
# Create your models here.
class Servicios(models.Model):
	nombre = models.CharField(max_length = 250)
	tipo = models.CharField(max_length= 100)

	def __str__(self):
		return self.nombre


class Servicios_Realizados(models.Model):
	servicio = models.ForeignKey(Servicios)
	vehiculo_cliente = models.ForeignKey(Vehiculo_Clientes)
	fecha = models.DateField()
	costo = models.FloatField()
	empleado = models.ForeignKey(Empleados)


	def __str__(self):
		return "%s - %s - %s " %(self.vehiculo_cliente, self.fecha, self.costo)


class ServiciosForm(ModelForm):
	class Meta:
		model = Servicios
		fields = ('nombre', 'tipo')

class Servicios_RealizadosForm(ModelForm):
	class Meta:
		model = Servicios_Realizados
		fields = ('servicio', 'vehiculo_cliente', 'fecha', 'costo', 'empleado')
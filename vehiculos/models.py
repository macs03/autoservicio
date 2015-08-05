from django.db import models
from clientes.models import Clientes
from django.forms import ModelForm
# Create your models here.
class Vehiculos(models.Model):
	placa = models.CharField(max_length=20)
	modelo = models.CharField(max_length=100)
	marca = models.CharField(max_length=100)
	km = models.CharField(max_length=20)

	def __str__(self):
		return "%s - %s" % (self.placa,self.modelo)

class Vehiculo_Clientes(models.Model):
	cliente = models.ForeignKey(Clientes)
	vehiculo = models.ForeignKey(Vehiculos)

	def __str__(self):
		return "%s - %s" % (self.cliente, self.vehiculo)


class VehiculosForm(ModelForm):
	class Meta:
		model = Vehiculos
		fields = ('placa', 'modelo', 'marca', 'km')

class Vehiculo_ClientesForm(ModelForm):
	class Meta:
		model = Vehiculo_Clientes
		fields = ('cliente', 'vehiculo')
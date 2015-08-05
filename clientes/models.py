from django.db import models
from django.forms import ModelForm
# Create your models here.
class Clientes(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	cedula = models.CharField(max_length=100)
	direccion = models.CharField(max_length=300)

	def __str__(self):
		return self.nombre

class ClientesForm(ModelForm):
	class Meta:
		model = Clientes
		fields = ('nombre', 'apellido', 'cedula','direccion')
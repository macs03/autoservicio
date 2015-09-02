from django.db import models
from django.forms import ModelForm
# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

    def __str__(self):
		return "%s %s - %s" % (self.nombre,self.apellido,self.placa)

class ClientesForm(ModelForm):
	class Meta:
		model = Clientes
		fields = ('nombre', 'apellido', 'cedula','direccion','telefono','placa','modelo','marca')
from django.db import models
from vehiculos.models import Vehiculo_Clientes
from servicios.models import Servicios_Realizados, Servicios
from empleados.models import Bancos, TipoEgreso
from django.forms import ModelForm
# Create your models here.
class Productos(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=150)
	costo = models.FloatField()
	precio = models.FloatField()
	cantidad = models.IntegerField()

	def __str__(self):
		return "%s - %s" % (self.nombre, self.precio)


class Factura(models.Model):
	cliente_vehiculo = models.ForeignKey(Vehiculo_Clientes)
	servicios = models.ManyToManyField(Servicios_Realizados)
	productos = models.ManyToManyField(Productos)
	banco = models.ForeignKey(Bancos, blank=True ,null=True)
	fecha = models.DateField()
	total = models.FloatField()

	def __str__(self):
		return "%s -%s" % (self.cliente_vehiculo, self.fecha)

class Egresos(models.Model):
    cobrador = models.CharField(max_length=100)
    monto = models.FloatField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length= 300)
    tipo = models.ForeignKey(TipoEgreso)
    banco = models.ForeignKey(Bancos)
    responsable = models.CharField(max_length= 100)

    def __str__(self):
        return "%s %s" % (self.cobrador, self.monto)


class ProductosForm(ModelForm):
	class Meta:
		model = Productos
		fields = ('nombre', 'codigo', 'costo', 'precio', 'cantidad')

class FacturasForm(ModelForm):
	class Meta:
		model = Factura
		fields = ('cliente_vehiculo', 'servicios', 'productos', 'fecha', 'banco', 'total')


class EgresosForm(ModelForm):
	class Meta:
		model = Egresos
		fields = ('cobrador', 'monto', 'fecha', 'descripcion', 'tipo','banco','responsable')
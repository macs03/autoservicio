from django.db import models
from django.forms import ModelForm
# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    # sueldo_base = models.FloatField()
    cargo = models.CharField(max_length=100)
    hoja_de_vida = models.FileField(upload_to='media/archivos/')

    def __str__(self):
        return "%s %s - %s" % (self.nombre, self.apellido, self.cargo)


class Control_Empleados(models.Model):
    empleado = models.ForeignKey(Empleados)
    fecha = models.DateField()
    sueldo = models.FloatField()
    cestatickets = models.FloatField()


    def __str__(self):
        return "%s - %s" % (self.empleado, self.sueldo)


class Constantes_Administracion(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.FloatField()

    def __str__(self):
        return "%s %s" % (self.nombre,self.valor)


class Cestatickets(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    empleado = models.ForeignKey(Empleados)
    costo = models.ForeignKey(Constantes_Administracion, related_name='constantes_administracion_costo')
    dias_laborados = models.IntegerField()
    dias_nolaborados = models.IntegerField()
    unidad_tributaria = models.ForeignKey(Constantes_Administracion,
                                          related_name='constantes_administracion_unidad_tributaria')
    total_pagar= models.FloatField(null=True,blank=True)

    def __str__(self):
        return "%s %s %s" % (self.empleado, self.costo, self.dias_laborados)


class Quincenas(models.Model):
    # numero_semana_1 = models.IntegerField()
    numero_semana = models.IntegerField()
    #numero_quincena = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    empleado = models.ForeignKey(Empleados)
    # dias_mes = models.IntegerField()
    # dias_laborados = models.IntegerField()
    # asignaciones_dia_laborado = models.FloatField(null=True, blank=True)
    # bono1 = models.ForeignKey(Constantes_Administracion)
    # bono1_pagar = models.FloatField(null=True, blank=True)
    # bono2 = models.FloatField()
    # dias_descanso = models.IntegerField()
    # dias_feriados = models.IntegerField()
    # asignaciones_dia_feriado = models.FloatField(null=True, blank=True)
    # SSO = models.FloatField(null=True, blank=True)
    # SPF = models.FloatField(null=True, blank=True)
    # LPH = models.FloatField(null=True, blank=True)
    # dias_no_laborados = models.IntegerField()
    prestamos = models.FloatField(null=True, blank=True)
    # cantidad_lunes = models.IntegerField()
    # total_asignaciones = models.FloatField(null=True, blank=True)
    # total_deducciones = models.FloatField(null=True, blank=True)
    total_pagar = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.empleado, self.total_pagar)

class Bancos(models.Model):
    nombre = models.CharField(max_length=120)
    cuenta = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    monto_disponible = models.FloatField()
    def __str__(self):
        return "%s %s %d" % (self.nombre, self.cuenta, self.monto_disponible)

class TipoEgreso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return  "%s" % (self.nombre)

class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleados
        fields = ('nombre', 'apellido', 'cedula','cargo', 'hoja_de_vida')


class CestaticketForm(ModelForm):
    class Meta:
        model = Cestatickets
        fields = ('fecha_inicio', 'fecha_fin', 'empleado', 'costo','dias_laborados','dias_nolaborados','unidad_tributaria')

class ConstantesForm(ModelForm):
    class Meta:
        model = Constantes_Administracion
        fields = ('nombre', 'valor')

class QuincenasForm(ModelForm):
    class Meta:
        model = Quincenas
        fields = ('fecha_inicio','fecha_fin','numero_semana','empleado','prestamos')

class BancosForm(ModelForm):
    class Meta:
        model = Bancos
        fields = ('nombre', 'cuenta','numero','monto_disponible')


class NominaForm(ModelForm):
    class Meta:
        model = Quincenas
        fields = ('numero_semana',)

class ServEmpForm(ModelForm):
    class Meta:
        model = Empleados
        fields = ('cedula',)
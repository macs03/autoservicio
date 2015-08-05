from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Vehiculos, Vehiculo_Clientes, Vehiculo_ClientesForm, VehiculosForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.

@login_required(login_url='/administracion')
def vehiculos(request):
	template = "vehiculos.html"
	vehiculos = Vehiculos.objects.all()
	value_boton = "Agregar"	
	if request.method=='POST':
		vehiculo_form = VehiculosForm(request.POST)
		if vehiculo_form.is_valid():
			new_vehiculo = vehiculo_form.save()

			return HttpResponseRedirect('/administracion/vehiculos')
	else:
		vehiculo_form  = VehiculosForm()
	return  render(request, template, locals())

@login_required(login_url='/administracion')
def vehiculos_edit(request, pk_id):
	template = "vehiculos.html"
	vehiculo_instance = get_object_or_404(Vehiculos, pk = pk_id)
	vehiculos = Vehiculos.objects.all()
	value_boton = "Editar"
	print vehiculo_instance
	if request.method=='POST':
		vehiculo_form = VehiculosForm(request.POST, instance=vehiculo_instance)
		if vehiculo_form.is_valid():
			new_empleado = vehiculo_form.save()

		return HttpResponseRedirect('/administracion/vehiculos')
	else:
		vehiculo_form = VehiculosForm(instance=vehiculo_instance)
		print vehiculo_form
		
	return  render(request, template, locals())

@login_required(login_url='/administracion')
def vehiculos_delete(request, pk_id):
	template = "vehiculos.html"
	vehiculo_instance = get_object_or_404(Vehiculos, pk = pk_id)
	vehiculo_instance.delete()
	return HttpResponseRedirect('/administracion/vehiculos')

@login_required(login_url='/administracion')
def asociar(request):
	template = "asociar.html"
	vehiculos_clientes = Vehiculo_Clientes.objects.all()
	value_boton = "Agregar"	
	if request.method=='POST':
		asociar_form = Vehiculo_ClientesForm(request.POST)
		if asociar_form.is_valid():
			new_asociar = asociar_form.save()

			return HttpResponseRedirect('/administracion/vehiculos/asociar')
	else:
		asociar_form  = Vehiculo_ClientesForm()
	return  render(request, template, locals())

@login_required(login_url='/administracion')
def asociar_edit(request, pk_id):
	template = "asociar.html"
	vehiculos_clientes = Vehiculo_Clientes.objects.all()
	vehiculos_clientes_instance = get_object_or_404(Vehiculo_Clientes, pk = pk_id)
	value_boton = "Editar"
	if request.method=='POST':
		asociar_form = Vehiculo_ClientesForm(request.POST, instance=vehiculos_clientes_instance)
		if asociar_form.is_valid():
			new_asociar = asociar_form.save()

			return HttpResponseRedirect('/administracion/vehiculos/asociar')
	else:
		asociar_form  = Vehiculo_ClientesForm(instance=vehiculos_clientes_instance)
	return  render(request, template, locals())


@login_required(login_url='/administracion')
def asociar_delete(request, pk_id):
	template = "vehiculos.html"
	vehiculos_clientes_instance = get_object_or_404(Vehiculo_Clientes, pk = pk_id)
	vehiculos_clientes_instance.delete()
	return HttpResponseRedirect('/administracion/vehiculos/asociar')
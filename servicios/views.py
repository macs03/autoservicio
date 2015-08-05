from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from servicios.models import Servicios, Servicios_Realizados, ServiciosForm, Servicios_RealizadosForm
from datetime import date
# Create your views here.


def inicio(request):
	template = "inicio.html"
	if request.method == 'POST':
		usuario = request.POST['username']
		clave = request.POST['password']
		user = authenticate(username=usuario, password=clave)
		if user is not None:
			if user.is_active:
 					print("User is valid, active and authenticated")
 					login(request, user)
 					return HttpResponseRedirect('/administracion')
			else:
				print("The password is valid, but the account has been disabled!")
		else:
			# the authentication system was unable to verify the username and password
			print("The username and password were incorrect.")
			log = True
			return  render(request, template, locals())

	fecha = date.today()

	return  render(request, template, locals())

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/administracion')



# Create your views here.

@login_required(login_url='/administracion')
def servicios(request):
	template = "servicios.html"
	servicios = Servicios.objects.all()
	value_boton = "Agregar"
	if request.method=='POST':
		servicio_form = ServiciosForm(request.POST)
		if servicio_form.is_valid():
			new_servicio = servicio_form.save()

			return HttpResponseRedirect('/administracion/servicios/')
	else:
		servicio_form  = ServiciosForm()
	return  render(request, template, locals())

@login_required(login_url='/administracion')
def servicios_edit(request, pk_id):
	template = "servicios.html"
	servicio_instance = get_object_or_404(Servicios, pk = pk_id)
	servicios = Servicios.objects.all()
	value_boton = "Editar"
	if request.method=='POST':
		servicio_form = ServiciosForm(request.POST, instance=servicio_instance)
		if servicio_form.is_valid():
			servicio_form.save()

		return HttpResponseRedirect('/administracion/servicios/')
	else:
		servicio_form = ServiciosForm(instance=servicio_instance)

	return  render(request, template, locals())

@login_required(login_url='/administracion')
def servicios_delete(request, pk_id):
	template = "servicios.html"
	servicio_instance = get_object_or_404(Servicios, pk = pk_id)
	servicio_instance.delete()
	return HttpResponseRedirect('/administracion/servicios/')

# Create your views here.
@login_required(login_url='/administracion')
def servicios_realizados(request):
	template = "servicios_realizados.html"
	servicios_realizados = Servicios_Realizados.objects.all()
	value_boton = "Agregar"
	if request.method=='POST':
		servicio_realizado_form = Servicios_RealizadosForm(request.POST)
		if servicio_realizado_form.is_valid():
			new_servicio = servicio_realizado_form.save()

			return HttpResponseRedirect('/administracion/servicios/realizados')
	else:
		servicio_realizado_form  = Servicios_RealizadosForm()
	return  render(request, template, locals())

@login_required(login_url='/administracion')
def servicios_realizados_edit(request, pk_id):
	template = "servicios_realizados.html"
	servicio_realizado_instance = get_object_or_404(Servicios_Realizados, pk = pk_id)
	servicios_realizados = Servicios_Realizados.objects.all()
	value_boton = "Editar"
	if request.method=='POST':
		servicio_realizado_form = Servicios_RealizadosForm(request.POST, instance=servicio_realizado_instance)
		if servicio_realizado_form.is_valid():
			servicio_realizado_form.save()

		return HttpResponseRedirect('/administracion/servicios/realizados')
	else:
		servicio_realizado_form = Servicios_RealizadosForm(instance=servicio_realizado_instance)

	return  render(request, template, locals())

@login_required(login_url='/administracion')
def servicios_realizados_delete(request, pk_id):
	template = "servicios_realizados.html"
	servicio_realizado_instance = get_object_or_404(Servicios_Realizados, pk = pk_id)
	servicio_realizado_instance.delete()
	return HttpResponseRedirect('/administracion/servicios/realizados')

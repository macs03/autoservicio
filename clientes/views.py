from django.shortcuts import render, get_object_or_404
from .models import Clientes, ClientesForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.

@login_required(login_url='/administracion')
def clientes(request):
	template = "clientes.html"
	clientes = Clientes.objects.all().order_by("-id")
	value_boton = "Agregar"
	if request.method=='POST':
		cliente_form = ClientesForm(request.POST)
		if cliente_form.is_valid():
			new_cliente = cliente_form.save()

			return HttpResponseRedirect('/administracion/clientes')
	else:
		cliente_form  = ClientesForm()
	return  render(request, template, locals())

@login_required(login_url='/administracion')
def clientes_edit(request, pk_id):
	template = "clientes.html"
	cliente_instance = get_object_or_404(Clientes, pk = pk_id)
	clientes = Clientes.objects.all()
	value_boton = "Editar"
	if request.method=='POST':
		cliente_form = ClientesForm(request.POST, instance=cliente_instance)
		if cliente_form.is_valid():
			new_empleado = cliente_form.save()

		return HttpResponseRedirect('/administracion/clientes')
	else:
		cliente_form = ClientesForm(instance=cliente_instance)
		
		
	return  render(request, template, locals())

@login_required(login_url='/administracion')
def clientes_delete(request, pk_id):
	template = "clientes.html"
	cliente_instance = get_object_or_404(Clientes, pk = pk_id)
	cliente_instance.delete()
	return HttpResponseRedirect('/administracion/clientes')

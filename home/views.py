from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from vehiculos.models import Vehiculos, Vehiculo_Clientes
from clientes.models import Clientes
from servicios.models import Servicios, Servicios_Realizados
import json

# Create your views here.

def home(request):
    template = "index.html"
    return render(request, template, locals())


def resultado(request):
    errors = []
    template = "result.html"
    if 'placa' in request.GET:
        placa = request.GET['placa']
        if not placa:
            print "no hay placa"
            errors.append('Por favor introduce una placa')
        elif len(placa)<=6 or len(placa)>=8:
            print "no cumple requisitos de placa"
            errors.append('Por favor introduce una placa valida')
        else:
            print "placa valida"
            print placa
            placaObj = get_object_or_404(Clientes, placa__icontains=placa)
            # placaObj = get_object_or_404(Vehiculos, placa__icontains=placa)
            #vehiculos = Vehiculos.objects.filter(placa__icontains=placa)
            # vehiculo_cliente = Clientes.objects.filter(vehiculo=placaObj)
            print "vehiculo encontrado"
            # print vehiculo_cliente
            print placaObj
            servicio_realizado = Servicios_Realizados.objects.all().order_by('-fecha')
            for servicio in servicio_realizado:
                placa =  servicio.vehiculo_cliente.placa
                print "placa buscada"
                print placa
                if placa == placaObj.placa :
                    placaexito = servicio.vehiculo_cliente
                    print placaexito
                    servicios_hechos =  Servicios_Realizados.objects.filter(vehiculo_cliente = placaexito)
                    print servicios_hechos
            return render(request, template, {'Cliente': placaObj, 'placa': placa , 'servicios_hechos' : servicios_hechos})
            

    return render(request,"index.html",{'errors': errors})



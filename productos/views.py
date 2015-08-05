# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
import json
import time
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Productos, ProductosForm, Factura, FacturasForm, Egresos, EgresosForm
from servicios.models import Servicios_Realizados, Servicios
from vehiculos.models import Vehiculo_Clientes
from empleados.models import Bancos
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from numero_letra import number_to_letter
# Create your views here.

@login_required(login_url='/administracion')
def productos(request):
    template = "productos.html"
    productos = Productos.objects.all()
    value_boton = "Agregar"
    if request.method == 'POST':
        producto_form = ProductosForm(request.POST)
        if producto_form.is_valid():
            new_producto = producto_form.save()

            return HttpResponseRedirect('/administracion/productos/')
    else:
        producto_form = ProductosForm()
    return render(request, template, locals())


@login_required(login_url='/administracion')
def productos_edit(request, pk_id):
    template = "productos.html"
    producto_instance = get_object_or_404(Productos, pk=pk_id)
    productos = Productos.objects.all()
    value_boton = "Editar"
    if request.method == 'POST':
        producto_form = ProductosForm(request.POST, instance=producto_instance)
        if producto_form.is_valid():
            new_producto = producto_form.save()

        return HttpResponseRedirect('/administracion/productos/')
    else:
        producto_form = ProductosForm(instance=producto_instance)

    return render(request, template, locals())


@login_required(login_url='/administracion')
def productos_delete(request, pk_id):
    template = "productos.html"
    producto_instance = get_object_or_404(Productos, pk=pk_id)
    producto_instance.delete()
    return HttpResponseRedirect('/administracion/productos/')


# Create your views here.
@login_required(login_url='/administracion')
def facturas(request):
    template = "factura.html"
    facturas = Factura.objects.all()
    servicios = Servicios_Realizados.objects.all()
    bancos = Bancos.objects.all()
    fecha_hoy = time.strftime("%d/%m/%y")
    productos = Productos.objects.filter(cantidad__gt = 0)


    clientes_vehiculos = Vehiculo_Clientes.objects.all()
    if request.method=='POST':
        print request.POST
        cliente_vehiculo = get_object_or_404(Vehiculo_Clientes, pk= request.POST['cliente'])
        fecha = request.POST['fecha']
        total = request.POST['total']
        banco_seleccionado = request.POST['bancos']
        if banco_seleccionado != 'none':

            print "banco seleccionado"
            bancos = Bancos.objects.filter(pk=banco_seleccionado)
            banco = bancos[0]
            print banco
        else:
            print "no selecciono banco"
            banco = None

        factura = Factura(cliente_vehiculo=cliente_vehiculo, fecha=fecha, total=total, banco=banco)
        factura.save()
        print dict(request.POST)["productos"]
        for servicio_pk in dict(request.POST)["servicios"]:
            servicio = get_object_or_404(Servicios_Realizados, pk=servicio_pk)
            factura.servicios.add(servicio)


        for producto_pk in dict(request.POST)["productos"]:
            producto = get_object_or_404(Productos, pk = producto_pk)
            cantidad = request.POST['cantidad-'+str(producto.pk)];
            cantidad = int(cantidad)
            producto.cantidad = producto.cantidad - cantidad
            producto.save()
            factura.productos.add(producto)

        serviciosFactura = factura.servicios.all()
        productosFactura = factura.productos.all()

        html = render_to_string('factura_pdf.html', {'pagesize':'A4', 'factura':factura,  'servicios': serviciosFactura, 'productos': productosFactura,'fecha_hoy':fecha_hoy,'banco':banco},context_instance=RequestContext(request))
        return generar_pdf(html)
        #return HttpResponseRedirect('/administracion/facturas/')

    return  render(request, template, locals())




@login_required(login_url='/administracion')
def facturas_delete(request, pk_id):
    template = "factura.html"
    factura_instance = get_object_or_404(Factura, pk=pk_id)
    factura_instance.delete()
    return HttpResponseRedirect('/administracion/facturas/')

@login_required(login_url='/administracion')
def facturas_print(request, pk_id):
    factura_instance = get_object_or_404(Factura, pk = pk_id)
    fecha_hoy = time.strftime("%d/%m/%y")
    consulta = Factura.objects.filter(pk = pk_id)
    banco = consulta[0].banco
    print banco
    serviciosFactura = consulta[0].servicios.all()
    productosFactura = consulta[0].productos.all()
    html = render_to_string('factura_pdf.html', {'pagesize':'A4', 'factura':consulta[0],'fecha_hoy':fecha_hoy,'servicios': serviciosFactura, 'productos': productosFactura,'banco':banco},context_instance=RequestContext(request))
    return generar_pdf(html)


# Create your views here.

@csrf_exempt
def get_servicios(request):
    id = request.POST.get('id')
    vehiculo_cliente = get_object_or_404(Vehiculo_Clientes, pk=id)
    servicios = Servicios_Realizados.objects.filter(vehiculo_cliente=vehiculo_cliente)
    response_data = []
    for servicio in servicios:
        response_serv = {}
        response_serv['id'] = servicio.pk
        response_serv['servicio'] = servicio.servicio.nombre
        response_serv['vehiculo_cliente'] = "%s - %s" % (
            servicio.vehiculo_cliente.cliente, servicio.vehiculo_cliente.vehiculo)
        response_serv['fecha'] = servicio.fecha.__str__()
        response_serv['costo'] = servicio.costo
        response_serv['empleado'] = servicio.empleado.nombre
        response_data.append(response_serv)

    # print json.dumps(response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


@login_required(login_url='/administracion')
def egresos(request):
    print "vista egresos"
    template = "egresos.html"
    egresos = Egresos.objects.all()
    fecha_hoy = time.strftime("%d/%m/%y")
    value_boton = "Generar"
    if request.method == 'POST':
        egresos_form = EgresosForm(request.POST, request.FILES)
        if egresos_form.is_valid():
            new_egreso = egresos_form.save()
            monto_letra = number_to_letter.to_word(int(new_egreso.monto))
            print monto_letra
            print request.POST['banco']
            bancos = Bancos.objects.filter(pk=request.POST['banco'])
            print bancos[0].monto_disponible
            monto_restante = bancos[0].monto_disponible - float(request.POST['monto'])
            print monto_restante
            Bancos.objects.update(monto_disponible = monto_restante)
            html = render_to_string('egresos_pdf.html', {'pagesize': 'A4', 'egresos': new_egreso,'fecha_hoy':fecha_hoy,'monto_letra': monto_letra},
                            context_instance=RequestContext(request))
            return generar_pdf(html)
    else:
        egresos_form = EgresosForm()



    return render(request, template, locals())


@login_required(login_url='/administracion')
def egresos_delete(request, pk_id):
    egresos_instance = get_object_or_404(Egresos, pk=pk_id)
    egresos_instance.delete()
    return HttpResponseRedirect('/administracion/egresos')

@login_required(login_url='/administracion')
def egresos_print(request, pk_id):
    egreso_instance = get_object_or_404(Egresos, pk = pk_id)
    fecha_hoy = time.strftime("%d/%m/%y")
    consulta = Egresos.objects.filter(pk = pk_id)
    monto_letra = number_to_letter.to_word(int(consulta[0].monto))
    print monto_letra
    html = render_to_string('egresos_pdf.html', {'pagesize':'A4', 'egresos':consulta[0],'fecha_hoy':fecha_hoy, 'monto_letra': monto_letra},context_instance=RequestContext(request))
    return generar_pdf(html)

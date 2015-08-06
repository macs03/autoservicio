from django.shortcuts import render, get_object_or_404
from servicios.models import Servicios_Realizados
from .models import Empleados, Cestatickets ,Constantes_Administracion,Quincenas,Control_Empleados,Bancos
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import EmpleadosForm, CestaticketForm, ConstantesForm,QuincenasForm,BancosForm,NominaForm,ServEmpForm
from django.http.response import HttpResponse, HttpResponseRedirect
from productos.views import generar_pdf
from django.template.loader import render_to_string
from django.template import RequestContext
import time, calendar
# Create your views here.

@login_required(login_url='/administracion')
def empleados(request):
    template = "empleados.html"
    empleados = Empleados.objects.all()
    value_boton = "Agregar"
    if request.method == 'POST':
        empleado_form = EmpleadosForm(request.POST, request.FILES)
        if empleado_form.is_valid():
            new_empleado = empleado_form.save()

            return HttpResponseRedirect('/administracion/empleados')
    else:
        empleado_form = EmpleadosForm()
    return render(request, template, locals())


@login_required(login_url='/administracion')
def empleados_edit(request, pk_id):
    template = "empleados.html"
    empleado_instance = get_object_or_404(Empleados, pk=pk_id)
    empleados = Empleados.objects.all()
    value_boton = "Editar"
    print empleado_instance
    if request.method == 'POST':
        empleado_form = EmpleadosForm(request.POST, request.FILES, instance=empleado_instance)
        if empleado_form.is_valid():
            new_empleado = empleado_form.save()

        return HttpResponseRedirect('/administracion/empleados')
    else:
        empleado_form = EmpleadosForm(instance=empleado_instance)
        print empleado_form

    return render(request, template, locals())


@login_required(login_url='/administracion')
def empleados_delete(request, pk_id):
    template = "empleados.html"
    empleado_instance = get_object_or_404(Empleados, pk=pk_id)
    empleado_instance.delete()
    return HttpResponseRedirect('/administracion/empleados')


@login_required(login_url='/administracion')
def nomina(request):
    print "vista nomina"
    template = "nomina.html"
    errors = []
    value_boton = "Generar"
    fecha_hoy = time.strftime("%d/%m/%y")
    quincenas = Quincenas.objects.all()
    if request.method == 'GET':
        nomina_form = NominaForm(request.GET,request.FILES)
        if(nomina_form.is_valid()):
            print request.GET
            print "-------------------quincena"
            numero_quincena = request.GET['numero_quincena']
            if not numero_quincena:
                print "no hay quincena"
                errors.append('Por favor introduce un numero de quincena')
            else:
                print "si hay quincena"
                #quincena_valida = get_object_or_404(Quincenas, numero_quincena=numero_quincena)
                print numero_quincena
                print type(numero_quincena)
                numero = int(numero_quincena)
                quincena_valida = Quincenas.objects.filter(numero_quincena = numero).order_by('pk')
                print quincena_valida
                fecha_inicio = quincena_valida[0].fecha_inicio
                print fecha_inicio
                fecha_fin = quincena_valida[0].fecha_fin
                print fecha_fin
                fecha_final = str(fecha_fin)
                corte = fecha_final.split('-')
                print "ultimo dia ----"
                dia_final = corte[2]
                print dia_final
                print type(fecha_final)
                consulta2 = None
                fecha_inicio_c = None
                fecha_fin_C = None
                acum_nomina = 0
                acum_cestaticket = 0
                for dato in quincena_valida:
                    print dato.empleado.nombre
                    print dato.empleado.apellido
                    print dato.numero_quincena
                    print dato.dias_laborados
                    print dato.bono1_pagar
                    print dato.bono2
                    print dato.dias_descanso
                    print dato.dias_feriados
                    print dato.asignaciones_dia_laborado
                    asignaciones = dato.asignaciones_dia_laborado + dato.asignaciones_dia_feriado
                    print asignaciones
                    print dato.SSO
                    print dato.SPF
                    print dato.LPH
                    print dato.dias_no_laborados
                    print dato.prestamos
                    deducciones = dato.SSO - dato.SPF - dato.LPH
                    print deducciones
                    print dato.total_pagar
                    acum_nomina = acum_nomina + dato.total_pagar

                if dia_final == '31' or dia_final == '30' or dia_final == '29' or dia_final == '28' :
                    print "hay cestaticket"
                    consulta2 = Cestatickets.objects.filter(fecha_fin=fecha_fin).order_by('pk')
                    fecha_inicio_c = consulta2[0].fecha_inicio
                    fecha_fin_C = consulta2[0].fecha_fin
                    for ticket in consulta2:
                        print ticket.empleado.nombre
                        print ticket.empleado.apellido
                        print ticket.empleado.cedula
                        print ticket.fecha_inicio
                        print ticket.fecha_fin
                        print ticket.total_pagar
                        acum_cestaticket = acum_cestaticket + ticket.total_pagar


                html = render_to_string('nomina_pdf.html', {'pagesize':'A4', 'nomina':quincena_valida, 'cestaticket':consulta2,'fecha_hoy':fecha_hoy ,'fecha_inicio':fecha_inicio,'fecha_fin':fecha_fin ,'fecha_inicio_c' : fecha_inicio_c ,'fecha_fin_C': fecha_fin_C, 'acum_nomina':acum_nomina,'acum_cestaticket':acum_cestaticket},context_instance=RequestContext(request))
                return generar_pdf(html)

    return render(request, template, locals())

@login_required(login_url='/administracion')
def constantes(request):
    print "vista constante"
    template = "constantes.html"
    constantes = Constantes_Administracion.objects.all()
    value_boton = "Guardar"
    if request.method == 'POST':
        constantes_form = ConstantesForm(request.POST, request.FILES)
        if constantes_form.is_valid():

            new_constante = constantes_form.save()
    else:
        constantes_form = ConstantesForm()

    return render(request, template, locals())

@login_required(login_url='/administracion')
def constantes_delete(request, pk_id):
	constantes_instance = get_object_or_404(Constantes_Administracion, pk = pk_id)
	constantes_instance.delete()
	return HttpResponseRedirect('/administracion/constantes')

@login_required(login_url='/administracion')
def constantes_edit(request, pk_id):
    template = "constantes.html"
    constantes_instance = get_object_or_404(Constantes_Administracion, pk=pk_id)
    constantes = Constantes_Administracion.objects.all()
    value_boton = "Editar"
    print constantes_instance
    if request.method == 'POST':
        constantes_form = ConstantesForm(request.POST, request.FILES, instance=constantes_instance)
        if constantes_form.is_valid():
            new_constante = constantes_form.save()

        return HttpResponseRedirect('/administracion/constantes')
    else:
        constantes_form = ConstantesForm(instance=constantes_instance)
        print constantes_form

    return render(request, template, locals())

@login_required(login_url='/administracion')
def cestaticket(request):
    print "vista cestaticket"
    template = "cestaticket.html"
    cestaticket = Cestatickets.objects.all()
    value_boton = "Generar"
    fecha_hoy = time.strftime("%d/%m/%y")
    if request.method == 'POST':
        cestaticket_form = CestaticketForm(request.POST, request.FILES)
        if cestaticket_form.is_valid():

            new_cestaticket = cestaticket_form.save()
            print new_cestaticket.costo.valor
            total = new_cestaticket.costo.valor * new_cestaticket.dias_laborados
            new_cestaticket.total_pagar =  total
            print total
            print fecha_hoy
            new_cestaticket.save()
            #return HttpResponseRedirect('/administracion/empleados/cestaticket')
            html = render_to_string('cestaticket_pdf.html', {'pagesize':'A4', 'cestaticket':new_cestaticket,'fecha_hoy':fecha_hoy},context_instance=RequestContext(request))
            return generar_pdf(html)
    else:
        cestaticket_form = CestaticketForm()

    return render(request, template, locals())

@login_required(login_url='/administracion')
def cestaticket_delete(request, pk_id):
	cestaticket_instance = get_object_or_404(Cestatickets, pk = pk_id)
	cestaticket_instance.delete()
	return HttpResponseRedirect('/administracion/empleados/cestaticket')

@login_required(login_url='/administracion')
def cestaticket_print(request, pk_id):
    cestaticket_instance = get_object_or_404(Cestatickets, pk = pk_id)
    fecha_hoy = time.strftime("%d/%m/%y")
    consulta = Cestatickets.objects.filter(pk = pk_id)
    html = render_to_string('cestaticket_pdf.html', {'pagesize':'A4', 'cestaticket':consulta[0],'fecha_hoy':fecha_hoy},context_instance=RequestContext(request))
    return generar_pdf(html)

@login_required(login_url='/administracion')
def quincena(request):
    print "vista quincena"
    template = "quincena.html"
    quincena = Quincenas.objects.all()
    value_boton = "Generar"
    fecha_hoy = time.strftime("%d/%m/%y")
    if request.method == 'POST':
        quincena_form = QuincenasForm(request.POST, request.FILES)
        if quincena_form.is_valid():

            new_quincena = quincena_form.save()
            empleados = Servicios_Realizados.objects.filter(empleado=new_quincena.empleado)
            for dato in empleados:
                print dato
                if dato.fecha < new_quincena.fecha_fin and dato.fecha > new_quincena.fecha_inicio:
                    print "servicio hecho en quincena"
                    servicio_hechos = len(empleados)
                    print servicio_hechos
                    bono1 = servicio_hechos * new_quincena.bono1.valor
                    print bono1
                    new_quincena.bono1_pagar = bono1
                    sueldos = Empleados.objects.filter(nombre=new_quincena.empleado.nombre)
                    print "sueldo base"
                    print sueldos
                    sueldo = sueldos[0].sueldo_base
                    print sueldo
                    print "------"
                    asignacion_laborado = (sueldo/new_quincena.dias_mes)*new_quincena.dias_laborados
                    print asignacion_laborado
                    new_quincena.asignaciones_dia_laborado= asignacion_laborado
                    #bono1 = servicio_hechos * new_quincena.bono1.valor
                    #print bono1
                    print new_quincena.bono2
                    #new_quincena.bono1_pagar = bono1
                    asignacion_feriado = (new_quincena.dias_feriados*(sueldo/new_quincena.dias_mes))*1.5
                    print  asignacion_feriado
                    new_quincena.asignaciones_dia_feriado = asignacion_feriado
                    print "menos"
                    SSO = (((sueldo * 12)/52)*new_quincena.cantidad_lunes)*0.4
                    print SSO
                    new_quincena.SSO = SSO
                    SPF = (asignacion_laborado + asignacion_feriado) * 0.005
                    print SPF
                    new_quincena.SPF =SPF
                    LPH = (asignacion_laborado + asignacion_feriado) * 0.01
                    print LPH
                    new_quincena.LPH = LPH
                    total_asignacion = asignacion_laborado + asignacion_feriado + bono1 + new_quincena.bono2
                    total_deduccion = SSO + SPF + LPH + new_quincena.prestamos
                    new_quincena.total_asignaciones = total_asignacion
                    new_quincena.total_deducciones = total_deduccion
                    total = (asignacion_laborado + asignacion_feriado + bono1 + new_quincena.bono2) - (SSO + SPF + LPH)
                    print total

                    new_quincena.total_pagar = total

                    new_quincena.save()
                else:
                    print "no hay servicios hechos"
                    servicio_hechos = 0
                    print servicio_hechos
                    bono1 = servicio_hechos * new_quincena.bono1.valor
                    print bono1
                    new_quincena.bono1_pagar = bono1
                    sueldos = Empleados.objects.filter(nombre=new_quincena.empleado.nombre)
                    print "sueldo base"
                    print sueldos
                    sueldo = sueldos[0].sueldo_base
                    print sueldo
                    print "------"
                    asignacion_laborado = (sueldo/new_quincena.dias_mes)*new_quincena.dias_laborados
                    print asignacion_laborado
                    new_quincena.asignaciones_dia_laborado= asignacion_laborado
                    #bono1 = servicio_hechos * new_quincena.bono1.valor
                    #print bono1
                    print new_quincena.bono2
                    #new_quincena.bono1_pagar = bono1
                    asignacion_feriado = (new_quincena.dias_feriados*(sueldo/new_quincena.dias_mes))*1.5
                    print  asignacion_feriado
                    new_quincena.asignaciones_dia_feriado = asignacion_feriado
                    print "menos"
                    SSO = (((sueldo * 12)/52)*new_quincena.cantidad_lunes)*0.4
                    print SSO
                    new_quincena.SSO = SSO
                    SPF = (asignacion_laborado + asignacion_feriado) * 0.005
                    print SPF
                    new_quincena.SPF =SPF
                    LPH = (asignacion_laborado + asignacion_feriado) * 0.01
                    print LPH
                    total_asignacion = asignacion_laborado + asignacion_feriado + bono1 + new_quincena.bono2
                    total_deduccion = SSO + SPF + LPH + new_quincena.prestamos
                    new_quincena.total_asignaciones = total_asignacion
                    new_quincena.total_deducciones = total_deduccion
                    total = (asignacion_laborado + asignacion_feriado + bono1 + new_quincena.bono2) - (SSO + SPF + LPH)
                    print total

                    new_quincena.total_pagar = total

                    new_quincena.save()


            html = render_to_string('quincena_pdf.html', {'pagesize':'A4', 'quincena':new_quincena,'fecha_hoy':fecha_hoy},context_instance=RequestContext(request))
            return generar_pdf(html)

            #return HttpResponseRedirect('/administracion/empleados/quincena')
    else:
        quincena_form = QuincenasForm()

    return render(request, template, locals())

@login_required(login_url='/administracion')
def quincena_delete(request, pk_id):
	quincena_instance = get_object_or_404(Quincenas, pk = pk_id)
	quincena_instance.delete()
	return HttpResponseRedirect('/administracion/empleados/quincena')

@login_required(login_url='/administracion')
def quincena_print(request, pk_id):
    quincena_instance = get_object_or_404(Quincenas, pk = pk_id)
    fecha_hoy = time.strftime("%d/%m/%y")
    consulta = Quincenas.objects.filter(pk = pk_id)
    html = render_to_string('quincena_pdf.html', {'pagesize':'A4', 'quincena':consulta[0],'fecha_hoy':fecha_hoy},context_instance=RequestContext(request))
    return generar_pdf(html)


@login_required(login_url='/administracion')
def bancos(request):
    print "vista bancos"
    template = "bancos.html"
    bancos = Bancos.objects.all()
    value_boton = "Guardar"
    if request.method == 'POST':
        bancos_form = BancosForm(request.POST, request.FILES)
        if bancos_form.is_valid():

            new_banco = bancos_form.save()
    else:
        bancos_form = BancosForm()

    return render(request, template, locals())

@login_required(login_url='/administracion')
def bancos_delete(request, pk_id):
	bancos_instance = get_object_or_404(Bancos, pk = pk_id)
	bancos_instance.delete()
	return HttpResponseRedirect('/administracion/bancos')

@login_required(login_url='/administracion')
def bancos_edit(request, pk_id):
    template = "bancos.html"
    bancos_instance = get_object_or_404(Bancos, pk=pk_id)
    bancos = Bancos.objects.all()
    value_boton = "Editar"
    print bancos_instance
    if request.method == 'POST':
        bancos_form = BancosForm(request.POST, request.FILES, instance=bancos_instance)
        if bancos_form.is_valid():
            new_banco = bancos_form.save()

        return HttpResponseRedirect('/administracion/bancos')
    else:
        constantes_form = ConstantesForm(instance=bancos_instance)


    return render(request, template, locals())

@login_required(login_url='/administracion')
def serv_empl(request):
    template = "serv_empl.html"
    ser_empl_form = ServEmpForm(request.GET,request.FILES)
    empleados = Empleados.objects.all()
    fecha_hoy = time.strftime("%d/%m/%y")
    value_boton = "Consultar"
    if request.method == 'GET':
        if (ser_empl_form.is_valid()):
            print request.GET
            print "..........................empleado"
            empleado = request.GET['cedula']
            print empleado
            fecha_inicio = request.GET.get('fecha_inicio','')
            print "........fecha1"
            print fecha_inicio
            print type(fecha_inicio)
            fecha_inicio_S = str(fecha_inicio)
            print type(fecha_inicio_S)
            fecha_S_split = fecha_inicio_S.split('-')
            dia_inicio = fecha_S_split[0]
            print  dia_inicio
            dia_inicio_I = int(dia_inicio)
            mes_inicio = fecha_S_split[1]
            print  mes_inicio
            mes_inicio_I = int(mes_inicio)
            ano_inicio = fecha_S_split[2]
            print  ano_inicio
            ano_inicio_I = int(ano_inicio)


            fecha_fin = request.GET.get('fecha_fin','')
            print "........fecha2"
            print fecha_fin
            print type(fecha_fin)
            fecha_fin_S = str(fecha_fin)
            print type(fecha_fin_S)
            fecha_S_split2 = fecha_fin_S.split('-')
            dia_inicio2 = fecha_S_split2[0]
            print  dia_inicio2
            dia_inicio_I2 = int(dia_inicio2)
            mes_inicio2 = fecha_S_split2[1]
            print  mes_inicio2
            mes_inicio_I2 = int(mes_inicio2)
            ano_inicio2 = fecha_S_split2[2]
            print  ano_inicio2
            ano_inicio_I2 = int(ano_inicio2)

            empleado_ingresado = Empleados.objects.filter(cedula = empleado)
            print empleado_ingresado

            servicios = Servicios_Realizados.objects.filter(empleado = empleado_ingresado)
            print servicios
            for servicio in servicios:
                fecha = servicio.fecha
                print fecha
                print type(fecha)
                fecha_S = str(fecha)
                print type(fecha_S)

                fecha_S_split3 = fecha_S.split('-')
                dia_inicio3 = fecha_S_split3[0]
                print  dia_inicio3
                dia_inicio_I3 = int(dia_inicio3)
                mes_inicio3 = fecha_S_split3[1]
                print  mes_inicio3
                mes_inicio_I3 = int(mes_inicio3)
                ano_inicio3 = fecha_S_split3[2]
                print  ano_inicio3
                ano_inicio_I3 = int(ano_inicio3)

                if ano_inicio3 >= ano_inicio and ano_inicio3 <=ano_inicio2:
                    print "estamos dentro del rango de ano"
                    if mes_inicio3 >= mes_inicio and mes_inicio3 <=mes_inicio2:
                        print "estamos en el rago de meses"
                        if dia_inicio3 >= dia_inicio and dia_inicio3 <=dia_inicio2:
                            print "estamos en el rago de dias"
                            html = render_to_string('serv_empl_pdf.html', {'pagesize':'A4', 'empleado':empleado_ingresado, 'servicios':servicios,'fecha_hoy':fecha_hoy ,'fecha_inicio':fecha_inicio,'fecha_fin':fecha_fin },context_instance=RequestContext(request))
                            return generar_pdf(html)
                        else:
                            print "fuera de rango"
                    else:
                        print "fuera de rango"
                else:
                    print "fuera de rango"



    return render(request, template, locals())
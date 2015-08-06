from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^$', 'empleados.views.empleados', name='empleados'),
    url(r'^edit/(\d+)$', 'empleados.views.empleados_edit', name='editEmpleado'),
    url(r'^delete/(\d+)$', 'empleados.views.empleados_delete', name='deleteEmpleado'),
    url(r'^nomina/$', 'empleados.views.nomina', name='nomina'),
    url(r'^servicio-empleado/$', 'empleados.views.serv_empl', name='serv_empl'),
    url(r'^cestaticket/$', 'empleados.views.cestaticket', name='cestaticket'),
    url(r'^cestaticket/delete(\d+)$', 'empleados.views.cestaticket_delete', name='cestaticket_delete'),
    url(r'^cestaticket/print(\d+)$', 'empleados.views.cestaticket_print', name='cestaticket_print'),
    url(r'^quincena/$', 'empleados.views.quincena', name='quincena'),
    url(r'^quincena/delete(\d+)$', 'empleados.views.quincena_delete', name='quincena_delete'),
    url(r'^quincena/print(\d+)$', 'empleados.views.quincena_print', name='quincena_print'),
]
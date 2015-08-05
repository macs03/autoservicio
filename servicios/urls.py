from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^$', 'servicios.views.servicios', name='servicios'),
    url(r'^edit/(\d+)$', 'servicios.views.servicios_edit', name='editServicio'),
    url(r'^delete/(\d+)$', 'servicios.views.servicios_delete', name='deleteServicio'),
    url(r'^realizados/$', 'servicios.views.servicios_realizados', name='serviciosRealizados'),
    url(r'^realizados/edit/(\d+)$', 'servicios.views.servicios_realizados_edit', name='editServicioRealizado'),
    url(r'^realizados/delete/(\d+)$', 'servicios.views.servicios_realizados_delete', name='deleteServicioRealizado'),
    
]
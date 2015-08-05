from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^resultado/$', 'home.views.resultado', name='resultado'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^logout/$', 'servicios.views.logout_view', name='logout'),
    url(r'^administracion/$', 'servicios.views.inicio', name='inicio'),
    url(r'^administracion/empleados/', include("empleados.urls")),
    url(r'^administracion/clientes/', include("clientes.urls")),
    url(r'^administracion/vehiculos/', include("vehiculos.urls")),
    url(r'^administracion/productos/', include("productos.urls")),
    url(r'^administracion/servicios/', include("servicios.urls")),
    url(r'^administracion/facturas/$', 'productos.views.facturas', name='productos'),
    url(r'^administracion/facturas/delete/(\d+)$', 'productos.views.facturas_delete', name='deleteFactura'),
    url(r'^administracion/facturas/print/(\d+)$', 'productos.views.facturas_print', name='printFactura'),
    url(r'^administracion/egresos/$', 'productos.views.egresos', name='egresos'),
    url(r'^administracion/egresos/delete/(\d+)$', 'productos.views.egresos_delete', name='deleteEgreso'),
    url(r'^administracion/egresos/print/(\d+)$', 'productos.views.egresos_print', name='printEgreso'),
    url(r'^administracion/constantes/$', 'empleados.views.constantes', name='constantes'),
    url(r'^administracion/constantes/delete/(\d+)$', 'empleados.views.constantes_delete', name='deleteConstante'),
    url(r'^administracion/constantes/edit/(\d+)$', 'empleados.views.constantes_edit', name='editConstante'),
    url(r'^administracion/bancos/$', 'empleados.views.bancos', name='bancos'),
    url(r'^administracion/bancos/delete/(\d+)$', 'empleados.views.bancos_delete', name='deleteBancos'),
    url(r'^administracion/bancos/edit/(\d+)$', 'empleados.views.bancos_edit', name='editBancos'),
    url(r'^administracion/getservicios/', 'productos.views.get_servicios', name='serviciosGet'),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

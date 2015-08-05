from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^$', 'vehiculos.views.vehiculos', name='vehiculos'),
    url(r'^edit/(\d+)$', 'vehiculos.views.vehiculos_edit', name='editVehiculo'),
    url(r'^delete/(\d+)$', 'vehiculos.views.vehiculos_delete', name='deleteVehiculo'),
    url(r'^asociar/$', 'vehiculos.views.asociar', name='asociar'),
    url(r'^asociar/edit/(\d+)$', 'vehiculos.views.asociar_edit', name='editAsociar'),
    url(r'^asociar/delete/(\d+)$', 'vehiculos.views.asociar_delete', name='deleteAsociar'),
]
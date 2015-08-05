from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^$', 'clientes.views.clientes', name='clientes'),
    url(r'^edit/(\d+)$', 'clientes.views.clientes_edit', name='editCliente'),
    url(r'^delete/(\d+)$', 'clientes.views.clientes_delete', name='deleteCliente'),
]
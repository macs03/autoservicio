from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^$', 'productos.views.productos', name='productos'),
    url(r'^edit/(\d+)$', 'productos.views.productos_edit', name='editProducto'),
    url(r'^delete/(\d+)$', 'productos.views.productos_delete', name='deleteProducto'),
    
]
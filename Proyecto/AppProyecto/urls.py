from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path('',inicio,name="inicio"),
    path('categoria/',categoria, name="categoria"),
    path('cliente/',cliente, name="cliente"),
    path('producto/',producto, name="producto"),
    path('formulario-producto/',formProducto,name="formularioProducto"),
    path('formulario-categoria/',formCategoria,name="formularioCategoria"),
    path('formulario-cliente/',formCliente,name="formularioCliente"),
]
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import FormProducto

# Create your views here.

def inicio(req):
    return render(req, "inicio.html")

def categoria(req):
    return render(req, "categoria.html")

def cliente(req):
    return render(req, "cliente.html")

def producto(req):
    return render(req, "producto.html")

def formProducto(req):
    print('method',req.method)
    print('POST',req.POST)

    if req.method == 'POST':
        miFormulario=FormProducto(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            producto=Producto(nombre=data['nombre'],descripcion=data['descripcion'],precio=data['precio'])
            producto.save()

        return render(req,"formProducto.html")
    
    else:
        miFormulario=FormProducto()
        return render(req, "formProducto.html",{"miFormulario":miFormulario})

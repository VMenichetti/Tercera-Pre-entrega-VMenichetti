from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import FormProducto,FormCategoria,FormCliente

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
    
def formCategoria(req):
    print('method',req.method)
    print('POST',req.POST)

    if req.method == 'POST':
        miFormulario=FormCategoria(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            categoria=Categoria(nombre=data['nombre'])
            categoria.save()

        return render(req,"formCategoria.html")
    
    else:
        miFormulario=FormCategoria()
        return render(req, "formCategoria.html",{"miFormulario":miFormulario})

def formCliente(req):
    print('method',req.method)
    print('POST',req.POST)

    if req.method == 'POST':
        miFormulario=FormCliente(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            categoria=Cliente(usuario=data['usuario'],edad=data['edad'],email=data['email'],direccion=data['direccion'])
            categoria.save()

        return render(req,"formCliente.html")
    
    else:
        miFormulario=FormCliente()
        return render(req, "formCliente.html",{"miFormulario":miFormulario})

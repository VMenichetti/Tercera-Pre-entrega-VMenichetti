from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(req):
    return render(req, "inicio.html")

def categoria(req):
    return render(req, "categoria.html")

def cliente(req):
    return render(req, "cliente.html")

def producto(req):
    return render(req, "producto.html")
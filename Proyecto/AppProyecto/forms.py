from django import forms

class FormProducto(forms.Form):
    nombre=forms.CharField(max_length=40)
    descripcion=forms.CharField(max_length=80)
    precio=forms.DecimalField(max_digits=10, decimal_places=2)  
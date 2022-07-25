from django import forms

class FormularioCliente(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    documento=forms.IntegerField()
    email=forms.EmailField()

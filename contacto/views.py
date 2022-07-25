from django.shortcuts import redirect, render
from .forms import FormContacto

# Create your views here.

def contacto(request):
    formulario_contacto=FormContacto()
    
    if request.method == 'POST':
        formulario_contacto=FormContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')

            return redirect('/contacto/?valido')



    return render(request, 'contacto/contacto.html',{'miFormulario': formulario_contacto})
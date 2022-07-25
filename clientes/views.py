from django.shortcuts import render, redirect
from .models import Clientes
from .forms import FormularioCliente
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='Loguear')
def clientes(request):

    clientes = Clientes.objects.all()

    contexto = {'clientes': clientes}

    return render (request, 'clientes/clientes.html', contexto )

def formclientes(request):

    if request.method == 'POST':

        miFormulario=FormularioCliente(request.POST)

        if miFormulario.is_valid():

            informacion=miFormulario.cleaned_data

            cliente= Clientes(nombre=informacion['nombre'], apellido=informacion['apellido'], documento=informacion['documento'], email=informacion['email'])

            cliente.save()

            return redirect('Clientes')
    else:
        
        miFormulario=FormularioCliente()

        return render(request, 'clientes/formclientes.html',{'miFormulario': miFormulario} )

def busqueda(request):
    if request.GET['busca']:

        docu=request.GET['busca']
        clien=Clientes.objects.filter(documento__icontains=docu)
        return render(request, 'clientes/resultado_busqueda.html', {'clientes':clien, 'documento':docu})
    else:

        respuesta='Datos incorrectos'

        return render(request, 'clientes/clientes.html', respuesta)

def eliminar(request, cliente_nombre):

    cliente = Clientes.objects.get(nombre=cliente_nombre)
    cliente.delete()

    clientes = Clientes.objects.all()
    contexto = {'clientes':clientes}
    return render(request, 'clientes/clientes.html', contexto)

def edicioncliente(request, cliente_nombre):
    cliente=Clientes.objects.get(nombre=cliente_nombre)

    if request.method == 'POST':
        miFormulario=FormularioCliente(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            cliente.nombre = informacion['nombre']
            cliente.apellido = informacion['apellido']
            cliente.documento = informacion['documento']
            cliente.email = informacion['email']

            cliente.save()

            return redirect('Clientes')
    else:

        miFormulario=FormularioCliente(initial={'nombre':cliente.nombre, 'apellido':cliente.apellido, 'documento':cliente.documento, 'email':cliente.email})

    
    return render(request, 'clientes/editarclientes.html', {'miFormulario':miFormulario,  'cliente_nombre':cliente_nombre})



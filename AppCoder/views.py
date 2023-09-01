from django.shortcuts import render
from .models import Cliente
from django.http import HttpResponse

# Create your views here.
def cliente(req, nombre, apellido):

    cliente = Cliente(nombre=nombre, apellido=apellido)
    cliente.save()

    return HttpResponse(f"""
        <p>Cliente: {cliente.nombre} {cliente.apellido} agendado</p>
    """)

def lista_clientes(req):

    lista = Cliente.objects.all()

    return render(req, "lista_clientes.html", {"lista_cliente": lista})
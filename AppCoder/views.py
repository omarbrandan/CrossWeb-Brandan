from django.shortcuts import render
from .models import Athlete, Competitions, Store
from django.http import HttpResponse
from .forms import AthleteFormulario, CompetitionsFormulario, StoreFormulario

# Create your views here.
def athletes(req, nombre, apellido):

    athletes = Athlete(nombre=nombre, apellido=apellido)
    athletes.save()

def lista_athletes(req):

    lista = Athlete.objects.all()

    return render(req, "lista_athletes.html", {"lista_athletes": lista})

def inicio(req):

    return render(req, "inicio.html")

def athletes(req):

    return render(req, "athletes.html")


def competitions(req):

    return render(req, "competitions.html")


def store(req):

    return render(req, "store.html")

def athletes_formulario(req):

    if req.method == 'POST':

        miFormulario = AthleteFormulario(req.POST)

        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            athletes = Athlete(nombre=data["nombre"], apellido=data["apellido"])
            athletes.save()
            return render(req, "inicio.html", {"mensaje": "Registro de atleta creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
        
    else:

        miFormulario = AthleteFormulario()

        return render(req, "athletes_formulario.html", {"miFormulario": miFormulario})
    
def competitions_formulario(req):

    if req.method == 'POST':

        miFormulario = CompetitionsFormulario(req.POST)

        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            competitions = Competitions(nombre=data["nombre"], arena=data["arena"])
            competitions.save()
            return render(req, "inicio.html", {"mensaje": "Registro de competición creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
        
    else:

        miFormulario = CompetitionsFormulario()

        return render(req, "competitions_formulario.html", {"miFormulario": miFormulario})
    
def store_formulario(req):

    if req.method == 'POST':

        miFormulario = StoreFormulario(req.POST)

        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            store = Store(producto=data["producto"], precio=data["precio"])
            store.save()
            return render(req, "inicio.html", {"mensaje": "Registro de producto creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
        
    else:

        miFormulario = StoreFormulario()

        return render(req, "store_formulario.html", {"miFormulario": miFormulario})
    
def busqueda_apellido(req):

    return render(req, "busqueda_apellido.html")

def buscar(req):

    if req.GET["apellido"]:
        apellido = req.GET["apellido"]
        athletes = Athlete.objects.get(apellido=apellido)
        return render(req, "resultado_busqueda.html", {"athletes": athletes})
    else:
        return HttpResponse('No escribiste ningún apellido')
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
            return render(req, "inicio.html", {"mensaje": "Athlete creado con éxito"})
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
            return render(req, "inicio.html", {"mensaje": "Competition creada con éxito"})
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
            return render(req, "inicio.html", {"mensaje": "Producto creado con éxito"})
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
    
def lista_athletes(req):

    athletes = Athlete.objects.all()

    return render(req, "leerAthletes.html", {"athletes": athletes})

def lista_competitions(req):

    competitions = Competitions.objects.all()

    return render(req, "leerCompetitions.html", {"competitions": competitions})

def lista_store(req):

    store = Store.objects.all()

    return render(req, "leerStore.html", {"store": store})

def crea_athletes(req):

    if req.method == 'POST':

        miFormulario = AthleteFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            athletes = Athlete(nombre=data["nombre"], apellido=data["apellido"])
            athletes.save()
            return render(req, "inicio.html", {"mensaje": "Athlete creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
        
    else:

        miFormulario = AthleteFormulario()

        return render(req, "athletes_formulario.html", {"miFormulario": miFormulario})
    
def crea_competitions(req):

    if req.method == 'POST':

        miFormulario = CompetitionsFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            competitions = Competitions(nombre=data["nombre"], arena=data["arena"])
            competitions.save()
            return render(req, "inicio.html", {"mensaje": "Competition creada con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
        
    else:

        miFormulario = CompetitionsFormulario()

        return render(req, "competitions_formulario.html", {"miFormulario": miFormulario})
    
def crea_store(req):

    if req.method == 'POST':

        miFormulario = StoreFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            store = Store(producto=data["producto"], precio=data["precio"])
            store.save()
            return render(req, "inicio.html", {"mensaje": "Producto creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
        
    else:

        miFormulario = StoreFormulario()

        return render(req, "store_formulario.html", {"miFormulario": miFormulario})
    
def elimina_athletes(req, id):

    if req.method == 'POST':

        athletes = Athlete.objects.get(id=id)
        athletes.delete()

        athletes = Athlete.objects.all()

        return render(req, "leerAthletes.html", {"athletes": athletes})
    
def elimina_competitions(req, id):

    if req.method == 'POST':

        competitions = Competitions.objects.get(id=id)
        competitions.delete()

        competitions = Competitions.objects.all()

        return render(req, "leerCompetitions.html", {"competitions": competitions})
    
def elimina_store(req, id):

    if req.method == 'POST':

        store = Store.objects.get(id=id)
        store.delete()

    store = Store.objects.all()

    return render(req, "leerStore.html", {"store": store})

def editar_athletes(req, id):

    athletes = Athlete.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = AthleteFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            athletes.nombre = data["nombre"]
            athletes.apellido = data["apellido"]
            athletes.save()
            return render(req, "inicio.html", {"mensaje": "Athlete actualizado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Actualización inválida"})
        
    else:

        miFormulario = AthleteFormulario(initial={
            "nombre": athletes.nombre,
            "apellido": athletes.apellido,
        })

        return render(req, "editar_athletes.html", {"miFormulario": miFormulario, "id": athletes.id})
    
def editar_competitions(req, id):

    competitions = Competitions.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = CompetitionsFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            competitions.nombre = data["nombre"]
            competitions.arena = data["arena"]
            competitions.save()
            return render(req, "inicio.html", {"mensaje": "Competition actualizada con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Actualización inválida"})
        
    else:

        miFormulario = CompetitionsFormulario(initial={
            "nombre": competitions.nombre,
            "arena": competitions.arena,
        })

        return render(req, "editar_competitions.html", {"miFormulario": miFormulario, "id": competitions.id})
    
def editar_store(req, id):

    store = Store.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = StoreFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            store.producto = data["producto"]
            store.precio = data["precio"]
            store.save()
            return render(req, "inicio.html", {"mensaje": "Producto actualizado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Actualización inválida"})
        
    else:

        miFormulario = StoreFormulario(initial={
            "producto": store.producto,
            "arena": store.precio,
        })

        return render(req, "editar_store.html", {"miFormulario": miFormulario, "id": store.id})
    

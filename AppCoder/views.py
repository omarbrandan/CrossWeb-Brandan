from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Athlete, Competitions, Store, Avatar
from .forms import AthleteFormulario, CompetitionsFormulario, StoreFormulario, UserEditForm, AvatarFormulario

# Create your views here.
def athletes(req, nombre, apellido):

    athletes = Athlete(nombre=nombre, apellido=apellido)
    athletes.save()

def competitions(req, nombre, arena):

    competitions = Competitions(nombre=nombre, arena=arena)
    competitions.save()

def store(req, producto, precio):

    store = Competitions(producto=producto, precio=precio)
    store.save()

#def lista_athletes(req):
#
#    lista = Athlete.objects.all()
#
#    return render(req, "lista_athletes.html", {"lista_athletes": lista})

def inicio(req):

    try:

        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url": avatar.imagen.url})
    
    except:
        return render(req, "inicio.html")

#def athletes(req):
#
#    return render(req, "athletes.html")
#
#
#def competitions(req):
#
#    return render(req, "competitions.html")
#
#
#def store(req):
#
#    return render(req, "store.html")
#
#def athletes_formulario(req):
#
#    if req.method == 'POST':
#
#        miFormulario = AthleteFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            print(miFormulario.cleaned_data)
#            data = miFormulario.cleaned_data
#
#            athletes = Athlete(nombre=data["nombre"], apellido=data["apellido"])
#            athletes.save()
#            return render(req, "inicio.html", {"mensaje": "Athlete creado con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
#        
#    else:
#
#        miFormulario = AthleteFormulario()
#
#        return render(req, "athletes_formulario.html", {"miFormulario": miFormulario})
#    
#def competitions_formulario(req):
#
#    if req.method == 'POST':
#
#        miFormulario = CompetitionsFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            print(miFormulario.cleaned_data)
#            data = miFormulario.cleaned_data
#
#            competitions = Competitions(nombre=data["nombre"], arena=data["arena"])
#            competitions.save()
#            return render(req, "inicio.html", {"mensaje": "Competition creada con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
#        
#    else:
#
#        miFormulario = CompetitionsFormulario()
#
#        return render(req, "competitions_formulario.html", {"miFormulario": miFormulario})
#    
#def store_formulario(req):
#
#    if req.method == 'POST':
#
#        miFormulario = StoreFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            print(miFormulario.cleaned_data)
#            data = miFormulario.cleaned_data
#
#            store = Store(producto=data["producto"], precio=data["precio"])
#            store.save()
#            return render(req, "inicio.html", {"mensaje": "Producto creado con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
#        
#    else:
#
#        miFormulario = StoreFormulario()
#
#        return render(req, "store_formulario.html", {"miFormulario": miFormulario})
    
def busqueda_apellido(req):

    return render(req, "busqueda_apellido.html")

def buscar(req):

    try:

        if req.GET["apellido"]:
            apellido = req.GET["apellido"]
            athletes = Athlete.objects.get(apellido=apellido)
            return render(req, "resultado_busqueda.html", {"athletes": athletes})
        
        else:
            return render(req, "inicio.html")
    
    except:
        return render(req, "busqueda_fallida.html")
    
def lista_athletes(req):

    athletes = Athlete.objects.all()

    return render(req, "leer_athletes.html", {"athletes": athletes})

def lista_competitions(req):

    competitions = Competitions.objects.all()

    return render(req, "leer_competitions.html", {"competitions": competitions})

#def lista_store(req):
#
#    store = Store.objects.all()
#
#    return render(req, "leer_store.html", {"store": store})

#def crea_athletes(req):
#
#    if req.method == 'POST':
#
#        miFormulario = AthleteFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            data = miFormulario.cleaned_data
#
#            athletes = Athlete(nombre=data["nombre"], apellido=data["apellido"])
#            athletes.save()
#            return render(req, "inicio.html", {"mensaje": "Athlete creado con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
#        
#    else:
#
#        miFormulario = AthleteFormulario()
#
#        return render(req, "athletes_formulario.html", {"miFormulario": miFormulario})
#    
#def crea_competitions(req):
#
#    if req.method == 'POST':
#
#        miFormulario = CompetitionsFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            data = miFormulario.cleaned_data
#
#            competitions = Competitions(nombre=data["nombre"], arena=data["arena"])
#            competitions.save()
#            return render(req, "inicio.html", {"mensaje": "Competition creada con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
#        
#    else:
#
#        miFormulario = CompetitionsFormulario()
#
#        return render(req, "competitions_formulario.html", {"miFormulario": miFormulario})
#    
#def crea_store(req):
#
#    if req.method == 'POST':
#
#        miFormulario = StoreFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            data = miFormulario.cleaned_data
#
#            store = Store(producto=data["producto"], precio=data["precio"])
#            store.save()
#            return render(req, "inicio.html", {"mensaje": "Producto creado con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Registro inválido"})
#        
#    else:
#
#        miFormulario = StoreFormulario()
#
#        return render(req, "store_formulario.html", {"miFormulario": miFormulario})
    
#def elimina_athletes(req, id):
#
#    if req.method == 'POST':
#
#        athletes = Athlete.objects.get(id=id)
#        athletes.delete()
#
#        athletes = Athlete.objects.all()
#
#        return render(req, "leer_athletes.html", {"athletes": athletes})
    
#def elimina_competitions(req, id):
#
#    if req.method == 'POST':
#
#        competitions = Competitions.objects.get(id=id)
#        competitions.delete()
#
#        competitions = Competitions.objects.all()
#
#        return render(req, "leer_competitions.html", {"competitions": competitions})
#    
#def elimina_store(req, id):
#
#    if req.method == 'POST':
#
#        store = Store.objects.get(id=id)
#        store.delete()
#
#    store = Store.objects.all()
#
#    return render(req, "leer_store.html", {"store": store})

#def editar_athletes(req, id):
#
#    athletes = Athlete.objects.get(id=id)
#
#    if req.method == 'POST':
#
#        miFormulario = AthleteFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            data = miFormulario.cleaned_data
#
#            athletes.nombre = data["nombre"]
#            athletes.apellido = data["apellido"]
#            athletes.save()
#            return render(req, "inicio.html", {"mensaje": "Athlete actualizado con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Actualización inválida"})
#        
#    else:
#
#        miFormulario = AthleteFormulario(initial={
#            "nombre": athletes.nombre,
#            "apellido": athletes.apellido,
#        })
#
#        return render(req, "editar_athletes.html", {"miFormulario": miFormulario, "id": athletes.id})
#    
#def editar_competitions(req, id):
#
#    competitions = Competitions.objects.get(id=id)
#
#    if req.method == 'POST':
#
#        miFormulario = CompetitionsFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            data = miFormulario.cleaned_data
#
#            competitions.nombre = data["nombre"]
#            competitions.arena = data["arena"]
#            competitions.save()
#            return render(req, "inicio.html", {"mensaje": "Competition actualizada con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Actualización inválida"})
#        
#    else:
#
#        miFormulario = CompetitionsFormulario(initial={
#            "nombre": competitions.nombre,
#            "arena": competitions.arena,
#        })
#
#        return render(req, "editar_competitions.html", {"miFormulario": miFormulario, "id": competitions.id})
#    
#def editar_store(req, id):
#
#    store = Store.objects.get(id=id)
#
#    if req.method == 'POST':
#
#        miFormulario = StoreFormulario(req.POST)
#
#        if miFormulario.is_valid():
#
#            data = miFormulario.cleaned_data
#
#            store.producto = data["producto"]
#            store.precio = data["precio"]
#            store.save()
#            return render(req, "inicio.html", {"mensaje": "Producto actualizado con éxito"})
#        else:
#            return render(req, "inicio.html", {"mensaje": "Actualización inválida"})
#        
#    else:
#
#        miFormulario = StoreFormulario(initial={
#            "producto": store.producto,
#            "arena": store.precio,
#        })
#
#        return render(req, "editar_store.html", {"miFormulario": miFormulario, "id": store.id})
   
class AthleteList(ListView):
    model = Athlete
    template_name = "athletes_list.html"
    context_object_name = "athletes"

class AthleteDetail(DetailView):
    model = Athlete
    template_name = "athletes_detail.html"
    context_object_name = "athletes"

class AthleteCreate(LoginRequiredMixin, CreateView):
    model = Athlete
    template_name = "athletes_create.html"
    fields = ["nombre", "apellido"]
    success_url = "/app-coder/lista-athletes/"

class AthleteUpdate(LoginRequiredMixin, UpdateView):
    model = Athlete
    template_name = "athletes_update.html"
    fields = ("__all__")
    success_url = "/app-coder/lista-athletes/"

class AthleteDelete(LoginRequiredMixin, DeleteView):
    model = Athlete
    template_name = "athletes_delete.html"
    success_url = "/app-coder/lista-athletes/"


class CompetitionsList(ListView):
    model = Competitions
    template_name = "competitions_list.html"
    context_object_name = "competitions"


class CompetitionsDetail(DetailView):
    model = Competitions
    template_name = "competitions_detail.html"
    context_object_name = "competitions"

class CompetitionsCreate(LoginRequiredMixin, CreateView):
    model = Competitions
    template_name = "competitions_create.html"
    fields = ["nombre", "arena"]
    success_url = "/app-coder/lista-competitions/"

class CompetitionsUpdate(LoginRequiredMixin, UpdateView):
    model = Competitions
    template_name = "competitions_update.html"
    fields = ("__all__")
    success_url = "/app-coder/lista-competitions/"

class CompetitionsDelete(LoginRequiredMixin, DeleteView):
    model = Competitions
    template_name = "competitions_delete.html"
    success_url = "/app-coder/lista-competitions/"

    
class StoreList(ListView):
    model = Store
    template_name = "store_list.html"
    context_object_name = "store"


class StoreDetail(DetailView):
    model = Store
    template_name = "store_detail.html"
    context_object_name = "store"

class StoreCreate(LoginRequiredMixin, CreateView):
    model = Store
    template_name = "store_create.html"
    fields = ["producto", "precio"]
    success_url = "/app-coder/lista-store/"

class StoreUpdate(LoginRequiredMixin, UpdateView):
    model = Store
    template_name = "store_update.html"
    fields = ("__all__")
    success_url = "/app-coder/lista-store/"

class StoreDelete(LoginRequiredMixin, DeleteView):
    model = Store
    template_name = "store_delete.html"
    success_url = "/app-coder/lista-store/"

def login_view(req):

    if req.method == 'POST':
        
        miFormulario = AuthenticationForm(req, data=req.POST) 

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"¡Bienvenido {usuario}!"})
            else:
                return render(req, "inicio.html", {"mensaje": f"Datos incorrectos"})
        
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})
    
def register(req):

    if req.method == 'POST':
        
        miFormulario = UserCreationForm(req.POST) 

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"] 

            miFormulario.save()

            return render(req, "inicio.html", {"mensaje": f"¡Usuario {usuario} creado con éxito!"})
        
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})
    
def editar_perfil(req):

    usuario = req.user

    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "¡Perfil actualizado con éxito!"})
        else:
            return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
        
    else:

        miFormulario = UserEditForm(instance=req.user)
        
        return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
    
def agregar_avatar(req):

    if req.method == 'POST':
        
        miFormulario = AvatarFormulario(req.POST, req.FILES) 

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": f"¡Avatar actualizado con éxito!"})
        
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregar_avatar.html", {"miFormulario": miFormulario})
    
def about(req):

    return render(req, "about.html")

def busqueda_fallida(req):

    return render(req, "busqueda_fallida.html")
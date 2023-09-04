from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('athletes/', athletes, name='Athletes'),
    path('competitions/', competitions, name='Competitions'),
    path('store/', store, name='Store'),
    path('athletes-formulario/', athletes_formulario, name='AthletesFormulario'),
    path('competitions-formulario/', competitions_formulario, name='CompetitionsFormulario'),
    path('store-formulario/', store_formulario, name='StoreFormulario'),
    path('busqueda-apellido/', busqueda_apellido, name='BusquedaApellido'),
    path('buscar/', buscar, name='Buscar'),
]
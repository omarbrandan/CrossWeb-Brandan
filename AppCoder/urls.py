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
    path('lista-athletes/', lista_athletes, name='ListaAthletes'),
    path('lista-competitions/', lista_competitions, name='ListaCompetitions'),
    path('lista-store/', lista_store, name='ListaStore'),
    path('crea-athletes/', crea_athletes, name='CreaAthletes'),
    path('crea-competitions/', crea_competitions, name='CreaCompetitions'),
    path('crea-store/', crea_store, name='CreaStore'),
    path('elimina-athletes/<int:id>', elimina_athletes, name='EliminaAthletes'),
    path('elimina-competitions/<int:id>', elimina_competitions, name='EliminaCompetitions'),
    path('elimina-store/<int:id>', elimina_store, name='EliminaStore'),
    path('editar-athletes/<int:id>', editar_athletes, name='EditarAthletes'),
    path('editar-competitions/<int:id>', editar_competitions, name='EditarCompetitions'),
    path('editar-store/<int:id>', editar_store, name='EditarStore'),
]
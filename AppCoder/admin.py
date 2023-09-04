from django.contrib import admin
from .models import *

class AthleteAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido']

class CompetitionsAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'arena']
    search_fields = ['nombre']

class StoreAdmin(admin.ModelAdmin):
    list_display = ['producto', 'precio']
    search_fields = ['producto']

# Register your models here.
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Competitions, CompetitionsAdmin)
admin.site.register(Store, StoreAdmin)
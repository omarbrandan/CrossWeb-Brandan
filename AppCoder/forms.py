from django import forms

class AthleteFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)

class CompetitionsFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    arena = forms.CharField(required=True)

class StoreFormulario(forms.Form):

    producto = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
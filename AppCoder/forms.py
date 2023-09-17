from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Athlete, Competitions, Store, Avatar

#class AthleteFormulario(forms.Form):
#
#    nombre = forms.CharField(required=True)
#    apellido = forms.CharField(required=True)

class AthleteFormulario(forms.ModelForm):

    class Meta:
        model=Athlete
        fields=('__all__')

#class CompetitionsFormulario(forms.Form):
#
#    nombre = forms.CharField(required=True)
#    arena = forms.CharField(required=True)

class CompetitionsFormulario(forms.ModelForm):

    class Meta:
        model=Competitions
        fields=('__all__')

#class StoreFormulario(forms.Form):
#
#    producto = forms.CharField(required=True)
#    precio = forms.IntegerField(required=True)

class StoreFormulario(forms.ModelForm):

    class Meta:
        model=Store
        fields=('__all__')

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)
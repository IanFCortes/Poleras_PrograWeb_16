# PENDIENTE
from .models import polera, equipo, usuario, carrito, soporte
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


#class LoginForm(AuthenticationForm):
#    pass


class RegistroForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombre', 'apellido', 'rut', 'numero_celular', 'fecha_nacimiento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['rut'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero_celular'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_nacimiento'].widget.attrs.update({'class': 'form-control', 'type': 'date'})

# PENDIENTE
from .models import usuario, envio
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


#class LoginForm(AuthenticationForm):
#    pass


class RegistroForm(UserCreationForm):
    rut = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero_celular = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_nacimiento = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            usuario.objects.create(
                user=user,
                rut=self.cleaned_data['rut'],
                direccion=self.cleaned_data['direccion'],
                numero_celular=self.cleaned_data['numero_celular'],
                fecha_nacimiento=self.cleaned_data['fecha_nacimiento']
            )
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EnvioForm(forms.ModelForm):
    class Meta:
        model = envio
        fields = ['direccion', 'ciudad', 'codigo_postal', 'pais', 'fecha_envio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['ciudad'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_postal'].widget.attrs.update({'class': 'form-control'})
        self.fields['pais'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_envio'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
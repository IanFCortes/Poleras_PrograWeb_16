# PENDIENTE
from .models import usuario, envio, polera, equipo, soporte, envio, Seguimiento
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils import timezone


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
    CIUDADES_CHOICES = [
        ('Santiago', 'Santiago'),
        ('Linares', 'Linares'),
        ('Chillán', 'Chillán'),
        ('Concepción', 'Concepción'),
        ('Temuco', 'Temuco'),
        ('Valdivia', 'Valdivia'),
        ('Osorno', 'Osorno'),
        ('Puerto Montt', 'Puerto Montt'),
        ('Coyhaique', 'Coyhaique'),
        ('Punta Arenas', 'Punta Arenas'),
    ]

    ciudad = forms.ChoiceField(choices=CIUDADES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = envio
        fields = ['direccion', 'ciudad', 'codigo_postal', 'pais']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['ciudad'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_postal'].widget.attrs.update({'class': 'form-control'})
        self.fields['pais'].widget = forms.HiddenInput()
        self.fields['pais'].initial = 'Chile'
class PoleraForm(forms.ModelForm):
    class Meta:
        model = polera
        fields = ['nombre', 'precio', 'talla', 'equipo', 'logo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'talla': forms.TextInput(attrs={'class': 'form-control'}),
            'equipo': forms.Select(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = equipo
        fields = ['nombre', 'logo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UsuarioForm(forms.ModelForm):
    admin = forms.BooleanField(required=False, label="Convertir a Admin")

    class Meta:
        model = usuario
        fields = ['rut', 'direccion', 'numero_celular', 'fecha_nacimiento', 'admin']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_celular': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.user.is_superuser:
            self.fields.pop('admin')

class SoporteForm(forms.ModelForm):
    class Meta:
        model = soporte
        fields = ['titulo', 'mensaje']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del mensaje'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mensaje', 'rows': 5}),
        }

class ActualizarPerfilForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['rut', 'direccion', 'numero_celular', 'fecha_nacimiento']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_celular': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = ['estado', 'comentario']
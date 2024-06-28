from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import RegistroForm, LoginForm, PoleraForm, EquipoForm, UsuarioForm, SoporteForm, EnvioForm
from .models import equipo, polera, usuario, soporte, carrito, ItemCarrito
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

# Create your views here.

def inicio(request):
    return render(request,'app/main/index.html')

def udechile(request):

    equipo_u = equipo.objects.get(nombre='udechile')
    poleras = polera.objects.filter(equipo=equipo_u)
    return render(request,'app/equipo/udechile.html', {'poleras': poleras})

def ucatolica(request):

    equipo_uc = equipo.objects.get(nombre='ucatolica')
    poleras = polera.objects.filter(equipo=equipo_uc)

    return render(request,'app/equipo/ucatolica.html', {'poleras': poleras})

def colocolo(request):
    equipo_colo = equipo.objects.get(nombre='colocolo')
    poleras = polera.objects.filter(equipo=equipo_colo)
    return render(request,'app/equipo/colocolo.html', {'poleras': poleras})

def huachipato(request):
    equipo_huachipato = equipo.objects.get(nombre='huachipato')
    poleras = polera.objects.filter(equipo=equipo_huachipato)
    return render(request,'app/equipo/huachipato.html', {'poleras': poleras})

def pago(request):
    return render(request,'app/acciones/pago.html')

def soporteadmin(request):
    return render(request,'app/admin/soporteadmin.html')

def home(request):
    return render(request,'app/admin/home.html')

def usuarioadmin(request):
    return render(request,'app/admin/usuarioadmin.html')

def equipoadmin(request):
    return render(request,'app/admin/equipoadmin.html')

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'app/acciones/login.html'

    def get_success_url(self):
        return reverse_lazy('Inicio')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Inicio')  # Redirige a la página de inicio después del registro
    else:
        form = RegistroForm()
    return render(request,'app/acciones/registro.html', {'form': form})  

def logout_view(request):
    logout(request)  
    return render(request,'app/main/index.html')

# def login_view(request): 
#     mensaje = ""
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('inicio')
#         else:
#             mensaje = "Mal ahí, no se pudo autenticar"
#     else:
#         form = LoginForm(request)
#     contexto = {
#         "form": form,
#         "mensaje": mensaje
#     }
#     return render(request, 'app/login.html', contexto)


## ADMIIIIIIIIIN

def polera_admin(request):
    equipos = equipo.objects.all()
    equipo_id = request.GET.get('equipo')
    if equipo_id:
        poleras = polera.objects.filter(equipo_id=equipo_id)
    else:
        poleras = polera.objects.all()
    return render(request, 'app/admin/poleradmin.html', {'poleras': poleras, 'equipos': equipos})

def editar_polera(request, pk=None):
    if pk:
        polera_obj = get_object_or_404(polera, pk=pk)
    else:
        polera_obj = polera()
    
    if request.method == 'POST':
        form = PoleraForm(request.POST, request.FILES, instance=polera_obj)
        if form.is_valid():
            form.save()
            return redirect('polera_admin')
    else:
        form = PoleraForm(instance=polera_obj)
    
    return render(request, 'app/admin/editarpolera.html', {'form': form, 'polera': polera_obj})

def eliminar_polera(request, pk):
    polera_obj = get_object_or_404(polera, pk=pk)
    polera_obj.delete()
    return redirect('polera_admin')

#crud equipo

def equipo_admin(request):
    equipos = equipo.objects.all()
    return render(request, 'app/admin/equipoadmin.html', {'equipos': equipos})

def editar_equipo(request, pk=None):
    if pk:
        equipo_obj = get_object_or_404(equipo, pk=pk)
    else:
        equipo_obj = equipo()
    
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo_obj)
        if form.is_valid():
            form.save()
            return redirect('equipo_admin')
    else:
        form = EquipoForm(instance=equipo_obj)
    
    return render(request, 'app/admin/editarequipo.html', {'form': form, 'equipo': equipo_obj})

def eliminar_equipo(request, pk):
    equipo_obj = get_object_or_404(equipo, pk=pk)
    equipo_obj.delete()
    return redirect('equipo_admin')

#usuario

def usuario_admin(request):
    usuarios = usuario.objects.all()
    return render(request, 'app/admin/usuarioadmin.html', {'usuarios': usuarios})

def editar_usuario(request, pk):
    usuario_obj = get_object_or_404(usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario_obj)
        if form.is_valid():
            form.save()
            return redirect('usuario_admin')
    else:
        form = UsuarioForm(instance=usuario_obj)
    
    return render(request, 'app/admin/usuarioeditar.html', {'form': form, 'usuario': usuario_obj})

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_admin')
    else:
        form = RegistroForm()
    return render(request, 'app/admin/usuarioeditar.html', {'form': form, 'usuario': None})

def eliminar_usuario(request, pk):
    usuario_obj = get_object_or_404(usuario, pk=pk)
    usuario_obj.delete()
    return redirect('usuario_admin')

@login_required
def enviar_soporte(request):
    if request.method == 'POST':
        form = SoporteForm(request.POST)
        if form.is_valid():
            soporte = form.save(commit=False)
            soporte.usuario = request.user.usuario 
            soporte.save()
            messages.success(request, 'Tu mensaje ha sido enviado al soporte.')
            return redirect('soporte_exito_view')
    else:
        form = SoporteForm()
    
    return render(request, 'app/acciones/soporte.html', {'form': form})

def soporte(request):
    if request.user.is_authenticated:
        return enviar_soporte(request)
    else:
        messages.info(request, 'Debes iniciar sesión para acceder al soporte.')
        return redirect('login')
    
def soporte_exito_view(request):
    return render(request, 'app/main/soporte_exito.html')

@login_required
def agregar_al_carrito(request, polera_id):
    polera_instance = get_object_or_404(polera, id=polera_id)
    carrito, created = carrito.objects.get_or_create(usuario=request.user.usuario)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, polera=polera_instance)
    
    if not created:
        item.cantidad += 1
        item.save()

    carrito.total += polera_instance.precio
    carrito.save()

    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = get_object_or_404(carrito, usuario=request.user.usuario)
    items = ItemCarrito.objects.filter(carrito=carrito)
    return render(request, 'app/acciones/carrito.html', {'carrito': carrito, 'items': items})

@login_required
def realizar_compra(request):
    carrito_actual = get_object_or_404(carrito, usuario=request.user.usuario)
    items = ItemCarrito.objects.filter(carrito=carrito_actual)
    
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            envio = form.save(commit=False)
            envio.usuario = request.user.usuario
            envio.fecha_envio = timezone.now()
            envio.save()
            carrito_actual.total = 0
            carrito_actual.save()
            items.delete()

            return render(request, 'app/acciones/compra_exito.html', {'envio': envio})
    else:
        form = EnvioForm()

    return render(request, 'app/acciones/realizar_compra.html', {'carrito': carrito_actual, 'items': items, 'form': form})
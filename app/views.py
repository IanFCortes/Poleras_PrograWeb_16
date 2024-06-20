from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm

# Create your views here.

def inicio(request):
    return render(request,'app/main/index.html')

def udechile(request):
    return render(request,'app/equipo/udechile.html')

def ucatolica(request):
    return render(request,'app/equipo/ucatolica.html')

def colocolo(request):
    return render(request,'app/equipo/colocolo.html')

def huachipato(request):
    return render(request,'app/equipo/huachipato.html')

def soporte(request):
    return render(request,'app/acciones/soporte.html')

def pago(request):
    return render(request,'app/acciones/pago.html')

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
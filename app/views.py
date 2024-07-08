from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from .forms import RegistroForm, LoginForm, PoleraForm, EquipoForm, UsuarioForm, SoporteForm, EnvioForm, ActualizarPerfilForm, SeguimientoForm
from .models import equipo, polera, usuario, soporte, carrito, ItemCarrito, Compra, CompraItem, ItemPedido, Pedido, Seguimiento
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db import IntegrityError
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied




# Create your views here.
def check_bloqueado(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'usuario') and request.user.usuario.bloqueado:
            raise PermissionDenied("Tu cuenta está bloqueada.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def inicio(request):
    return render(request,'app/main/index.html')

def udechile(request):

    equipo_u = equipo.objects.get(nombre='udechile')
    poleras = polera.objects.filter(equipo=equipo_u)

    if request.method == 'POST':
        polera_id = request.POST.get('polera_id')
        polera_obj = get_object_or_404(polera, id=polera_id)
        carrito_obj, created = carrito.objects.get_or_create(usuario=request.user.usuario)
        item, created = itemcarrito.objects.get_or_create(carrito=carrito_obj, item=polera_obj)
        if not created:
            item.cantidad += 1
            item.save()
        carrito_obj.total += polera_obj.precio
        carrito_obj.save()
        return redirect('ver_carrito')

    return render(request,'app/equipo/udechile.html', {'poleras': poleras})

def ucatolica(request):

    equipo_uc = equipo.objects.get(nombre='ucatolica')
    poleras = polera.objects.filter(equipo=equipo_uc)

    if request.method == 'POST':
        polera_id = request.POST.get('polera_id')
        polera_obj = get_object_or_404(polera, id=polera_id)
        carrito_obj, created = carrito.objects.get_or_create(usuario=request.user.usuario)
        item, created = itemcarrito.objects.get_or_create(carrito=carrito_obj, item=polera_obj)
        if not created:
            item.cantidad += 1
            item.save()
        carrito_obj.total += polera_obj.precio
        carrito_obj.save()
        return redirect('ver_carrito')

    return render(request,'app/equipo/ucatolica.html', {'poleras': poleras})

@login_required
def colocolo(request):
    equipo_colo = equipo.objects.get(nombre='colocolo')
    poleras = polera.objects.filter(equipo=equipo_colo)

    if request.method == 'POST':
        polera_id = request.POST.get('polera_id')
        polera_obj = get_object_or_404(polera, id=polera_id)
        carrito_obj, created = carrito.objects.get_or_create(usuario=request.user.usuario)
        item, created = itemcarrito.objects.get_or_create(carrito=carrito_obj, item=polera_obj)
        if not created:
            item.cantidad += 1
            item.save()
        carrito_obj.total += polera_obj.precio
        carrito_obj.save()
        return redirect('ver_carrito')

    return render(request, 'app/equipo/colocolo.html', {'poleras': poleras})

def huachipato(request):
    equipo_huachipato = equipo.objects.get(nombre='huachipato')
    poleras = polera.objects.filter(equipo=equipo_huachipato)

    if request.method == 'POST':
        polera_id = request.POST.get('polera_id')
        polera_obj = get_object_or_404(polera, id=polera_id)
        carrito_obj, created = carrito.objects.get_or_create(usuario=request.user.usuario)
        item, created = itemcarrito.objects.get_or_create(carrito=carrito_obj, item=polera_obj)
        if not created:
            item.cantidad += 1
            item.save()
        carrito_obj.total += polera_obj.precio
        carrito_obj.save()
        return redirect('ver_carrito')

    return render(request,'app/equipo/huachipato.html', {'poleras': poleras})

def pago(request):
    return render(request,'app/acciones/pago.html')

@login_required
def gestionar_soporte(request):
    if not request.user.is_superuser:
        return redirect('Inicio')

    mensajes = soporte.objects.all().order_by('-titulo')

    context = {
        'mensajes': mensajes,
    }
    return render(request, 'app/admin/soporteadmin.html', context)

@login_required
def detalle_soporte_admin(request, mensaje_id):
    if not request.user.is_superuser:
        return redirect('Inicio')  

    mensaje = get_object_or_404(soporte, id=mensaje_id)  

    if request.method == 'POST':
        mensaje.delete()
        messages.success(request, 'Mensaje de soporte eliminado con éxito.')
        return redirect('gestionar_soporte')

    context = {
        'mensaje': mensaje,
    }
    return render(request, 'app/admin/detalle_soporte_admin.html', context)

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
            try:
                user = form.save()
                login(request, user)
                return redirect('Inicio')
            except IntegrityError:
                form.add_error(None, 'Ya existe un usuario con estos datos.')
        else:
            form.add_error(None, 'El formulario no es válido. Por favor, verifica los datos ingresados.')
    else:
        form = RegistroForm()
    return render(request, 'app/acciones/registro.html', {'form': form})
def logout_view(request):
    logout(request)  
    return render(request,'app/main/index.html')



@check_bloqueado
def polera_admin(request):
    if not request.user.is_superuser:
        return redirect('Inicio')  
    equipos = equipo.objects.all()
    equipo_id = request.GET.get('equipo')
    if equipo_id:
        poleras = polera.objects.filter(equipo_id=equipo_id)
    else:
        poleras = polera.objects.all()
    return render(request, 'app/admin/poleradmin.html', {'poleras': poleras, 'equipos': equipos})

@check_bloqueado
def editar_polera(request, pk=None):
    if not request.user.is_superuser:
        return redirect('Inicio')  
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

@check_bloqueado
def eliminar_polera(request, pk):
    if not request.user.is_superuser:
        return redirect('Inicio')  
    polera_obj = get_object_or_404(polera, pk=pk)
    polera_obj.delete()
    return redirect('polera_admin')

#crud equipo

@check_bloqueado
def equipo_admin(request):
    if not request.user.is_superuser:
        return redirect('Inicio')  
    equipos = equipo.objects.all()
    return render(request, 'app/admin/equipoadmin.html', {'equipos': equipos})

@check_bloqueado
def editar_equipo(request, pk=None):
    if not request.user.is_superuser:
        return redirect('Inicio')  
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

@check_bloqueado
def eliminar_equipo(request, pk):
    if not request.user.is_superuser:
        return redirect('Inicio')  
    equipo_obj = get_object_or_404(equipo, pk=pk)
    equipo_obj.delete()
    return redirect('equipo_admin')

#usuario

@check_bloqueado
def usuario_admin(request):
    if not request.user.is_superuser:
        return redirect('Inicio')  
    usuarios = usuario.objects.all()
    return render(request, 'app/admin/usuarioadmin.html', {'usuarios': usuarios})

@check_bloqueado
@login_required
def editar_usuario(request, pk):
    if not request.user.is_superuser:
        return redirect('Inicio')  
    usuario_obj = get_object_or_404(usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario_obj)
        if form.is_valid():
            usuario_form = form.save(commit=False)
            if form.cleaned_data['admin']:
                usuario_obj.user.is_superuser = True
                usuario_obj.user.is_staff = True  
            else:
                usuario_obj.user.is_superuser = False
                usuario_obj.user.is_staff = False
            usuario_obj.user.save()
            usuario_form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('usuario_admin')
    else:
        form = UsuarioForm(instance=usuario_obj)

    return render(request, 'app/admin/usuarioeditar.html', {'form': form, 'usuario': usuario_obj})
@check_bloqueado
@login_required
def registrar_usuario(request):
    if not request.user.is_superuser:
        return redirect('Inicio')  
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_admin')
    else:
        form = RegistroForm()
    return render(request, 'app/admin/usuarioeditar.html', {'form': form, 'usuario': None})

@login_required
def bloquear_usuario(request, pk):
    if not request.user.is_superuser:
        return redirect('Inicio')
    
    usuario_obj = get_object_or_404(usuario, pk=pk)
    
    usuario_obj.bloquear()
    messages.success(request, 'El usuario ha sido bloqueado exitosamente.')
    return redirect('usuario_admin')

@login_required
def desbloquear_usuario(request, pk):
    if not request.user.is_superuser:
        return redirect('Inicio')
    
    usuario_obj = get_object_or_404(usuario, pk=pk)
    
    usuario_obj.desbloquear()
    messages.success(request, 'El usuario ha sido desbloqueado exitosamente.')
    return redirect('usuario_admin')


@login_required
def eliminar_usuario(request, pk):
    if not request.user.is_superuser:
        return redirect('Inicio')
    
    usuario_obj = get_object_or_404(usuario, pk=pk)

    if Pedido.objects.filter(usuario=usuario_obj).exists():
        usuario_obj.bloquear()
        messages.success(request, 'El usuario ha sido bloqueado porque tiene pedidos asociados.')
    else:
        usuario_obj.delete()
        messages.success(request, 'El usuario ha sido eliminado exitosamente.')
    
    return redirect('usuario_admin')

@check_bloqueado
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

def soporte_view(request):
    if request.user.is_authenticated:
        return enviar_soporte(request)
    else:
        messages.info(request, 'Debes iniciar sesión para acceder al soporte.')
        return redirect('login')
    
def soporte_exito_view(request):
    return render(request, 'app/main/soporte_exito.html')

@check_bloqueado
@login_required
def agregar_al_carrito(request, polera_id):
    polera_obj = get_object_or_404(polera, id=polera_id)
    carrito_obj, created = carrito.objects.get_or_create(usuario=request.user.usuario)
    
    item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito_obj, polera=polera_obj)
    if not created:
        item_carrito.cantidad += 1
    item_carrito.save()

    return redirect('ver_carrito')


@check_bloqueado
@login_required
def realizar_compra(request):
    usuario_obj = request.user.usuario
    carrito_obj, created = carrito.objects.get_or_create(usuario=usuario_obj)
    items_carrito = carrito_obj.items.all()

    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            envio_obj = form.save(commit=False)
            envio_obj.usuario = usuario_obj
            envio_obj.fecha_envio = timezone.now()
            envio_obj.save()

            total = sum(item.precio_total for item in items_carrito)
            pedido = Pedido.objects.create(
                usuario=usuario_obj,
                total=total,
                fecha_compra=timezone.now(),
            )

            detalle_items = []
            for item in items_carrito:
                ItemPedido.objects.create(
                    pedido=pedido,
                    polera=item.polera,
                    cantidad=item.cantidad,
                    precio=item.precio_total
                )
                detalle_items.append(f'{item.cantidad} x {item.polera.nombre}')
                item.delete()

            carrito_obj.items.all().delete()

            Seguimiento.objects.create(
                pedido=pedido,
                estado='pendiente',
                comentario='Pedido realizado correctamente.',
                detalle='\n'.join(detalle_items)
            )

            response = render(request, 'app/acciones/compra_exito.html', {'pedido': pedido, 'envio': envio_obj})
            response.delete_cookie('carrito')
            return response
    else:
        form = EnvioForm()

    items = []
    total = 0
    for item in items_carrito:
        subtotal = item.precio_total
        total += subtotal
        items.append({
            'polera': item.polera,
            'cantidad': item.cantidad,
            'subtotal': subtotal
        })

    context = {
        'form': form,
        'items': items,
        'total': total,
    }
    return render(request, 'app/acciones/realizar_compra.html', context)



@check_bloqueado
@login_required
def ver_carrito(request):
    carrito_obj, created = carrito.objects.get_or_create(usuario=request.user.usuario)
    items = carrito_obj.items.all()

    context = {
        'items': items,
        'total': carrito_obj.total_precio,
    }
    return render(request, 'app/acciones/ver_carrito.html', context)

@check_bloqueado
@login_required
def mis_pedidos(request):
    usuario_obj = request.user.usuario
    pedidos = Pedido.objects.filter(usuario=usuario_obj).order_by('-fecha_compra') 

    context = {
        'pedidos': pedidos,
    }
    return render(request, 'app/acciones/mis_pedidos.html', context)

@check_bloqueado
@login_required
def ver_perfil(request):
    usuario_obj = request.user.usuario

    if request.method == 'POST':
        form = ActualizarPerfilForm(request.POST, instance=usuario_obj)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil')
    else:
        form = ActualizarPerfilForm(instance=usuario_obj)

    context = {
        'form': form,
        'usuario': usuario_obj,
    }
    return render(request, 'app/main/ver_perfil.html', context)

@check_bloqueado
@login_required
def ver_pedidos_admin(request):
    if not request.user.is_superuser:
        return redirect('Inicio')

    pedidos = Pedido.objects.all().order_by('-fecha_compra')

    context = {
        'pedidos': pedidos,
    }
    return render(request, 'app/admin/ver_pedidos_admin.html', context)


@check_bloqueado
@login_required
def detalle_pedido_admin(request, pedido_id):
    if not request.user.is_superuser:
        return redirect('Inicio')

    pedido = get_object_or_404(Pedido, id=pedido_id)
    items = pedido.items.all()

    context = {
        'pedido': pedido,
        'items': items,
    }
    return render(request, 'app/admin/detalle_pedido_admin.html', context)

@check_bloqueado
@login_required
def mis_seguimientos(request):
    usuario_obj = request.user.usuario
    seguimientos = Seguimiento.objects.filter(pedido__usuario=usuario_obj).order_by('-fecha_actualizacion')

    context = {
        'seguimientos': seguimientos,
    }
    return render(request, 'app/acciones/mis_seguimientos.html', context)

@check_bloqueado
@login_required
def detalle_seguimiento(request, seguimiento_id):
    seguimiento = get_object_or_404(Seguimiento, id=seguimiento_id)
    pedido_usuario_rut = seguimiento.pedido.usuario.rut.strip() if seguimiento.pedido.usuario.rut else ''
    user_rut = request.user.usuario.rut.strip() if request.user.usuario.rut else ''
    
    print(f"pedido_usuario_rut: '{pedido_usuario_rut}'")
    print(f"user_rut: '{user_rut}'")
    print(f"request.user.is_staff: {request.user.is_staff}")
    
    if pedido_usuario_rut != user_rut and not request.user.is_staff:
        print("PermissionDenied triggered")
        raise PermissionDenied

    context = {
        'seguimiento': seguimiento,
    }
    return render(request, 'app/acciones/detalle_seguimiento.html', context)

@check_bloqueado
@staff_member_required
def seguimiento_admin(request):
    seguimientos = Seguimiento.objects.all()
    return render(request, 'app/admin/seguimiento_admin.html', {'seguimientos': seguimientos})

@check_bloqueado
@staff_member_required
def detalle_seguimiento_admin(request, seguimiento_id):
    seguimiento = get_object_or_404(Seguimiento, pk=seguimiento_id)
    if request.method == 'POST':
        form = SeguimientoForm(request.POST, instance=seguimiento)
        if form.is_valid():
            form.save()
            return redirect(reverse('seguimiento_admin'))
    else:
        form = SeguimientoForm(instance=seguimiento)
    return render(request, 'app/admin/detalle_seguimiento_admin.html', {'form': form, 'seguimiento': seguimiento})


from django.urls import path, include
from .views import inicio, udechile,enviar_soporte, soporte_exito_view ,ucatolica, colocolo, huachipato, soporte_view, pago, registro, CustomLoginView, logout_view, equipoadmin, home, usuarioadmin, polera_admin, editar_polera, eliminar_polera, equipo_admin, editar_equipo, eliminar_equipo, usuario_admin, editar_usuario, eliminar_usuario, registrar_usuario, realizar_compra
from .views import agregar_al_carrito, ver_carrito, mis_pedidos, ver_perfil, ver_pedidos_admin, detalle_pedido_admin, gestionar_soporte, detalle_soporte_admin, cambio
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns = [
    
    path('', inicio, name="Inicio"),
    path('udechile', udechile, name="udechile"),
    path('ucatolica', ucatolica, name="ucatolica"),
    path('colocolo', colocolo, name="colocolo"),
    path('huachipato', huachipato, name="huachipato"),
    path('soporte/', soporte_view, name="soporte"),
    path('enviar_soporte/', enviar_soporte, name='enviar_soporte'),
    path('soporte/exito/', soporte_exito_view, name='soporte_exito_view'),
    path('pago', pago, name="pago"),
    path('registro/', registro, name='registro'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('equipoadmin', equipoadmin, name="equipoadmin"),
    path('home', home, name="home"),
    path('usuarioadmin', usuarioadmin, name="usuarioadmin"),
    path('polerasadm/', polera_admin, name='polera_admin'),
    path('polerasadm/editar/<int:pk>/', editar_polera, name='editar_polera'),
    path('polerasadm/editar/', editar_polera, name='editar_polera'), 
    path('polerasadm/eliminar/<int:pk>/', eliminar_polera, name='eliminar_polera'),
    path('equipos/', equipo_admin, name='equipo_admin'),
    path('equipos/editar/<int:pk>/', editar_equipo, name='editar_equipo'),
    path('equipos/editar/', editar_equipo, name='editar_equipo'), 
    path('equipos/eliminar/<int:pk>/', eliminar_equipo, name='eliminar_equipo'),
    path('usuarios/', usuario_admin, name='usuario_admin'),
    path('usuarios/editar/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('usuarios/registrar/', registrar_usuario, name='registrar_usuario'),
    path('usuarios/eliminar/<int:pk>/', eliminar_usuario, name='eliminar_usuario'),
    path('compra-exitosa/', TemplateView.as_view(template_name='app/acciones/compra_exito.html'), name='compra_exitosa'),##
    path('agregar-al-carrito/<int:polera_id>/', agregar_al_carrito, name='agregar_al_carrito'),##
    path('carrito/', ver_carrito, name='ver_carrito'), ##
    path('realizar-compra/', realizar_compra, name='realizar_compra'), 
    path('mis_pedidos/', mis_pedidos, name='mis_pedidos'),
    path('ver_perfil/', ver_perfil, name='ver_perfil'),
    path('poto/', ver_pedidos_admin, name='ver_pedidos_admin'),
    path('poto/<int:pedido_id>/', detalle_pedido_admin, name='detalle_pedido_admin'),
    path('sexo/', gestionar_soporte, name='gestionar_soporte'),
    path('sexo/<int:mensaje_id>/', detalle_soporte_admin, name='detalle_soporte_admin'),
    path('cambio/', cambio, name='cambio'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
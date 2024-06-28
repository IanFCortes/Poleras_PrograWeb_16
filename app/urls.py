from django.urls import path, include
from .views import inicio, udechile,enviar_soporte, soporte_exito_view ,ucatolica, colocolo, huachipato, soporte, pago, registro, CustomLoginView, logout_view, equipoadmin, home, soporteadmin, usuarioadmin, polera_admin, editar_polera, eliminar_polera, equipo_admin, editar_equipo, eliminar_equipo, usuario_admin, editar_usuario, eliminar_usuario, registrar_usuario
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', inicio, name="Inicio"),
    path('udechile', udechile, name="udechile"),
    path('ucatolica', ucatolica, name="ucatolica"),
    path('colocolo', colocolo, name="colocolo"),
    path('huachipato', huachipato, name="huachipato"),
    path('soporte/', soporte, name="soporte"),
    path('enviar_soporte/', enviar_soporte, name='enviar_soporte'),
    path('soporte/exito/', soporte_exito_view, name='soporte_exito_view'),
    path('pago', pago, name="pago"),
    path('registro/', registro, name='registro'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('equipoadmin', equipoadmin, name="equipoadmin"),
    path('home', home, name="home"),
    path('soporteadmin', soporteadmin, name="soporteadmin"),
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
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
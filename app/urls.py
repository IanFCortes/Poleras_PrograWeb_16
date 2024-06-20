from django.urls import path, include
from .views import inicio, udechile, ucatolica, colocolo, huachipato, soporte, pago, registro
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('', inicio, name="Inicio"),
    path('udechile', udechile, name="udechile"),
    path('ucatolica', ucatolica, name="ucatolica"),
    path('colocolo', colocolo, name="colocolo"),
    path('huachipato', huachipato, name="huachipato"),
    path('soporte', soporte, name="soporte"),
    path('pago', pago, name="pago"),
    path('registro/', registro, name='registro'),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_rut = settings.MEDIA_ROOT)
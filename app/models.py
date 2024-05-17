from django.db import models
from django.contrib.auth.models import User

class equipo (models.Model):
    nombre = models.CharField(max_length=50)
   # logo = models.ImageField() Hasta instalar pillows

class polera (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    talla = models.CharField(max_length=3)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE)
   # logo = models.ImageField() Hasta instalar pillows
    
class usuario(User):
    rut = (models.CharField)
    region = (models.CharField)

class carrito(models.Model):
    item = models.ForeignKey(polera,  on_delete=models.CASCADE)
    total = models.IntegerField()
    usuario = models.ForeignKey(usuario,  on_delete=models.CASCADE)
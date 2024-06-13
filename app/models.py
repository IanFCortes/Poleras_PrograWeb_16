from django.db import models
from django.contrib.auth.models import User

class equipo (models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='media/', null=True)

class polera (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    talla = models.CharField(max_length=3)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='media/', null=True)
    
class usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rut = models.CharField (max_length=10, blank=True, null=True)
    region = models.CharField (max_length=30, blank=True, null=True)

    def __str__(self):
        return self.rut
        
class carrito(models.Model):
    item = models.ForeignKey(polera,  on_delete=models.CASCADE)
    total = models.IntegerField()
    usuario = models.ForeignKey(usuario,  on_delete=models.CASCADE)

class soporte(models.Model):
    usuario = models.ForeignKey(usuario, verbose_name=("Usuario"), on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=500)
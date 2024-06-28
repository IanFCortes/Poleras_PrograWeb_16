from django.db import models
from django.contrib.auth.models import User

class equipo (models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='equipos/', null=True)

    def __str__(self):
        return self.nombre

    

class polera (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    talla = models.CharField(max_length=3)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/', null=True)

    def __str__(self):
        return self.nombre
    
class usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rut = models.CharField (max_length=10, blank=True, null=True)
    direccion = models.CharField (max_length=30, blank=True, null=True)
    numero_celular = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.rut
        
class carrito(models.Model):
    total = models.IntegerField()
    usuario = models.ForeignKey(usuario,  on_delete=models.CASCADE)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE)
    polera = models.ForeignKey(polera, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    subtotal = models.IntegerField()

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.polera.precio
        super().save(*args, **kwargs)

class soporte(models.Model):
    usuario = models.ForeignKey(usuario, verbose_name=("Usuario"), on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.titulo} - {self.usuario}'

class envio(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    pais = models.CharField(max_length=50)
    fecha_envio = models.DateField()
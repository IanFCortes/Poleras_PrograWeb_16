from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class equipo(models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='equipos/', null=True)

    def __str__(self):
        return self.nombre

class polera(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    talla = models.CharField(max_length=3)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/', null=True)

    def __str__(self):
        return self.nombre

class usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rut = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=30, blank=True, null=True)
    numero_celular = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    bloqueado = models.BooleanField(default=False)
    fecha_bloqueo = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.rut

    def bloquear(self):
        self.bloqueado = True
        self.fecha_bloqueo = timezone.now()
        self.save()

    def desbloquear(self):
        self.bloqueado = False
        self.fecha_bloqueo = None
        self.save()

class carrito(models.Model):
    usuario = models.OneToOneField(usuario, on_delete=models.CASCADE, related_name='carrito')

    def __str__(self):
        return f'Carrito de {self.usuario.user.username}'

    @property
    def total_precio(self):
        return sum(item.precio_total for item in self.items.all())
    
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE, related_name='items')
    polera = models.ForeignKey(polera, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    @property
    def precio_total(self):
        return self.polera.precio * self.cantidad

    def __str__(self):
        return f'{self.cantidad} x {self.polera.nombre}'

class Pedido(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='pedidos')
    fecha_compra = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.user.username}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    polera = models.ForeignKey(polera, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.polera.nombre}'
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
    pais = models.CharField(max_length=50, null=True, blank=True)
    fecha_envio = models.DateField()

class Compra(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    total = models.IntegerField()
    fecha_compra = models.DateTimeField()
    envio = models.ForeignKey(envio, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'Compra {self.id} - {self.usuario}'

class CompraItem(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='items')
    item_carrito = models.ForeignKey(ItemCarrito, on_delete=models.CASCADE)

    def __str__(self):
        return f'Item de Compra {self.compra.id}: {self.item_carrito}'
    

class Seguimiento(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en proceso', 'En Proceso'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado')
    )

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='seguimientos')
    estado = models.CharField(max_length=50, default='Pendiente', choices=ESTADO_CHOICES)
    creado = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    comentario = models.TextField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'Seguimiento de {self.pedido.id} - {self.estado}'
from django.contrib import admin
from .models import polera, equipo, usuario, carrito, soporte, Compra, ItemCarrito,CompraItem, Pedido, ItemPedido
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class PoleraAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "talla", "equipo", "logo")

    class Meta:
        model = polera
        
class EquipoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "logo")

    class Meta:
        model = equipo
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "fecha_compra", "total")

    class Meta:
        model = Pedido

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "polera", "cantidad", "precio")

    class Meta:
        model = ItemPedido

class CompraItemAdmin(admin.ModelAdmin):
    list_display = ("compra", "item_carrito")

    class Meta:
        model = CompraItem

class PerfilUsuario(admin.StackedInline):
    model = usuario
    can_delete = False
    verbose_name_plural = 'Perfil de Usuario'

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (PerfilUsuario, )


class CarritoAdmin(admin.ModelAdmin):
    list_display = ("item", "total", "usuario")

    class Meta:
        model = carrito

@admin.register(soporte)
class SoporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'titulo', 'mensaje')
    list_filter = ('usuario', 'titulo')
    search_fields = ('titulo', 'mensaje')

    class Meta:
        model = soporte
    
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "items", "total", "fecha_compra")

    class Meta:
        model = Compra

admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)
admin.site.register(polera)
admin.site.register(ItemPedido)
admin.site.register(Pedido)
admin.site.register(equipo )
admin.site.register(carrito)
admin.site.register(CompraItem)
admin.site.register(Compra)
admin.site.register(ItemCarrito)



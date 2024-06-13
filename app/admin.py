from django.contrib import admin
from .models import polera, equipo, usuario, carrito, soporte
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

class SoporteAdmin(admin.ModelAdmin):
    list_display = ("usuario", "titulo", "mensaje")

    class Meta:
        model = soporte

admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)
admin.site.register(polera)
admin.site.register(equipo )
admin.site.register(carrito)
admin.site.register(soporte )



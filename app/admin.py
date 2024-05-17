from django.contrib import admin
from .models import polera

class PoleraAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "talla", "equipo")

    class Meta:
        model = polera

admin.site.register(polera, PoleraAdmin)

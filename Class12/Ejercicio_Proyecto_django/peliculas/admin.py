from django.contrib import admin

# Register your models here.
from .models import Directores, InstanciaPeliculas, Peliculas

admin.site.register(Directores)
admin.site.register(Peliculas)
admin.site.register(InstanciaPeliculas)
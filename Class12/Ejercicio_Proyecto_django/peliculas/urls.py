from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home),
    path('directores/', view=views.directores),
    path('peliculas/', view=views.peliculas),
    path('directores/<int:directorid>', view=views.biografiadirectore),
    path('peliculas/<int:peliculaid>', view=views.detallepelicula),
]

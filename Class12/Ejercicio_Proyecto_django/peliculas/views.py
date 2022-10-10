from typing import List
from django.http import HttpResponse, JsonResponse
from .models import InstanciaPeliculas, Peliculas, Directores
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'index.html')


def directores(request):
    directores = list(Directores.objects.all())
    return render(request, 'directores.html', {'directores': directores})


def peliculas(request):
    peliculas = list(Peliculas.objects.values())
    return JsonResponse(peliculas, safe=False)


def detallepelicula(request, peliculaid):
    pelicula = get_object_or_404(Peliculas, id=peliculaid)
    name = pelicula.name
    sinopsis = pelicula.descripcion
    dir = pelicula.directores
    # director = List(Directores.objects.get(id=pelicula.directores))
    # print(director)
    return render(
        request, 'pelicula.html', {
            'name': name,
            'sinopsis': sinopsis,
            'director': dir.name + " " + dir.lastName
        })


def biografiadirectore(request, directorid):
    # director = List(Directores.objects.get(id=directorid))
    director = get_object_or_404(Directores, id=directorid)
    name = director.name + " " + director.lastName + " (" + str(
        director.age) + ")"
    bio = director.bio
    return render(request, 'biografia.html', {'name': name, 'bio': bio})

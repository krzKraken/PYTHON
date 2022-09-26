from django.db import models
import uuid


class Directores(models.Model):

    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + self.lastName


class Peliculas(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.TextField(help_text="Resumen del libro", default="")
    directores = models.ForeignKey('Directores',
                                   on_delete=models.SET_NULL,
                                   null=True)

    def __str__(self):
        return self.name


class InstanciaPeliculas(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text="Id unico para esta pelicula")
    pelicula = models.ForeignKey('Peliculas',
                                 on_delete=models.SET_NULL,
                                 null=True)
    fechaEstreno = models.DateField(null=True, blank=True)
    GENEROS_DISPONIBLES = (
        ('t', 'Terror'),
        ('c', 'Comedia'),
        ('p', 'Parodia'),
        ('a', 'Accion'),
        ('s', 'Suspenso'),
        ('d', 'Drama'),
        ('cf', 'Ciencia-Ficcion'),
        ('cr', 'Comedia-Romantica'),
    )
    genero = models.CharField(max_length=2,
                              choices=GENEROS_DISPONIBLES,
                              blank=True,
                              default='t',
                              help_text="Ingresa el genero")

    def __str__(self):
        return str(self.pelicula)

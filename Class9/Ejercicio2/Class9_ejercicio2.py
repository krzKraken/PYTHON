# Eneste segundo ejercicio, tenemos que crear una aplicacion que obtenga los elementos impares de una lista pasando porparametro con filter y realizara una suma de tosos los elementos obtenidos mediante un reduce

from functools import reduce

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def filtro(x):
    if x % 2 != 0:
        return True
    else:
        return False


listaResultado = filter(filtro, listaNumeros)
lista = list(listaResultado)
print(lista)

sumaLista = reduce(lambda a, b: a+b, lista)
print(sumaLista)

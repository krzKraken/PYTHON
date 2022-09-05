#map, filter, reduce
# Filter -> Corre una funcion en toda una lista, si la condicion se cumple, regresa el valor de la lista, caso contrario no
from functools import reduce


num = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12]
nombres = ["pepe", "pepito", "carlos"]


def miFuncion(x):
    if x % 2 == 0:
        return True
    else:
        return False


def buscarNombre(nombre):
    if str(nombre).startswith("pep"):
        return True
    else:
        return False


def funcionAnonima(x): return x % 2 != 0


res = filter(miFuncion, num)
print(list(res))
res = filter(funcionAnonima, num)
print(list(res))

res = filter(buscarNombre, nombres)
print(list(res))

res = filter(lambda x: str(x).startswith("pep"), nombres)
print(list(res))


# Aplica una funcion en toda una lista o tupla (interables) indiscriminadamente sobre todos los elementos sin condiciones
# resultado = map(Funcion, Lista)

def cuadrado(x):
    return x*x


resultado = map(cuadrado, [1, 2, 3, 4, 5, 6])
print(list(resultado))

resultado = map(lambda x: x*x, [1, 2, 3, 4, 5, 6])
print(list(resultado))


# Reduce
# Aplica una funcion en toda una lista, hasta que la lista se reduzca a cero
# reduce(funcion, lista)


def suma(a, b):
    return a+b


res = reduce(suma, [1, 2, 3, 4])
print(res)

res = reduce(lambda a, b: a+b, [1, 2, 3, 4])
print(res)

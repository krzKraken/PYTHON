# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math
import sys
import string

alf = (string.ascii_letters + string.punctuation).replace(".", "")


def areaTriangulo(base, altura):
    resultado = base * altura / 2
    return resultado


def areaCirculo(radio):
    resultado = math.pi * math.pow(float(radio), 2)
    return resultado


def esFlotante(num):
    digitos = list(num)
    for i in digitos:
        if i in alf:
            sys.exit("Valor invalido, Terminando programa")

    if float(num):
        return True


base = input("Ingrese la base: ")
if (esFlotante(base)):
    altura = input("ingrese la altura: ")
    if (esFlotante(altura)):
        areaT = round(areaTriangulo(base=float(base), altura=float(altura)), 2)
    else:
        sys.exit("Valor no valido, terminando programa")
else:
    sys.exit("Valor no valido, terminando programa")

print(
    f"El area de un triangulo de lado: {base} y altura: {altura}, es: {areaT}")

radio = input("Ingrese el radio del circulo: ")
if esFlotante(radio):
    areaC = round(areaCirculo(radio=radio), 2)
    print(f"El area del circulo con radio : {radio} es: {areaC}")

# input -> ingreso de datos

from getpass import getpass

a = input("usuario: ")
b = getpass("password: ")
print(a, b)


# Convertir digito a String
secreto = 50

valor = input("Introduce un numero: ")
valor = int(valor)  # -> Convierte en entero

# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

from msilib import PID_REVNUMBER


def validarEdad(edad):
    try:
        int(edad)
        return True
    except:
        return False


edad = input("Ingrese su edad: ")
if (validarEdad(edad) and int(edad) > 18):
    print("Es mayor de edad")
elif (validarEdad(edad) and 0 <= int(edad) < 18):
    print("Es menor de edad")
else:
    print("edad invalida")

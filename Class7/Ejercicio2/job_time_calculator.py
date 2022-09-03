from decimal import Rounded
import time as t
from math import pow as pow

horaSalida = "19:00:00"  # 07:00:00 Horas


def queHoraEs():
    """
    Retorna Hora Actual en formato HH:MM:SS
    """
    return t.strftime("%H:%M:%S", t.localtime())


def convSecHora(horaInt):
    """
    Convierte la hora en segundos a formato HH:MM:SS
    """
    hora = int(horaInt/(60*60))
    minutos = int((horaInt/(60*60)-hora)*60)
    segundos = int(round((((horaInt/(60*60)-hora)*60)-minutos)*60, 0))
    return f"{hora}:{minutos}:{segundos}"


def compararHoras(horaActual, horaSalida):
    """
    Compara si HoraActual es mayor que HoraSalida y retorna si es hora de ir a casa o que tiempo falta para salir
    """
    horActInt = 0
    horSalInt = 0
    for i in range(0, 3):
        horActInt += int(horaActual.split(":")[i]) * pow(60, 2-i)
        horSalInt += int(horaSalida.split(":")[i]) * pow(60, 2-i)
    if horActInt > horSalInt:
        return 'Es hora de ir a casa...!!!'
    else:
        return f"Faltan {convSecHora(horSalInt - horActInt)} horas para salir"
    diferenciaHora = ""


horaActual = queHoraEs()
print(f"Hora Actual:  {horaActual} horas")
print(f"Hora de salida: {horaSalida} horas")
print(compararHoras(horaActual=horaActual, horaSalida=horaSalida))

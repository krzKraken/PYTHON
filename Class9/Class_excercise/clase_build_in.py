# funciones Built-in => https://docs.python.org/3/library/index.html

# Paradigma de programacion multi hilo

import _thread
import time


def horaActual(nombre_thread, tiempo_espera):
    cont = 0
    while cont < 5:
        time.sleep(tiempo_espera)
        mensaje = f'{nombre_thread} -{time.ctime(time.time())}'
        print(mensaje)
        cont += 1


_thread.start_new_thread(horaActual, ("Hijo_1", 1))
_thread.start_new_thread(horaActual, ("Hijo_2", 2))
print("He disparado los hijos")


while True:
    time.sleep(0.1)

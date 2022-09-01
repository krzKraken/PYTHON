# Ejercicio Clase Vehiculo

class Vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 5


class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 2.0


coche = Coche()
print(f"El coche es de color: {coche.color}")
print(f"El coche tiene {coche.ruedas} ruedas")
print(f"El coche tiene {coche.puertas} puertas")
print(f"la velocidad del coche es {coche.velocidad} km/h")
print(f"la cilidrada del coche es de {coche.cilindrada} litros")

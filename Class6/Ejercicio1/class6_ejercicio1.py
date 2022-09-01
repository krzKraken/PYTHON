# Ejercicio Clase Vehiculo
class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


miCoche = Coche(color="rojo", ruedas=4, puertas=4,
                velocidad=100, cilindrada=2000)

print(f"El coche de color {miCoche.color}")
print(f"Tiene {miCoche.color} ruedas")
print(f"El coche tiene {miCoche.color} puertas")
print(f"Alcanza una velocidad de {miCoche.color} km/h")
print(f"Tiene una cilindrada de {miCoche.color} cc")

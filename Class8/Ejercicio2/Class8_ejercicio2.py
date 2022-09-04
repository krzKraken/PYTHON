# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
class Vehiculo:
    color = ''
    puertas = 0
    velocidad = 0
    cilindrada = 0

    def __init__(self, puertas, velocidad, color, cilindrada):
        self.puertas = puertas
        self.velocidad = velocidad
        self.color = color
        self.cilindrada = cilindrada

    def imprimeVehiculo(self):
        detalle = f'''El Vehiculo Tiene las siguientes propiedades:
Color: {self.color}
Puertas: {self.puertas}
velocidad: {self.velocidad}
cilindrada: {self.cilindrada}'''

        return detalle


def guardarFichero(txt):
    print("Fichero guardado.... con nombre: fichero.txt")
    f = open("fichero.txt", 'w')
    f.writelines(txt)
    f.close()


def leerFichero():
    print("Leyendo fichero.txt....")
    f = open("fichero.txt", 'r')
    dato = f.read()
    f.close()
    return dato


def main():
    miVehiculo = Vehiculo(color='rojo', puertas=5,
                          velocidad=100, cilindrada=2000)
    guardarFichero(miVehiculo.imprimeVehiculo())
    datos = leerFichero()
    print(datos)


if __name__ == "__main__":
    main()

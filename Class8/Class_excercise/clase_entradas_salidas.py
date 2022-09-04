# La forma antigua
from cgitb import text
from re import U
from typing import overload


numero = 123
texto = "hola"
esAlgo = True
flotante = 1.2

# LA FORMA ANTIGUA ( LA FEA)
# El %.2f indica el numero de decimales
print("El numero es %d, y el texto es %s y el flotante es %.2f" %
      (numero, texto, flotante))
print("El numero es %d" % numero)


# LA FUNCION FORMAT
print("El numero es {} y el texto es {} y tiene {}"
      .format(numero, texto, esAlgo)
      )
print("El numero es {2} y el texto es {1} y tiene {0}"
      .format(numero, texto, esAlgo)
      )
print("El numero es {num} y el texto es {text} y tiene {esalgo}"
      .format(num=numero, text=texto, esalgo=esAlgo)
      )

# f"String"
print(f"El numero es {numero} y el texto es {texto} y el algo es {esAlgo}")


# STR Y REPR
# str() --> Salidas informales TODOS LOS OBJETOS LA TIENEN
# repr() --> Salidas de desarrollo o depuracion

class usuario:
    nombre = "Manolo"
    edad = 10

    def imprimirNombre(self, nombre, edad):  # Funcion de clase
        return f'Funcion Formal de impresion: Mi nombre es {self.nombre} y mi edad es {self.edad}'

    def __str__(self) -> str:  # Salida informal
        return f'Impresion informal con __STR___ -> Mi nombre es {self.nombre}'

    def __repr__(self) -> str:  # Salida de depuracion
        return f'Salida de depuracion con __REPR__ ->( Usuario -> {self.nombre} - {self.edad})'


u = usuario()
print(u.imprimirNombre("Cristhian", 100))
print(str(u))
print(repr(u))


# Manipulacion de strings
# print(dir(''))

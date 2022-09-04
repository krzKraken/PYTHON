# File handle
from pprint import pprint


f = open('D:/DEV/PYTHON/Class8/Class_excercise/Factura.xml', 'r')
datos = f.read()
f.close()
# ---- Modos ----
# r: lectura -> Solo lectura, no se puede escribir
# a: append -> Escribe en el fichero pero al final agrega
# w: escritura -> Borra el fichero y lo vuelve a escribir desde cero
# x: create -> Crea el fichero si no existe

# t: texto -> si es texto plano t ejemplo open('etc/password' , rt)
# b: binario  -> Si es binario -> b open('etc/password' , rb)

# + -> Ejemplo => open('archivo.txt', 'wt+') -> lectura y escritura texto plano w+ lectura y escritura

# Leer todo el archivo
# pprint(datos)

# leer por Linea 1ra Forma
datos = ''
f = open('D:/DEV/PYTHON/Class8/Class_excercise/Factura.xml', 'r')
while datos != "":
    datos = f.readline()
    # print(datos)
f.close()

# Leer por Linea 2da Forma
datos = 'a'
f = open('D:/DEV/PYTHON/Class8/Class_excercise/Factura.xml', 'r')
while len(datos) > 0:
    datos = f.readline()
    # print(datos)
f.close()


# leer ficheros mas util
datos = ''
f = open('D:/DEV/PYTHON/Class8/Class_excercise/Factura.xml', 'r')
datos = f.readlines()
f.close()
print(datos)

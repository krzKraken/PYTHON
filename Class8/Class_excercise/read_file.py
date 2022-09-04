nombre_comercial = ''
ruc = ''
numero_autorizacio = ''
numero_factura = ''
fecha = ''
subtotal_12 = ''
subtotal_0 = ''
subtotal_sin_impuestos = ''
iva_12 = ''
valor_total = ''


def main():
    datosUsuario = obtenerDatos()
    # print(datosUsuario)


def obtenerDatos():
    f = open('Class8/Class_excercise/Factura.xml', 'r')
    datos = f.readlines()
    f.close()
    return datos


def obtenerNombreComercial():
    datos = obtenerDatos()


if __name__ == '__main__':
    main()

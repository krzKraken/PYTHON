
def mensajeError():
    print("Error de datos... terminando Programa")


def validarValor(valor):
    try:
        float(valor)
        return True
    except:
        return False


print("Ingrese su peso en Kilogramos [Kg]: ")
peso = input()
if (float(peso) > 0 and validarValor(peso)):
    print("ingrese su altura en metros [m]: ")
    altura = input()
    if (float(altura) > 0 and validarValor(altura)):
        imc = float(peso) / (float(altura)**2)
        imcRedondeado = imc.__round__(2)
        print("IMC: " + str(imcRedondeado))

    else:
        mensajeError()
else:
    mensajeError()

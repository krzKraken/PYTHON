def mensajeError():
    print("Error de datos... terminando Programa")


print("Ingrese su peso en Kilogramos [Kg]: ")
peso = input()
if (peso.isnumeric() and int(peso) > 0):
    print("ingrese su altura en metros [cm]: ")
    altura = input()
    if (altura.isnumeric() and int(altura) > 0):
        print("Altura: " + altura + " , Peso: " + peso)
    else:
        mensajeError()
else:
    mensajeError()

imc = float(peso) / ((float(altura)/100)**2)
imcRedondeado = imc.__round__(2)
print(imcRedondeado)

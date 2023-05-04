# hacer un programa que le pida al usuario dos numero s
# que correspondan al dividenedo y el dividor
# debe mostrar la division. El programa debe mostrar un
# error en la divison por cero

dividendo = float(input("Ingresa el dividendo"))
divisor = float(input("Ingrese el divisor"))

if divisor == 0:
    print("No se puede dividir entre 0")
else:
    print("El resultado de la division es: ", round(dividendo/divisor, 2))
print("FIN DEL PROGRAMA")

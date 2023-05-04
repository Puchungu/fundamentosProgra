# Integrantes
# Nelson Oswaldo Alvarenga Cuadra
# Oscar Rene Palacios Franco
# Rodrigo Manuel Perla Amaya
# Salvador Alas Hernandez


# Solicitar al usuario que ingrese cuatro números y mostrar cuál es menor y que lo
# muestre únicamente si no hay números repetidos


num1 = int(input("Ingrese el numero"))
num2 = int(input("Ingrese el numero"))
num3 = int(input("Ingrese el numero"))
num4 = int(input("Ingrese el numero"))


if num1 < num2 and num1 < num3 and num1 < num4:
    print("El numero menor es: ", num1)

elif num2 < num1 and num2 < num3 and num2 < num4:
    print("El numero menor es: ", num2)

elif num3 < num1 and num3 < num2 and num3 < num4:
    print("El numero menor es: ", num3)

elif num4 < num1 and num4 < num2 and num4 < num3:
    print("El numero menor es: ", num4)
else:
    print("Los numeros son iguales")

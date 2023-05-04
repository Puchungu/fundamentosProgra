# Integrantes
# Nelson Oswaldo Alvarenga Cuadra
# Oscar Rene Palacios Franco
# Rodrigo Manuel Perla Amaya
# Salvador Alas Hernandez

# Solicitar al usuario que ingrese cuatro números y mostrar cuál es mayor.

num1 = int(input("Ingrese el numero"))
num2 = int(input("Ingrese el numero"))
num3 = int(input("Ingrese el numero"))
num4 = int(input("Ingrese el numero"))

if num1 > num2 and num1 > num3 and num1 > num4:
    print("El numero mayor es: ", num1)

if num2 > num1 and num2 > num3 and num2 > num4:
    print("El numero mayor es: ", num2)

if num3 > num1 and num3 > num2 and num3 > num4:
    print("El numero mayor es: ", num3)

if num4 > num1 and num4 > num2 and num4 > num3:
    print("El numero mayor es: ", num4)

# Integrantes
# Nelson Oswaldo Alvarenga Cuadra
# Oscar Rene Palacios Franco
# Rodrigo Manuel Perla Amaya
# Salvador Alas Hernandez


# Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje
# “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de
# más de un carácter, informarle que no se puede procesar el dato


letra = input("Ingrese la letra:")
if len(letra) != 1:
    print("Debe ser sólo una letra")
elif letra in "aeiou":
    print("Es vocal")

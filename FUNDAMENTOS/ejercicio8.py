# Integrantes
# Nelson Oswaldo Alvarenga Cuadra
# Oscar Rene Palacios Franco
# Rodrigo Manuel Perla Amaya
# Salvador Alas Hernandez

# Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en
# dos variables. A continuación, imprimir “coincidencia” si los nombres de ambas personas
# comienzan con la misma letra y si terminan con la misma letra. Si no es así, imprimir “no
# hay coincidencia


nom1 = input("Ingrese el primer nombre ")
nom2 = input("Ingrese el segundo nombre ")


# Encontrando la longitud del nombre para determinar la ultima letra
final_nom1 = len(nom1)-1
final_nom2 = len(nom2)-1


if nom1[0] == nom2[0]:
    if nom1[final_nom1] == nom2[final_nom2]:
        print("Coincidencia")
else:
    print("No hay coincidencia")

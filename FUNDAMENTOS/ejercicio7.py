# Integrantes
# Nelson Oswaldo Alvarenga Cuadra
# Oscar Rene Palacios Franco
# Rodrigo Manuel Perla Amaya
# Salvador Alas Hernandez

# Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto
# debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible
# por 40


año = int(input("Ingrese el año:"))
if año % 4 == 0:
    if año % 100 != 0 or año % 40 == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
else:
    print("El año no es bisiesto")

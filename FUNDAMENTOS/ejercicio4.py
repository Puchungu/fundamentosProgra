# Integrantes
# Nelson Oswaldo Alvarenga Cuadra
# Oscar Rene Palacios Franco
# Rodrigo Manuel Perla Amaya
# Salvador Alas Hernandez


# Si la temperatura ambiente está entre 10 y 20 grados Celsius que diga “Nivel azul”
# De lo contrario diga “Nivel verde”, pero si la temperatura es menor a 30 grados
# que diga “Nivel naranja” de lo contrario “Nivel rojo”

temperatura = float(input("Ingrese la temperatura actual "))

if temperatura > 10:
    if temperatura < 20:
        print("Nivel Azul")
    else:
        print("Nivel verde")
else:
    if temperatura < 30:
        print("Nivel Naranja")
    else:
        print("Nivel rojo")

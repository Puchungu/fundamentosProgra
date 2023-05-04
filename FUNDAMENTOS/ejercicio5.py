# Integrantes
# Nelson Oswaldo Alvarenga Cuadra
# Oscar Rene Palacios Franco
# Rodrigo Manuel Perla Amaya
# Salvador Alas Hernandez


# Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes,
# otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el
# día ingresado no es ninguno de esos, imprimir otro mensaje.


dia = input("Ingrese el dia ".lower())

if dia == "lunes":
    print("Inicio de la semana")
elif dia == "viernes":
    print("Fin de semana ve por unas birrias y alitas te lo mereces")
elif dia == "sabado":
    print("Finde sale playuki?")
elif dia == "domingo":
    print("Dia de ir a la casita de DEUS")
else:
    print("Un dia mas es un dia menos")

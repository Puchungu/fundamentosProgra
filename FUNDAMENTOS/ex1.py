# realizar la siguiente operacion
# usar round() para mostrar los decimales deseados

# a = (19/155)*(155/19)
# round(variables,numeros_decimales)
# entero o redondear
# print(round(a))
# 1 decimal
# print(round(a, 2))


# Calcular las notas del computo
lab1 = int(input("Ingresa la nota del primer lab"))  # 30%
lab2 = int(input("Ingresa la nota del segundo lab"))  # 30%
parc = int(input("Ingresa la nota del parcial"))   # 40%
# procesos
# lab1 *= 0.30
# lab2 *= 0.30
# parc *= 0.40
# notafinal = lab1+lab2+parc
# print(notafinal)
Notafinal = ((lab1 + lab2) / 2)*0.60 + (parc*0.40)
print("Tu promedio es: ", Notafinal)

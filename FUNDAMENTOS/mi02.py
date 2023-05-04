# Escribir un programa que guarde una contrasena en una variable
# y que solicite al usuario el ingreso de una contrasena y si esta
# coinciden le de acceso

password = "ugb2023"
paswus = input("Ingresa tu contrasena")

if paswus.lower() == password:
    print("Tu contrasena coincide, tienes acceso al sistema")

else:
    print("Error en la contrasena")
print("Fin de programa")

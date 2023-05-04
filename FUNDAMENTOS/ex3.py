# ingresar datos desde el teclado
name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
print("Su nombre es: ", name, " y su edad es: ", age)

if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

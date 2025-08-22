nombre = input("Digite su nombre:")
#Para que no hayan espacios
no_espacio = nombre.replace(" ", "")
#Mayuscula
print(nombre.upper())
#Minuscula
print(nombre.lower())
#Primera letra y ultima letra
print(nombre [0] + nombre [-1])
#Caracteres en total
print(no_espacio.__len__())
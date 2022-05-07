#Saber el número de mayúsculas en una string

texto = input("Introduzca el texto: ")
numero_mayusculas = 0
for i in texto:
    if i.isupper():
        numero_mayusculas += 1
print("\nEl número de máyusculas es: {}".format(numero_mayusculas))
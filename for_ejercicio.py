#Frase
texto = input("Escriba el texto para evaluarlo: ")
#Encontrar
coma = ","
punto = "."
espacio = " "

numero_comas = 0
numero_puntos = 0
numero_espacios = 0

for i in texto:
    if coma in i:
        numero_comas += 1
    elif punto in i:
        numero_puntos += 1
    elif espacio in i:
        numero_espacios += 1

print("El número de comas es: {}".format(numero_comas))
print("El número de puntos es: {}".format(numero_puntos))
print("El número de espacios es: {}".format(numero_espacios))


vocales = ["a", "e", "i", "o", "u"]
frase = "oidduyauidvaudtvaiudtvaiutdvautodiyavdvou"
numero_vocales = 0

for letra in frase:
    if letra in vocales:
        numero_vocales += 1

print("El numero de vocales en la frase es de: {}".format(numero_vocales))
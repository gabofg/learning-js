
numeros_introducidos = input("Digite los numeros separados por una coma[,]: ")
"""numeros_de_usuario = numeros_introducidos.split("")
numeros_de_usuario_limpios = []

for numeros in numeros_de_usuario:
    numeros_de_usuario_limpios.append(int(numeros))
    print(numeros)"""

numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]
#print(numeros_de_usuario)

numero_pequenio = numeros_de_usuario[0]
numero_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:
    if numero_pequenio > numero:
        numero_pequenio = numero

    if numero_grande < numero:
        numero_grande = numero

print("Numero grande mas: {} \n"
      "Numero pequeño mas: {}".format(numero_grande, numero_pequenio))


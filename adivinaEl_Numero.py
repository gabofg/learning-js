import random
numero = random.randint(1,10)
numero_jugador = int (input("Digita el número que crees que es: "))

if numero_jugador > 10:
    print("Te has pasado un poco ")

if numero_jugador < 1:
    print("Prueba con un numero mayor ;)")
    
if numero != numero_jugador:
    print("No adivinaste el número, el numero era: {}".format(numero))

if numero_jugador == numero:
    print("Bien hecho el numero era: {}".format(numero))


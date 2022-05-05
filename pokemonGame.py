import random
from random import randint
import os

vida_pikachu = 100

vida_squirtel = 100

while vida_pikachu > 0 and vida_squirtel > 0:
    #Se desenvuelven los turnos de combate

    #Turno de pikachu
    titulo_pikachu = "Ataca pikachu"
    print("\n" + "-" * len(titulo_pikachu) + "\n" + titulo_pikachu + "\n" + "-" * len(titulo_pikachu) + "\n")
    ataque_pikachu = random.randint(1,2)

    if ataque_pikachu == 1:
        #Bola voltio
        vida_squirtel -= 40
        barra_pikachu = "#" * vida_pikachu
        barra_squirtle = "#" * vida_squirtel
        print("Pikachu:  [{}] {}HP\n"
              "Squirtle: [{}] {}HP\n".format(barra_pikachu,vida_pikachu,barra_squirtle,vida_squirtel))
    else:
        #Cola ferrea
        vida_squirtel -= 20
        barra_pikachu = "#" * vida_pikachu
        barra_squirtle = "#" * vida_squirtel
        print("Pikachu:  [{}] {}HP\n"
              "Squirtle: [{}] {}HP\n".format(barra_pikachu, vida_pikachu, barra_squirtle, vida_squirtel))

    input("\nEnter para continuar...")
    os.system("cls")

    #Turno de Squirtle
    titulo_squirtle = "Ataca Squirtle"
    print("\n" + "-" * len(titulo_squirtle) + "\n" + titulo_squirtle + "\n" + "-" * len(titulo_squirtle) + "\n")

    ataque_squirtle = None

    while ataque_squirtle not in ["B", "P", "A"]:
        ataque_squirtle = input("¿Que ataque deseas realizar?\n\n"
                                "B - Burbuja\n"
                                "P - Placaje\n"
                                "A - Pistola Agua\n"
                                "Opción: ")

    if ataque_squirtle == "B" or ataque_squirtle == "b":
        vida_pikachu -= 30
        barra_pikachu = "#" * vida_pikachu
        barra_squirtle = "#" * vida_squirtel
        print("Pikachu:  [{}] {}HP\n"
              "Squirtle: [{}] {}HP\n".format(barra_pikachu, vida_pikachu, barra_squirtle, vida_squirtel))

    elif ataque_squirtle == "P" or ataque_squirtle == "p":
        vida_pikachu -= 50
        barra_pikachu = "#" * vida_pikachu
        barra_squirtle = "#" * vida_squirtel
        print("Pikachu:  [{}] {}HP\n"
              "Squirtle: [{}] {}HP\n".format(barra_pikachu, vida_pikachu, barra_squirtle, vida_squirtel))

    else: 
        vida_pikachu -= 10
        barra_pikachu = "#" * vida_pikachu
        barra_squirtle = "#" * vida_squirtel
        print("Pikachu:  [{}] {}HP\n"
              "Squirtle: [{}] {}HP\n".format(barra_pikachu, vida_pikachu, barra_squirtle, vida_squirtel))

    input("\nEnter para continuar...")
    os.system("cls")

if vida_pikachu > vida_squirtel:
    gana_pikachu = "Gana pikachu"
    print("\n" + "-" * len(gana_pikachu) + "\n" + gana_pikachu + "\n" + "-" * len(gana_pikachu) + "\n")
elif vida_squirtel > vida_pikachu:
    gana_squirtle = "Gana squirtle"
    print("\n" + "-" * len(gana_squirtle) + "\n" + gana_squirtle + "\n" + "-" * len(gana_squirtle) + "\n")

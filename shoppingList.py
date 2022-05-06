import os

items = []
while "Q" not in items:
    items.append(input("\n¿Que deseas añadir a la lista?          [Q] para salir\n"
                       "> "))
    os.system("cls")
    ultimo = items[-1]


    if "Q" in items:
        print("Los elementos de la lista son: {}".format(items))

    else:
        eleccion = None
        while eleccion not in ["S", "N", "s", "n"]:
            eleccion = input("\n¿Estas seguro de que deseas añadir {} a la lista?   [S/N]\n"
                             "Opción: ".format(ultimo))
            os.system("cls")

        if eleccion == "S":
            print("\n{} se a añadido correctamente a la lista.".format(ultimo))
            print(items)

        else:
            print("\n{} no a sido añadido a la lista.".format(ultimo))
            items.pop()

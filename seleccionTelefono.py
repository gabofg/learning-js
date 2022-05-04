#Programa para ayudar a escoger un teléfono

titulo = "| Bienvenido a mi programa para elegir tu teléfono |"
print("\n" + "-" * len(titulo) + "\n" + titulo + "\n" + "-" * len(titulo) + "\n")

opSystem = input("¿Que sistema poerativo prefieres?\n"
                 "A - Android\n"
                 "B - IOS\n"
                 "Opcion: ")

if opSystem == "A" or opSystem == "a":
    dinero = input("\n¿Tienes dinero?\n"
                   "A - Si\n"
                   "B - No\n"
                   "Opcion: ")

    if dinero == "A" or dinero == "a":
        importancia = input("\n¿Te importa la calidad del movil?\n"
                            "A - Si\n"
                            "B - No\n"
                            "Opcion: ")

        if importancia == "A" or importancia == "a":
            print("\nCompra un Google Pixel Super Camara")

        elif importancia == "B" or importancia == "b":
            print("\nCompra un Android Calidad/Precio")

        else:
            print("\nCreo que no has respondido correctamente, prueba con (A, B)")

    elif dinero == "B" or dinero == "b":
        print("\nCompra un Android Chino de 100$")

    else:
        print("\nCreo que no has respondido correctamente, prueba con (A, B)")

elif opSystem == "B" or opSystem == "b":
    dinero = input("\n¿Tienes dinero?\n"
                   "A - Si\n"
                   "B - No\n"
                   "Opcion: ")

    if dinero == "A" or dinero == "a":
        print("\nCompra un Iphone Pro Super Max")

    elif dinero == "B" or dinero == "b":
        print("\nCompra un Iphone de sgunda mano")

    else:
        print("\nCreo que no has respondido correctamente, prueba con (A, B)")

else:
    print("\nCreo que no has respondido correctamente, prueba con (A, B)")

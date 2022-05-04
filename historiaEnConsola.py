#Pequeña historia en consola CAZA EN EL BOSQUE

titulo = "| CAZA EN EL BOSQUE |"
print("\n" + "-" * len(titulo) + "\n" + titulo + "\n" + "-" * len(titulo) + "\n")

arma = input("Te encuentras como siempre en tu cabaña del monte, tienes que ir a cazar para sobrevivir\n"
      "pero tienes que escoger entre el rifle de larga distancia y la escopeta.\n\n"
      "A - Rifle de larga distancia\n"
      "B - Escopeta\n"
      "Opción: ")

camino = input("\n\nAhora que tienes tu arma tienes que escoger el camino que vas a seguir.\n\n"
               "A - Camino de grava con una pendiente empinada al final\n"
               "B - Bosque repleto de arboles y vegetación\n"
               "Opción: ")

if camino == "A" or camino == "a":
    opcion_camino = input("\nAvanzas por el camino rapidamente porque ya te lo conoces, pero ahora tienes que escoger la posición para estar durante horas esperando\n\n"
                          "A - Subes por la colina para coger altura y disparar desde lejos\n"
                          "B - Te escondes a un lado del camino ocultado con la vegetación, esperando a que haya movimiento por el camino\n"
                          "Opción: ")

    if opcion_camino == "A" or opcion_camino == "a":
        opcion_camino_dos = input("\nBien, despues de una tediosa subida llegas bien a la cima de la colina, ahora tienes que escoger si permanecer entre la"
                                " vegetación o asomar por la colina\n\n"
                                "A - Me quedo en la vegetación para sorprender a mi presa\n"
                                "B - Me asomo por la colina para disparar desde lejos\n"
                                "Opción: ")

        if opcion_camino_dos == "A" or opcion_camino_dos == "a" and arma == "B" or arma == "b":
            eleccion = input("\nEsta pasando un cervatillo que ves entre la vegetación\n\n"
                             "A - Disparas al cervatillo\n"
                             "B - Esperas a ver si pasa una presa mas grande\n"
                             "Opción: ")

            if eleccion == "A" or eleccion == "a":
                print("Le disparas y aciertas, te llevas un pequeño cervatillo a tu casa, ¿menos es nada no?")

            elif eleccion == "B" or eleccion == "b":
                print("Te quedas esperando todo lo que queda de dia sin que aparezca nada mas, mas suerte para la próxima :)")

            else:
                print("Creo que no has elegido correctamente la respuesta, prueba con (A o B)")


        elif opcion_camino_dos == "A" or opcion_camino_dos == "a" and arma == "A" or arma == "a":
            eleccion = input("\nEsta pasando un cervatillo que ves entre la vegetación\n\n"
                             "A - Disparas al cervatillo\n"
                             "B - Esperas a ver si pasa una presa mas grande\n"
                             "Opción: ")

            if eleccion == "A" or eleccion == "a":
                print("Le disparas y aciertas, te llevas un pequeño cervatillo a tu casa, ¿menos es nada no?")

            elif eleccion == "B" or eleccion == "b":
                print(
                    "Te quedas esperando todo lo que queda de dia sin que aparezca nada mas, mas suerte para la próxima :)")

            else:
                print("Creo que no has elegido correctamente la respuesta, prueba con (A o B)")

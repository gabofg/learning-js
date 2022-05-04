#Prueba Quiz con python

titulo = "| Bienvenido a mi Quiz sobre videojuegos |"
print("-" * len(titulo) + "\n" +titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0


#Pregunta 1
opcion = input("¿Cual es tu videojuego favorito?\n\n"
               "A - Minecraft\n"
               "B - League of Leguends\n"
               "C - Counter Strike\n\n"
               "Respuesta: ")

if opcion == "A" or opcion == "a":
    puntuacion += 10

elif opcion == "B" or opcion == "b":
    puntuacion += 0

elif opcion == "C" or opcion == "c":
    puntuacion += 5

else:
    print("Las opciones posibles son (A , B , C)")
    exit()


#Pregunta 2
opcion = input("\n¿En que plataforma juegas?\n\n"
               "A - Consola\n"
               "B - Ordenador\n"
               "C - Movil\n\n"
               "Respuesta: ")

if opcion == "A" or opcion == "a":
    puntuacion += 5

elif opcion == "B" or opcion == "b":
    puntuacion += 10

elif opcion == "C" or opcion == "c":
    puntuacion += 0

else:
    print("Las opciones posibles son (A , B , C)")
    exit()


#Pregunta 3
opcion = input("\n¿Con quien prefieres jugar?\n\n"
               "A - Solo\n"
               "B - Desconocidos\n"
               "C - Amigos\n\n"
               "Respuesta: ")

if opcion == "A" or opcion == "a":
    puntuacion += 0

elif opcion == "B" or opcion == "b":
    puntuacion += 5

elif opcion == "C" or opcion == "c":
    puntuacion += 10

else:
    print("Las opciones posibles son (A , B , C)")
    exit()


final = "| Tu puntuación es de: {}/30 puntos |".format(puntuacion)
print("-" * len(final) + "\n" +final + "\n" + "-" * len(final) + "\n")
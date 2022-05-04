#Pueba conversor de divisas con python

titulo = "| Bienvenido a mi conversor de divisas |"
print("-" * len(titulo) + "\n" + titulo + "\n" + "-" * len(titulo) + "\n")

#Conversiones
euro_dolar = 1.05
dolar_euro = 0.95
euro_libra = 0.83
libra_euro = 1.19

seleccion = input("Escoge la acción que quieres realizar \n\n"
                  "A - Pasar de euros a dolares \n"
                  "B - Pasar de dolares a euros \n"
                  "C - Pasar de euros a libras \n"
                  "D - Pasar de libras a euros \n\n"
                  "Opción: ")
cantidad = 0

#Euro --> Dolar
if seleccion == "A" or seleccion == "a":

    titulo_dos = "| Euro --> Dolar |"
    print("\n" + "-" * len(titulo_dos) + "\n" + titulo_dos + "\n" + "-" * len(titulo_dos) + "\n")

    cantidad = float(input("Selecciona la cantidad a convertir: "))
    valor = cantidad * euro_dolar
    print("\nEl valor en dolares es de: {}$".format(valor))

#Dolar --> Euro
elif seleccion == "B" or seleccion == "b":

    titulo_dos = "| Dolar --> Euro |"
    print("\n" + "-" * len(titulo_dos) + "\n" + titulo_dos + "\n" + "-" * len(titulo_dos) + "\n")

    cantidad =float(input("Selecciona la cantidad a convertir: "))
    valor = cantidad * dolar_euro
    print("\nEl valor en euros es de: {}€".format(valor))

#Euro --> Libra
elif seleccion == "C" or seleccion == "c":

    titulo_dos = "| Euro --> Libra |"
    print("\n" + "-" * len(titulo_dos) + "\n" + titulo_dos + "\n" + "-" * len(titulo_dos) + "\n")

    cantidad = float(input("Selecciona la cantidad a convertir: "))
    valor = cantidad * euro_libra
    print("\nEl valor en libras es de: {}£".format(valor))

#Libra --> Euro
elif seleccion == "D" or seleccion == "d":

    titulo_dos = "| Libra --> Euro |"
    print("\n" + "-" * len(titulo_dos) + "\n" + titulo_dos + "\n" + "-" * len(titulo_dos) + "\n")

    cantidad = float(input("Selecciona la cantidad a convertir: "))
    valor = cantidad * libra_euro
    print("\nEl valor en euros es de: {}€".format(valor))

else:
    print("No ha elegido ninguna de las opciones que el programa le ofrece, porfavor pruebe con A, B, C, D")
    exit()

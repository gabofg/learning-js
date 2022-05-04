edad = int(input("¿Que edad tienes? --> "))
carnet = input("Que tipo de carnet tienes (U / Para universitario, P / Para pensionista, F / Para familia numerosa, N / Ninguno ): ")

if (25 <= edad <= 35 and carnet == "U") or \
        (edad <= 10) or \
        (edad >= 65 and carnet == "P") or \
        (carnet == "F"):

    print("Tienes acceso al 25% de descuento :)")
else:
    print("No se te aplica el descuento")
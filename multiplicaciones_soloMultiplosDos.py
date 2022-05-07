#Solo mostrar los multiplos de dos

numero_user = int(input("Digite el número para hacer la tabla: "))
long_tabla = int(input("Digite la cantidad de veces que quiere multiplicar el numero: "))
resultado = 0
for i in range(1, long_tabla + 1):
    resultado = numero_user * i
    multiplos = (resultado % 2)

    if multiplos == 0:
        print(" {} * {} = {}".format(numero_user, i, resultado))
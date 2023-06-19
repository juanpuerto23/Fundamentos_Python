""""Programa para calcular el cuadrante de un plano cartesiano """

print("----------------------------------------------")
print("-------  Cuadrante de plano cartesiano -------")
print("----------------------------------------------")

X = int(input("Digite la coordenada de X: "))
Y = int(input("Digite la coordenada de Y: "))

if ((X > 0) and (Y > 0)):
    print("Punto en el primer cuadrante");
elif ((X < 0) and (Y > 0)):
    print("Punto en el segundo cuadrante");
elif((X < 0) and (Y < 0)):
    print("Punto en el tercer cuadrante");
elif((X > 0) and (Y < 0)):
    print("Punto en el cuarto cuadrante");
elif((X == 0) and (Y < 0) or (Y > 0)):
    print("Punto en el eje Y")
elif((X < 0) or (X > 0) and (Y == 0)):
    print("Punto en el eje X")
else:
    print("Punto de origen"); 
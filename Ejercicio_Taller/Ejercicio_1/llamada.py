""""Programa para calcular el valor de una llamada de $300/min"""

print("----------------------------------------------")
print("------------ Costo llamada -------------------")
print("----------------------------------------------")

X = int(input("Ingrese el tiempo de la llamada (minutos): "))

if X <= 3:
    print("La llamada tiene un costo de 300");
elif X > 3:
    Y = (((X * 50) + 150))
    print("La llamada tiene un costo de: " + str(Y))
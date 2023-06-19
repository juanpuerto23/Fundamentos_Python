"""Programa para determinar si dado 3 numeros enteros, la suma de los dos primeros es igual al tercero"""

X = int(input("Digite el primer numero entero: "))
Y = int(input("Digite el segundo numero entero: "))
Z = int(input("Digite el tercer numero entero: "))

print("----------------------------------------------")
print("------- La suma de 2 primeros  -------")
print("----------------------------------------------")

if X + Y == Z:
    print("La suma entre ", X, " y ", Y, " es equivalente a ", Z)

else:
    print("La suma entre ", X, " y ", Y, " no es equivalente a ", Z)
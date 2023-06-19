""""Programa para determinar si los dos ultimos digitos de un numero son iguales"""

print("----------------------------------------------")
print("---------- Ultimos digitos iguales -----------")
print("----------------------------------------------")

X = int(input("Ingrese un número: "))

Y = int(str(X)[-1])
Z = int(str(X)[-2])

if Y == Z:
    print("Los ultimos dos digitos de " + str(X) + " son iguales.")

else:
    print("Los ultimos dos digitos de " + str(X) + " no son iguales.")
""""Programa para que que dados 3 números los devuelva en orden ascendente."""

print("----------------------------------------------")
print("-------- Números en orden ascendente ---------")
print("----------------------------------------------")

X = int(input("Ingrese un número: "))
Y = int(input("Ingrese un segundo número: "))
Z = int(input("Ingrese un tercer número: "))

if  (X > Y and Y > Z):
    print("El número mayor es: " + str(X))
    print("El número mayor es: " + str(Y))
    print("El número mayor es: " + str(Z))

elif (X > Z and Z > Y):
    print("El número mayor es: " + str(X))
    print("El número mayor es: " + str(Z))
    print("El número mayor es: " + str(Y))

elif (Y > X and X > Z):
    print("El número mayor es: " + str(Y))
    print("El número mayor es: " + str(X))
    print("El número mayor es: " + str(Z))

elif (Y > Z and Z > X):
    print("El número mayor es: " + str(Y))
    print("El número mayor es: " + str(Z))
    print("El número mayor es: " + str(X))

elif (Z > Y and Y > X):
    print("El número mayor es: " + str(Z))
    print("El número mayor es: " + str(Y))
    print("El número mayor es: " + str(X))

elif (Z > X and X > Y):
    print("El número mayor es: " + str(Z))
    print("El número mayor es: " + str(X))
    print("El número mayor es: " + str(Y))

else:
    print("Se agregaron números iguales.")

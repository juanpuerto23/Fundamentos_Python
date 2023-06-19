""""Programa para calcular la potencia de dos numeros"""

print("----------------------------------------------")
print("---------- Potencia de dos numeros -----------")
print("----------------------------------------------")

# Input

X = input("Ingrese la base: ")
X = int(X)
Y = input("Ingrese el exponente: ")
Y = int(Y)

# Processing

Z = X ** Y

# Output

print(str(X) + " elevado a la " + str(Y) + " es igual a " + str(Z))
""""Programa para que lea un número entero y determine si es un 
número positivo de 4 dígitos"""

print("----------------------------------------------")
print("------- Número positivo de 4 dígitos ---------")
print("----------------------------------------------")

X = int(input("Digite el número de 4 digitos: "))

if X >= 1000:
    print("El número " + str(X) + (" es un número positivo de 4 digitos."));
elif X >= 0:
    print("El número " + str(X) + (" es un número positivo."));
else:
    print("El número " + str(X) + (" es un número negativo."));


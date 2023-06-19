""""Programa para que lea un número entero y que determine si su 
último dígito es un número par"""

print("----------------------------------------------")
print("------- Ultimo dígito es un número par -------")
print("----------------------------------------------")

X = int(input("Digite el número: "))

if X % 2 == 0:
    print("El ultimo dígito del número " + str(X) + " es par");
else:
    print("El ultimo dígito del número " + str(X) + " es impar");
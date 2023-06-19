""""Programa para calcular un numero par o impar"""

print("----------------------------------------------")
print("----------  Numero par o impar ---------------")
print("----------------------------------------------")

X = int(input("Ingrese el número: "))

if (X % 2 == 0):
    print("El número " + str(X) + " es par.");
else:
    print("El número " + str(X) + " es impar.");
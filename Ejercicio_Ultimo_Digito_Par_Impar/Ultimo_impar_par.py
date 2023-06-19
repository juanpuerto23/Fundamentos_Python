""""Programa para calcular si el ultimo digito de un numero es par o impar"""

print("----------------------------------------------")
print("--------  Ultimo Digito par o impar ----------")
print("----------------------------------------------")

X = int(input("Digite el número: "))

Y = X % 10

if (Y % 2 == 0):
    print(str(X) + " es par.")
else:
    print(str(X) + " es impar.")
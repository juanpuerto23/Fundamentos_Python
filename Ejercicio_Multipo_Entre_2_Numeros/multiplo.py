""""Programa para calcular si un numero entero es multiplo de otro"""

print("\n---------------------------------------------")
print("----------- Multiplo de 2 numeros -----------")
print("---------------------------------------------\n")

X = int(input("Digite un número: "))
Y = int(input("Digite otro número: "))

if Y <= 0 or X <= 0:
    print("No se permite el número 0 o números negativos")

elif X > Y:
    Z = X % Y
    if Z == 0:
        print(X, " es multiplo de ", Y)
    else:
        print(X, " no es multiplo de ", Y)

elif Y > X:
    Z = Y % X
    if Z == 0:
        print(Y, " es multiplo de ", X)
    else:
        print(Y, " no es multiplo de ", X)

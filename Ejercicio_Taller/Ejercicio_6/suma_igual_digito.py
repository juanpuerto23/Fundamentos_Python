""""Programa para determinar si el resultado de sumar sus dos últimos
dígitos es un número de 1 dígito."""

print("----------------------------------------------")
print("-------- Suma equivalente a 1 digito ---------")
print("----------------------------------------------")

X = int(input("Ingrese un número: "))

Y = int(str(X)[-1])
Z = int(str(X)[-2])
W = Y + Z

if W < 10:
    print("La suma de los dos ultimos digitos de " + str(X) + " es un números de 1 digito.")

else:
    print("La suma de los dos ultimos digitos de " + str(X) + " es un número de 2 digitos.")
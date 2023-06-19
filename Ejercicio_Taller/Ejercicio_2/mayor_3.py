""""Programa para calcular el valor mayor de 3 numeros"""

print("----------------------------------------------")
print("-------- Valor mayor de 3 numeros ------------")
print("----------------------------------------------")

X = int(input("Ingrese el primer valor: "))
Y = int(input("Ingrese el segundo valor: "))
Z = int(input("Ingrese el tercer valor: "))

if X<Y<Z:
    print(str(Z) + (" mayor que ") + str(Y) + " y " + str(X));
elif Z<=Y<=X:
    print(str(X) + (" mayor que ") + str(Y) + " y " + str(Z));
elif X>Z>Y:
    print(str(X) + (" mayor que ") + str(Z) + " y " + str(Y));
elif Z>X>Y:
    print(str(Z) + (" mayor que ") + str(X) + " y " + str(Y));
else:
    print(str(Y) + (" mayor que ") + str(X) + " y " + str(Z))



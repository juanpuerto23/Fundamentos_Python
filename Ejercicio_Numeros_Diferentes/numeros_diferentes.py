"""Programa No. 7:
Verificar si dos numeros son diferentes"""

print("---------------------------")
print("---- Numeros DIferentes ---")
print("---------------------------")

#input

X = int(input("Digite el valor de X: "))
Y = int(input("Digite el valor de Y: "))

#processing

if X != Y:
    msj = "son diferentes"
else:
    msj = "son iguales"

#output

print("Los numeros " + msj)
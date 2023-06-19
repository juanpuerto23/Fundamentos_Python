""""Programa para calcular el cociente y el residuo"""

print("----------------------------------------------")
print("------------ Cociente Y Residuo --------------")
print("----------------------------------------------")

# Input 

X = input("Introduzca el dividendo: ")
X = int(X)
Y = input("Introduzca el divisor: ")
Y = int(X)

# Processing

Z1 = (X / Y)
Z2 = (X % Y)
Z3 = (X // Y)

# Output


print("La división es: " + str(Z1))
print("El módulo es: " + str(Z2))
print("La división entera es: " + str(Z3))
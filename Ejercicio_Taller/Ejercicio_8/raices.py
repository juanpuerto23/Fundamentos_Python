""""Programa para resolver una ecuación de segundo grado"""

print("----------------------------------------------")
print("----------- Ecuación segundo grado -----------")
print("----------------------------------------------")

A = int(input("Ingrese el número del termino cuadratico: "))
E = int(input("Ingrese el número del termino lineal: "))
I = int(input("Ingrese el número del termino independiente: "))

from math import sqrt

O = (E**2)-4*A*I

if O < 0: 
    print("Los terminos equivalen al grupo de los números complejos");

else: 
  U1 = (-E+sqrt(E**2-(4*A*I)))/(2*A)
  U2 = (-E-sqrt(E**2-(4*A*I)))/(2*A)
  print("Las X de la ecuación son: " + str(U1) + " y " + str(U2))


""""Hacel el programa en Python que genere 1000 numeros aleatorios y que averigue e imprima cuantos son 
pares y cuantos son impares"""
import random
# input
n = int(input("Digite la cantidad de numeros: "))
# processing
pares = 0
impares = 0
rta = "Numeros = ("
for i in range(n):
    num_aleatorio = random.randint(1,200)
    if num_aleatorio % 2 == 0:
        pares += 1
    else:
        impares += 1
    if i < n - 1:
        rta = rta + str(n) + " ,"
    else:
        rta = rta + str(n)
# output
print("------Resultados------")
print(rta)
print(f"Cantidada de pares: {pares}")
print(f"Cantidada de impares: {impares}")
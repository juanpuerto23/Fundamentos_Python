""""FRECUENCIA DE LANZAMIENTO DE DADOS"""
import random
# input
n = int(input("Digite la cantidad de dados: "))
# processing
cara1 = 0
cara2 = 0
cara3 = 0
cara4 = 0
cara5 = 0
cara6 = 0
rta = "Lanzamiento = ("
for i in range(n):
    dado = random.randint(1,6)
    if dado == 1:
        cara1 += 1
    elif dado == 2:
        cara2 += 1
    elif dado == 3:
        cara3 += 1
    elif dado == 4:
        cara4 += 1
    elif dado == 5:
        cara5 += 1
    elif dado == 6:
        cara6 += 1
    else:
        print("Cara no valida")
    if i < n - 1:
        rta = rta + str(dado) + " ,"
    else:
        rta = rta + str(dado)
rta = rta + ")\nCara 1:"
for i in range(cara1):
    rta = rta + "*"
rta = rta + "->" + str(cara1)
# output
print("------RESULTADO------")
print(rta)
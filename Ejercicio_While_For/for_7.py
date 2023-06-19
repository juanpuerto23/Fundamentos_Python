""""Haga un programa para averiguar e imprimir cuantos multiplos de 9 y cuantos multiplos de 7 hay en los
numeros comprendidos"""

# input
m = int(input("Digite el valor de m: "))
n = int(input("Digite el valor de n: "))
# processing
multiplos7 = 0
multiplos9 = 0
for i in range(m, n+ 1, 1):
    if i % 7 == 0:
        multiplos7 += 1
    if i % 9 == 0:
        multiplos9 += 1
# output
print("------RESULTADO------")
print("Entre {m} y {n} hay: ")
print(f"{multiplos7} multiplos de 7")
print(f"{multiplos9} multiplos de 9")
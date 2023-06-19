""""Generar la siguiente serie 2,6,12,20,30,42,56,...,n"""

# input
n = int(input("Digite el valor de n:"))
# processing
s = "Serie: "
for i in range(1,n + 1):
    t = (i**2) + i
    if i < n:
        s = s + str(t) + ","
    else:
        s = s + str(t)
# output
print("------RESULTADO------")
print(s)
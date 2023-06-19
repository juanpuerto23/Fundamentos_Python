""""Generar la siguiente serie 1/2, 1/5, 1/10, 1/17, 1/26,...,n"""

# input
n = int(input("Digite el valor de n:"))
# processing
s = "Serie: 1, "
for i in range(1,n + 1):
    t = (i**2) + 1
    if i < n:
        s = s + "1/" + str(t) + ", "
    else:
        s = s + "1/" + str(t)
# output
print("------RESULTADO------")
print(s)
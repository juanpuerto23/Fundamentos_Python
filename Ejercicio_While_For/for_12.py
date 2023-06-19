""""Generar la siguiente serie 1, 1/2, 1/3, 1/4, 1/5,...,n"""

# input
n = int(input("Digite el valor de n:"))
# processing
s = "Serie: 1, "
for i in range(2,n + 1):
    t = i
    if i < n:
        s = s + "1/" + str(t) + ", "
    else:
        s = s + "1/" + str(t)
# output
print("------RESULTADO------")
print(s)
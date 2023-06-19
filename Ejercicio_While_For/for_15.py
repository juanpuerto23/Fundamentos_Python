""""Generar la siguiente serie 3,8,13,18,23,28,...,n"""

# input
n = int(input("Digite el valor de n:"))
# processing
s = "Serie: "
for i in range(1,n + 1):
    t = (5*i)-2
    if i < n:
        s = s + str(t) + ","
    else:
        s = s + str(t)
# output
print("------RESULTADO------")
print(s)
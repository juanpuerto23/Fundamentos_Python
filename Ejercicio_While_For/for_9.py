""""Generar la siguiente serie2,4,6,8,10,12,14,16,18,...,n"""

# input
n = int(input("Digite el valor de n:"))
# processing
s = "Serie: "
for i in range(1,n + 1):
    t = 2*i
    if i < n:
        s = s + str(t) + ","
    else:
        s = s + str(t)
# output
print("------RESULTADO------")
print(s)
# input

h = int(input("Digite la altura: "))

# processing

q = h / 5
n = 0

while (h >= q):
    h = h - (h * 0.10)
    n = n + 1
    print("La altura " + str(round(h, 3)) + " se alcanza en el rebote " + str(n))

# output

print("La pelota no alcanza la quinta parte de la altura inicial en el rebote " + str(n))

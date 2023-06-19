# Programa que digite su nombre y le cuente cuantas vocales hay en su nombre
nombre = input("Digite su nombre: ")
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
for letra in nombre:
    if letra.lower() in "a":
        contador_a += 1
    elif letra.lower() in "e":
        contador_e += 1
    elif letra.lower() in "i":
        contador_i += 1
    elif letra.lower() in "o":
        contador_o += 1
    elif letra.lower() in "u":
        contador_u += 1
print("El nombre" + nombre + " contiene " + str(contador_a) + " vocales a, " + str(contador_e) + " vocales e, " + str(contador_i) + " vocales i, " + str(contador_o) + " vocales o, " + str(contador_u) + " vocales u.")

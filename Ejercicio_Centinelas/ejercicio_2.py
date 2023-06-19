n = int(input("Digite un número entero: "))
par = 0
impar = 0

while n != 0:
    r = (n % 2)
    if r == 0:
        par += 1
    else:
        impar += 1
    n = int(input("Digite un número entero: "))

print("Los números impares son: " + str(impar) + " y los numeros pares son " + str(par))
    
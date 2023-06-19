def voltear_numero(reverso_n):
    n = reverso_n
    r = 0
    while(n > 0):
        a = n % 10 
        r = r * 10 + a
        n = n // 10
    return(r)

numero = int(input("Ingrese un número: "))

if numero % 10 == 0: 
    numero = numero // 10

if numero == voltear_numero(numero) :
    print(numero,"es un número palindromo")

else :
    print(numero,"no es un número palindromo")
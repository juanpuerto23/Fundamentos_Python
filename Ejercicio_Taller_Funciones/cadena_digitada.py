print("-------------------------------")
print("--RECIBIR UNA CADENA DIGITADA--")
print("-------------------------------")

def MostrarCadena(cadena, n):
    for i in range(n):
        print(cadena)
    
n = int(input("Digite las veces que quiere repetir la cadena: "))
cadena = input("Digite su cadena: ")
MostrarCadena(cadena, n)
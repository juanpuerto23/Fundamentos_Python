print("------------------------------")
print("-BUSCAR UN NUMERO EN CONJUNTO-")
print("------------------------------")

def buscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

# input
dato = int(input("Numero a buscar: "))

# processing
lista = [1,2,3,4,5]
if buscarDatoEnLista(dato, lista):
    print("Lo encontré")
else:
    print("No lo encontré")

# output
print("\nEso era.....")
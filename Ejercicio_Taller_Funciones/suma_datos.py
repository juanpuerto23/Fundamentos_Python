lista = []
n = int(input("Digite la cantidad de elementos en la lista: ")) 
for i in range(0, n):
    ultimo = int(input("Digite un número: "))
    lista.append(ultimo)

suma = sum(lista)
print(f"La suma de  {lista} es  {suma}")


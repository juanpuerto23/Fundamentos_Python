import statistics
lista = []
n = int(input("Digite la cantidad de elementos en la lista: ")) 
for i in range(0, n):
    ultimo = int(input("Digite un número: "))
    lista.append(ultimo)

promedio = statistics.mean(lista)
print(f"El promedio de {lista} es {promedio}")

def funcion(x):
    x.append(5)

# Programa principal
x = [1,2]
funcion(x)
print(x)

"""Salida:
[1,2,5]

El progrma aprincipal genera la lista [1,2] que se pasa a la función.
La función agrega el elemento 5 al final de la lista.
Como la lista se pasa por referencia, automáticamente aparece en el programa principal en la llamada de la función.
Rodos los arreglos, de cualquier tipo, y de cualquier dimensión, se pasan por referencia."""
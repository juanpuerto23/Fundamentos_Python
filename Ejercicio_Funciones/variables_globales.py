"""Se omite el parámetro x en el llamado de la función ya que la variable es global"""
def f():  
    global x
    x = x + 1
    print("Valor de X dentro de f(x) = ", x)
    return x 

# Algoritmo principal
x = 3
print("Valor inicial de x = ", x)
z = f(x)
print("Valor de x despues de llamar a f(x) = ", x)


capital = int(input("Ingrese el valor del capital: "))

doble = capital * 2
meses = 0

while (capital <= doble):
    capital = capital + (capital * 0.05)
    meses = meses + 1

print ("La cantidad de meses necesarios para duplicar el capital inicial es de " + str(meses) + " meses.")
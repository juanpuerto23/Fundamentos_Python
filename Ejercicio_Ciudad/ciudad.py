año = 1980
poblacion_a = 3.5
poblacion_b = 5

while (poblacion_a < poblacion_b):
    poblacion_b = poblacion_b + (poblacion_b * 0.05)
    poblacion_a = poblacion_a + (poblacion_a * 0.07)
    año = año + 1

print("En el año " + str(año) + " la poblacion A de " + str(poblacion_a) + " supero a la poblacion B de " + str(poblacion_b))
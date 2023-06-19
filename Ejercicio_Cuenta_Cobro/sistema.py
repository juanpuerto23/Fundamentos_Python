""""Programa para calcular el gasto mensual de agua (m3) sobre una vivienda"""

print("\n----------------------------------------------")
print("-------------- Sistema de cobro --------------")
print("----------------------------------------------")

metros_cubicos = int(input("\nIngrese los metros cubicos gastados: "))
cuota_fija_mensual = 10000

if metros_cubicos < 50:
    print("El valor a pagar es $", cuota_fija_mensual)

elif metros_cubicos >= 50 and metros_cubicos <= 200:
    cobro = ((metros_cubicos - 50) * 2000) + cuota_fija_mensual
    print("EL valor a pagar es $", cobro)

elif metros_cubicos > 200:
    cobro = ((metros_cubicos - 50) * 3000) + cuota_fija_mensual
    print("El valor a pagar es $", cobro)

else:
    print("Valor desconocido")

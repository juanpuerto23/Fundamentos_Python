print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
# input
codigo = int(input("Digite el codigo del estudiante: "))
nombre = input("Digite el nombre del estudiante: ")

if codigo != 0:
    nota1 = float(input("Digite la nota del parcila No. 1: "))
    nota2 = float(input("Digite la nota del parcila No. 2: "))
    nota3 = float(input("Digite la nota del parcila No. 3: "))
else:
    print("Fin de los datos de entrada")
# processing
reprobados = 0

while codigo != 0:
    nota_final = (nota1 + nota2 + nota3)/3
    print("EL estudiante de codigo " + str(codigo) + ", cuyo nombre es " + nombre + 
    ", obtuvo una nota definitiva de " + str(nota_final))
    if nota_final < 3:
        reprobados =+ 1
# input
        codigo = int(input("Digite el codigo del estudiante: "))
        nombre = input("Digite el nombre del estudiante: ")     
        if codigo != 0:
            nota1 = float(input("Digite la nota del parcila No. 1: "))
            nota2 = float(input("Digite la nota del parcila No. 2: "))
            nota3 = float(input("Digite la nota del parcila No. 3: "))
        else:
            print("Fin de los datos de entrada")
# output
print("Cantidad de estudiantes que reprobaron la materia: " + str(reprobados))

    
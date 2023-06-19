""""Programa que al ingresar el monto de la compra se obtenga
el monto del descuento o el monto del recargo y el total a pagar."""

print("----------------------------------------------")
print("------ Problema negocio total a pagar --------")
print("----------------------------------------------")

X = float(input("Ingresar monto de la compra: "))
Y = input("Cliente General o Cliente Afiliado: ")
Z = input("Pago de contado o Pago a plazos: ")

if Y == "Cliente General" and Z == "Pago de contado":
    W = X * 0.15
    T = (X - W)
    print("El monto de la compra es $" + str(X) + " , el monto de descuento o recargo es $" 
    + str(W) + " y el total a pagar es $" + str(T));

elif Y == "Cliente General" and Z == "Pago a plazos":
    W = X * 0.1
    T = (X + W)
    print("El monto de la compra es $" + str(X) + " , el monto de descuento o recargo es $" 
    + str(W) + " y el total a pagar es $" + str(T));

elif Y == "Cliente Afiliado" and Z == "Pago de contado":
    W = X * 0.2
    T = (X - W)
    print("El monto de la compra es $" + str(X) + " , el monto de descuento o recargo es $" 
    + str(W) + " y el total a pagar es $" + str(T));

elif Y == "Cliente Afiliado" and Z == "Pago a plazos":
    W = X * 0.05
    T = (X + W)
    print("El monto de la compra es $" + str(X) + " , el monto de descuento o recargo es $" 
    + str(W) + " y el total a pagar es $" + str(T));

else:
    print("Rectifique la información."); 

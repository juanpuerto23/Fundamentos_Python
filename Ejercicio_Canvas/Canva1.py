from textwrap import fill
from tkinter import Tk, Canvas, BOTH, Frame

# ----------------------
# VARIABLES GLOBALES
# ----------------------
BASE = 460
ALTURA = 380

# ----------------------
# VENTANA PRINCIPAL
# ----------------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D - Texto")
ventana_principal.resizable(False, False)
ventana_principal.config(bg = "green")

# ----------------------
# FRAME GRAFICACIÓN
# ----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "white", width = 480, height = 400)
frame_graficacion.pack(fill=BOTH, padx = 10, pady = 10)

# ----------------------
# CREACCIÓN CANVA
# ----------------------
C = Canvas(frame_graficacion, width = BASE, height = ALTURA)
C.place(x = 10, y = 10)

# ----------------------
# TEXTO
# ----------------------
texto = C.create_text(BASE/2, ALTURA/2, anchor = "center", text = "UIS Socorro", font = ("Arial", "20", "bold"), fill = "blue", activefill = "red")

# ----------------------
# LINEAS
# ----------------------
linea1 = C.create_line(0, 0, BASE, ALTURA, fill = "red", width = 5)
linea2 = C.create_line(0, ALTURA, BASE, 0, fill = "red", width = 5)
linea3 = C.create_line(BASE/2, 0, BASE/2, ALTURA/2, fill = "blue", width = 5)
linea4 = C.create_line(BASE, ALTURA/2, BASE/2, ALTURA/2, fill = "green", width = 5)
linea5 = C.create_line(BASE/2, ALTURA, BASE/2, ALTURA/2, fill = "yellow", width = 5)
linea6 = C.create_line(0, ALTURA/2, BASE/2, ALTURA/2, fill = "purple", width = 4)

# ----------------------
# CUADRADOS Y RECTANGULOS
# ----------------------
rect1 = C.create_rectangle(10, 10, (BASE/2)-10, (ALTURA/2)-10, fill = "pink", outline = "pink")
rect2 = C.create_rectangle(10,10,110,110, fill = "green")

# ----------------------
# POLIGONOS
# ----------------------
poli1 = C.create_polygon(0, ALTURA, BASE/2, 0, BASE, ALTURA, fill = "green", outline = "red", width = 5)

# ----------------------
# ELIPSES - CIRCULOS
# ----------------------


ventana_principal.mainloop()


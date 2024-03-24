from tkinter import Tk, Label, Button, PhotoImage
from datetime import datetime
import os

# Crear la ventana principal
mi_ventana = Tk()
mi_ventana.geometry("500x500")
mi_ventana.title("Mi GUI con Tkinter")

# Crear una etiqueta
mi_etiqueta = Label(mi_ventana, text="Estado del motor: Detenido", font=("Arial Bold", 20), fg="blue")
mi_etiqueta.place(x=0, y=100)

# Función para manejar el evento del botón
def girar_izquierda():
    mi_etiqueta.config(text="Estado del motor: Girando en sentido antihorario")
    mi_boton2.config(state="normal")
    mi_boton3.config(state="normal")
    mi_boton.config(state="disabled")

def girar_derecha():
    mi_etiqueta.config(text="Estado del motor: Girando en sentido horario")
    mi_boton2.config(state="normal")
    mi_boton3.config(state="disabled")
    mi_boton.config(state="normal")

def detener_motor():
    mi_etiqueta.config(text="Estado del motor: Detenido")
    mi_boton2.config(state="disabled")
    mi_boton3.config(state="normal")
    mi_boton.config(state="normal")

def actualizar_fecha_hora():
    fecha_hora_actual = datetime.now().strftime("%H:%M:%S - %Y-%m-%d")
    mi_etiqueta2.config(text=fecha_hora_actual)
    mi_ventana.after(1000, actualizar_fecha_hora)  # Actualizar cada segundo

# Crear una etiqueta para la fecha y hora
mi_etiqueta2 = Label(mi_ventana, text="", font=("Arial Bold", 20), fg="blue")
mi_etiqueta2.place(x=0, y=200)

# Crear un botón
imagen = PhotoImage(file="flecha-izquierda.png")
mi_boton = Button(mi_ventana, image=imagen, command=girar_izquierda)
mi_boton.place(x=0, y=0)
imagen2 = PhotoImage(file="pausa.png")
mi_boton2 = Button(mi_ventana, image=imagen2, command=detener_motor, state="disabled")
mi_boton2.place(x=100, y=0)
imagen3 = PhotoImage(file="flecha-correcta.png")
mi_boton3 = Button(mi_ventana, image=imagen3, command=girar_derecha)
mi_boton3.place(x=200, y=0)

actualizar_fecha_hora()
# Ejecutar el bucle de eventos
mi_ventana.mainloop()

from tkinter import Tk, Label, Button, PhotoImage
from datetime import datetime

# Crear la ventana principal
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Mi GUI con Tkinter")

# Crear una etiqueta
etiqueta = Label(ventana, text="Estado del motor: Detenido", font=("Arial Bold", 20), fg="blue")
etiqueta.place(x=0, y=100)

# Función para manejar el evento del botón
def izquierda():
    etiqueta.config(text="Estado del motor: Girando en sentido antihorario")
    boton2.config(state="normal")
    boton3.config(state="normal")
    boton.config(state="disabled")

def derecha():
    etiqueta.config(text="Estado del motor: Girando en sentido horario")
    boton2.config(state="normal")
    boton3.config(state="disabled")
    boton.config(state="normal")

def detener():
    etiqueta.config(text="Estado del motor: Detenido")
    boton2.config(state="disabled")
    boton3.config(state="normal")
    boton.config(state="normal")

def actualizar_fecha_hora():
    fecha_hora_actual = datetime.now().strftime("%H:%M:%S - %Y-%m-%d")
    etiqueta2.config(text=fecha_hora_actual)
    ventana.after(1000, actualizar_fecha_hora)  # Actualizar cada segundo

# Crear una etiqueta para la fecha y hora
etiqueta2 = Label(ventana, text="", font=("Arial Bold", 20), fg="blue")
etiqueta2.place(x=0, y=200)

# Crear un botón
imagen = PhotoImage(file="fotos/flecha-izquierda.png")
boton = Button(ventana, image=imagen, command=izquierda)
boton.place(x=0, y=0)
imagen2 = PhotoImage(file="fotos/pausa.png")
boton2 = Button(ventana, image=imagen2, command=detener, state="disabled")
boton2.place(x=100, y=0)
imagen3 = PhotoImage(file="fotos/flecha-correcta.png")
boton3 = Button(ventana, image=imagen3, command=derecha)
boton3.place(x=200, y=0)

actualizar_fecha_hora()
# Ejecutar el bucle de eventos
ventana.mainloop()
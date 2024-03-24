from tkinter import Tk, Label, Button, PhotoImage
from datetime import datetime

# Crear la ventana principal
principal = Tk()
principal.geometry("400x300")
principal.title("Control del Motor")

# etiqueta
estado = Label(principal, text="Estado del motor: \n Detenido", font=("Arial Bold", 20), fg="black")
estado.place(x=0, y=100)

nota = Label(principal, text="Use las fotos del compañero porque no encontre fotos de mismo tamaño", font=("Arial Bold", 8), fg="black")
nota.place(x=0, y=250)

# Funciónes de los botones
def girar_izquierda():
    estado.config(text="Estado del motor: \n Girando a la izquierda")
    detener.config(state="normal")
    derecha.config(state="normal")
    izquierda.config(state="disabled")

def girar_derecha():
    estado.config(text="Estado del motor: \n Girando a la derecha")
    detener.config(state="normal")
    derecha.config(state="disabled")
    izquierda.config(state="normal")

def detener_motor():
    estado.config(text="Estado del motor:\n Detenido")
    detener.config(state="disabled")
    derecha.config(state="normal")
    izquierda.config(state="normal")

def actualizar_fecha_hora():
    fecha_hora_actual = datetime.now().strftime("%H:%M:%S - %Y-%m-%d")
    etiqueta_fecha_hora.config(text=fecha_hora_actual)
    principal.after(1000, actualizar_fecha_hora)  # Actualizar cada segundo

# Colocar la etiqueta de la fecha y hora
etiqueta_fecha_hora = Label(principal, text="", font=("Arial Bold", 20), fg="black")
etiqueta_fecha_hora.place(x=0, y=200)

# poner imagenes en los botones
imagen_izquierda = PhotoImage(file="C:/Users/jesus/OneDrive/Documentos/GitHub/Motor/Desktop/fotos/izquierda.png")
izquierda = Button(principal, image=imagen_izquierda, command=girar_izquierda)
izquierda.place(x=0, y=0)

imagen_detener = PhotoImage(file="C:/Users/jesus/OneDrive/Documentos/GitHub/Motor/Desktop/fotos/pausa.png")
detener = Button(principal, image=imagen_detener, command=detener_motor, state="disabled")
detener.place(x=100, y=0)

imagen_derecha = PhotoImage(file="C:/Users/jesus/OneDrive/Documentos/GitHub/Motor/Desktop/fotos/derecha.png")
derecha = Button(principal, image=imagen_derecha, command=girar_derecha)
derecha.place(x=200, y=0)

salir = Button(principal, text="Salir", command=principal.quit, font=("Arial Bold", 15), fg="black")
salir.place(x=300, y=150)
# fecha y hora
actualizar_fecha_hora()

# while infinito
principal.mainloop()

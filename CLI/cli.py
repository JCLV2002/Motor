import datetime
import os

exit = "4"  
user = 0

while user != exit:

    fecha_actual = datetime.datetime.now()
    
    print("Fecha y hora actual: ", fecha_actual.strftime("%Y-%m-%d %H:%M:%S"))
    print("Bienvenido a Control de motor")
    print("1. Girar motor en sentido horario")
    print("2. Girar motor en sentido antihorario")
    print("3. Detener motor")
    print("4. Salir")

    entry = input("Ingrese comando para controlar el motor (ingrese {} para salir): ".format(exit))

    if entry == "1":
        print("Girando motor en sentido horario")
        #os.system('cls')
    elif entry == "2":
        print("Girando motor en sentido antihorario")
        #os.system('cls')
    elif entry == "3":
        print("Deteniendo motor")
        #os.system('cls')
    elif entry == "4":
        print("Saliendo")
        break
    else:
        print("Comando no válido")
        continue

print(" El programa ha terminado.")

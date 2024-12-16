import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from negocio.crud import *
from negocio.procesamiento import *
from Primer_menu import *
from servicios.Segundo_menu import maincrud


def menu_principal():
    while True:
        print("Bienvenido")
        print("1) Menú API")
        print("2) Menú API CRUD")
        
        # Solicitar al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")
        
        # Convertir la entrada a entero
        try:
            opcion = int(opcion)
        except ValueError:
            print("❌ Por favor ingrese un número válido.")
            continue

        if opcion == 1:
            main()
            break
        elif opcion == 2:
            maincrud()
        else:
            print("❌ Opción no válida, intente nuevamente.")

# Llamada al menú principal
menu_principal()
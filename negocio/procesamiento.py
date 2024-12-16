import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datos.db import conectar_bd

from datos.db import *
from colorama import Fore, init
from auxiliares.constantes import *
import requests
import json


# Función para mostrar el menú de opciones
def mostrar_menu():
    print(Fore.CYAN + "\n=== Menú de Opciones ===")
    print(Fore.CYAN + "1. Obtener todos los usuarios")
    print(Fore.CYAN + "2. Crear un nuevo usuario")
    print(Fore.CYAN + "3. Actualizar un usuario existente")
    print(Fore.CYAN + "4. Eliminar un usuario")
    print(Fore.CYAN + "5. Salir")
    print(Fore.CYAN + "========================")

# Función para leer la opción del usuario
def leer_opcion():
    while True:
        try:
            opcion = int(input(Fore.GREEN + "\nElige una opción (1-5): "))
            if opcion in [1, 2, 3, 4, 5]:
                return opcion
            else:
                print(Fore.RED + "Opción inválida, por favor elige un número entre 1 y 5.")
        except ValueError:
            print(Fore.RED + "Por favor ingresa un número válido.")
def leer_opcion_menu_principal():
    while True:
        try:
            opcion = int(input(Fore.GREEN + "\nElige una opción (1-2): "))
            if opcion in [1, 2]:
                return opcion
            else:
                print(Fore.RED + "Opción inválida, por favor elige un número entre 1 y 2.")
        except ValueError:
            print(Fore.RED + "Por favor ingresa un número válido.")


# Función principal que gestiona el flujo de opciones


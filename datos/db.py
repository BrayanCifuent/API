import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mysql.connector
from colorama import Fore, init

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database = "gestion_empleados"
        )
        return conexion
    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al conectar a la base de datos: {err}")
        return None


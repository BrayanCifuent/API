# main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cryptography.fernet import Fernet
from colorama import Fore
from servicios.servicios import *
from datos.datos import almacenar_datos_db, obtener_datos_db,almacenar_usuarios_db, conectar_bd
from negocio.negocio import encriptar_contraseña, desencriptar_contraseña, generar_clave, validar_contraseña,obtener_usuarios_api


def mostrar_menu():
    print("1. Encriptación de contraseña")
    print("2. Obtener usuarios desde la API y almacenarlos en DB")
    print("3. Crear un usuario API")
    print("4. Buscar en Google (API Serper)")
    print("5. Salir")

def leer_opcion():
    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        print("Opción no válida.")
        return 0

def main():
    clave = generar_clave()
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            contraseña = input("Ingrese la contraseña a encriptar: ")
            print(f"Contraseña ingresada: {contraseña}")
            contraseña_encriptada = encriptar_contraseña(clave, contraseña)
            print(f"Contraseña encriptada: {contraseña_encriptada}")
            contraseña_desencriptada = desencriptar_contraseña(clave, contraseña_encriptada)
            print(f"Contraseña desencriptada: {contraseña_desencriptada}")
            if validar_contraseña(contraseña, clave, contraseña_encriptada):
                print("La contraseña desencriptada coincide.")
            else:
                print("La contraseña desencriptada NO coincide.")
        
        elif opcion == 2:
            # Obtener datos desde la API
            print(Fore.CYAN + "\nObteniendo usuarios desde la API...")
            usuarios = obtener_usuarios_api()
            if usuarios:
                almacenar_usuarios_db(usuarios)
                print(Fore.GREEN + f"{len(usuarios)} usuarios obtenidos y almacenados en la DB local.")
                
                # Consultar la DB y mostrar los usuarios
                db = conectar_bd()
                cursor = db.cursor(dictionary=True)
                cursor.execute("SELECT * FROM usuariosT")
                for usuario in cursor.fetchall():
                    print(usuario)
                db.close()
            else:
                print(Fore.RED + "No se pudieron obtener usuarios desde la API.")
        
        elif opcion ==3:
            # Opción 2: Crear un usuario en la API
            print("Creando un usuario en la API...")
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese el correo del usuario: ")

            # Crear usuario en la API
            respuesta = crear_usuario_api(nombre, correo)
            if respuesta:
                print("Usuario creado correctamente en la API.")
            else:
                print("Hubo un error al crear el usuario en la API.")
        elif opcion == 4:
            query = input("Ingrese el término de búsqueda: ")
            resultados = buscar_en_google_api(query)
            if resultados:
                for item in resultados.get("organic", []):
                    print(f"Title: {item['title']}, Link: {item['link']}, Snippet: {item['snippet']}")
        
        elif opcion == 5:
            print("Saliendo...")
            break


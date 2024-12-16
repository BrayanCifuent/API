import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datos.db import conectar_bd
from datos.db import *
from colorama import Fore, init
from auxiliares.constantes import *
import requests
import json

a="hola"

def guardar_usuarios(usuarios):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        for usuario in usuarios:
            sql = "INSERT INTO usuarios_api (id, name, username, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (usuario.id, usuario.name, usuario.username, usuario.email))
        conexion.commit()
        cursor.close()
        conexion.close()



def agregar_usuario_api_a_bd():
    url = f"{url_base}/users"
    try:
        # Obtener usuarios desde la API
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        if respuesta.status_code == 200:
            usuarios_api = respuesta.json()
        else:
            print(Fore.RED + f"Error al obtener los usuarios desde la API: {respuesta.status_code}")
            usuarios_api = []
        
        # Conectar a la base de datos
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            # Insertar usuarios de la API en la base de datos
            for usuario in usuarios_api:
                # Verificar si el usuario ya existe en la base de datos (por ID)
                cursor.execute("SELECT id FROM usuarios_api WHERE id = %s", (usuario['id'],))
                if cursor.fetchone() is None:  # Si el usuario no existe
                    sql = """
                    INSERT INTO usuarios_api (id, name, username, email)
                    VALUES (%s, %s, %s, %s)
                    """
                    datos_usuario = (usuario['id'], usuario['name'], usuario['username'], usuario['email'])
                    cursor.execute(sql, datos_usuario)
                    print(Fore.GREEN + f"Usuario {usuario['name']} agregado a la base de datos.")
                else:
                    print(Fore.YELLOW + f"El usuario {usuario['name']} ya existe en la base de datos.")

            conexion.commit()  # Confirmar cambios
            cursor.close()
            conexion.close()
        else:
            print(Fore.RED + "Error al conectar a la base de datos.")
    
    except requests.exceptions.RequestException as error:
        print(Fore.RED + f"Error en la solicitud a la API: {error}")
    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al interactuar con la base de datos: {err}")

def obtener_usuario():
    url = f"{url_base}/users"
    try:
        # Obtener usuarios desde la API
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        if respuesta.status_code == 200:
            usuarios_api = respuesta.json()
        else:
            print(Fore.RED + f"Error al obtener los usuarios desde la API: {respuesta.status_code}")
            usuarios_api = []
        
        # Obtener usuarios desde la base de datos
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, name, username, email, habilitado FROM usuarios_api")
            usuarios_bd = cursor.fetchall()  # Obtener todos los usuarios de la base de datos
            cursor.close()
            conexion.close()
        else:
            usuarios_bd = []

        # Convertir la lista de usuarios_bd en un set de ids para evitar duplicados
        ids_usuarios_bd = {usuario[0] for usuario in usuarios_bd}

        # Filtrar los usuarios de la API para agregar solo los que no están en la base de datos
        usuarios_filtrados_api = [usuario for usuario in usuarios_api if usuario['id'] not in ids_usuarios_bd]

        # Combinamos los usuarios de la API y la base de datos
        usuarios_totales = usuarios_filtrados_api + [{'id': usuario[0], 'name': usuario[1], 'username': usuario[2], 'email': usuario[3], 'habilitado': usuario[4]} for usuario in usuarios_bd]

        # Mostrar usuarios con su estado de habilitación
        for usuario in usuarios_totales:
            habilitado = "Habilitado" if usuario['habilitado'] == 1 else "Deshabilitado"
            print(Fore.YELLOW + f"{usuario['id']} - {usuario['name']} - {usuario['username']} - {usuario['email']} - {habilitado}")

        return usuarios_totales

    except requests.exceptions.RequestException as error:
        print(Fore.RED + f"Error en la solicitud a la API: {error}")
        return []
    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al obtener usuarios de la base de datos: {err}")
        return []

def crear_usuario_api():
    nuevo_usuario = {
        "name": input(Fore.YELLOW + "Nombre del usuario: "),
        "username": input(Fore.YELLOW + "Username: "),
        "email": input(Fore.YELLOW + "Email: "),
    }

    # Convertir el nuevo usuario a formato JSON
    nuevo_usuario_json = json.dumps(nuevo_usuario)

    try:
        headers = {'Content-Type': 'application/json'}
        url = f"{url_base}/users"
        respuesta = requests.post(url, data=nuevo_usuario_json, headers=headers)

        if respuesta.status_code == 201:
            usuario_creado = respuesta.json()
            print(Fore.GREEN + f"Usuario creado exitosamente: {usuario_creado}")

            # Guardar el usuario en la base de datos
            conexion = conectar_bd()
            if conexion:
                cursor = conexion.cursor()

                # Ahora insertamos solo los campos name, username, email, habilitado
                sql = """
                INSERT INTO usuarios_api (name, username, email, habilitado)
                VALUES (%s, %s, %s, %s)
                """
                datos_usuario = (usuario_creado['name'], usuario_creado['username'], usuario_creado['email'], 1)  # 1 = habilitado por defecto
                cursor.execute(sql, datos_usuario)
                conexion.commit()
                print(Fore.GREEN + "usuario guardado en la base de datos.")
                cursor.close()
                conexion.close()
        else:
            print(Fore.RED + f"Error al crear el usuario: {respuesta.status_code}")

    except requests.exceptions.RequestException as error:
        print(Fore.RED + f"Error en la solicitud a la API: {error}")

def actualizar_usuario_api(usuario_id):
    usuario_actualizado = {
        "name": input(Fore.YELLOW + "Nuevo nombre del usuario: "),
        "username": input(Fore.YELLOW + "Nuevo username: "),
        "email": input(Fore.YELLOW + "Nuevo email: "),

    }
    usuario_actualizado_json = json.dumps(usuario_actualizado)
    
    try:
        url = f"{url_base}/users/{usuario_id}"
        headers = {'Content-Type': 'application/json'}
        respuesta = requests.put(url, data=usuario_actualizado_json, headers=headers)
        if respuesta.status_code == 200:
            usuario_actualizado = respuesta.json()
            print(Fore.GREEN + f"Usuario actualizado exitosamente: {usuario_actualizado}")

            # Actualizar en la base de datos también
            conexion = conectar_bd()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                UPDATE usuarios_api
                SET name = %s, username = %s, email = %s
                WHERE id = %s
                """
                cursor.execute(sql, (usuario_actualizado['name'], usuario_actualizado['username'], usuario_actualizado['email'], usuario_id))
                conexion.commit()
                print(Fore.GREEN + "Cliente actualizado en la base de datos.")
                cursor.close()
                conexion.close()

        else:
            print(Fore.RED + f"Error al actualizar el usuario con ID {usuario_id}: {respuesta.status_code}")
    except requests.exceptions.RequestException as error:
        print(Fore.RED + f"Error en la solicitud a la API: {error}")


# Función para eliminar un usuario en la API y base de datos
def eliminar_usuario_api(usuario_id):
    try:
        # Eliminar el usuario de la API
        url = f"{url_base}/users/{usuario_id}"
        respuesta = requests.delete(url)
        if respuesta.status_code == 200:
            print(Fore.GREEN + f"usuario con ID {usuario_id} eliminado exitosamente de la API.")
            
            # Ahora deshabilitamos el usuario en la base de datos (sin eliminarlo)
            conexion = conectar_bd()
            if conexion:
                cursor = conexion.cursor()
                # Actualizamos la columna 'habilitado' a FALSE (0) en lugar de eliminar el usuario
                sql = "UPDATE usuarios_api SET habilitado = 0 WHERE id = %s"
                cursor.execute(sql, (usuario_id,))
                conexion.commit()
                print(Fore.GREEN + f"usuario con ID {usuario_id} deshabilitado exitosamente en la base de datos.")
                cursor.close()
                conexion.close()
            else:
                print(Fore.RED + "Error al conectar a la base de datos para deshabilitar el usuario.")
        else:
            print(Fore.RED + f"Error al eliminar el usuario con ID {usuario_id} de la API: {respuesta.status_code}")
    except requests.exceptions.RequestException as error:
        print(Fore.RED + f"Error en la solicitud a la API: {error}")
    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al deshabilitar el usuario en la base de datos: {err}")
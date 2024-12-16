# servicios.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mysql.connector
from auxiliares.auxiliares import *

import requests
import json
# Función para obtener usuarios de la API
def obtener_usuarios_api():
    url = f"{API_URL}/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Función para obtener publicaciones de la API
def obtener_posts_api():
    url = f"{API_URL}/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Función para realizar una búsqueda con autenticación en la API de Serper
def buscar_en_google_api(query):
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': API_KEY_SERPER,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al realizar la búsqueda. Código de estado: {response.status_code}")
        return None

def crear_usuario_api(nombre, correo):
    url = "https://jsonplaceholder.typicode.com/users"  # URL de la API para crear un usuario
    
    # Definir el payload con los datos del usuario
    payload = {
        "name": nombre,
        "email": correo,
        "username": nombre.lower().replace(" ", ""),
        "phone": "123-456-7890",
        "website": "http://example.com"
    }
    
    try:
        # Realizar la solicitud POST
        response = requests.post(url, json=payload)
        
        # Verificar si la respuesta es exitosa (código 201)
        if response.status_code == 201:
            return response.json()  # Devolver los datos del usuario creado
        else:
            print(f"Error al crear el usuario. Código de estado: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

# Función para obtener usuarios de la API
def obtener_usuarios_api():
    url = f"{API_URL}/users"  # URL de la API para obtener los usuarios
    response = requests.get(url)  # Realizar la solicitud GET
    if response.status_code == 200:
        return response.json()  # Si la respuesta es exitosa, devolver los usuarios
    else:
        print(f"Error al obtener usuarios: {response.status_code}")
        return None  # Si ocurre un error, devolver None



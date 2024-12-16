# negocio/negocio.py
import sys
import os
import requests
import mysql.connector
from cryptography.fernet import Fernet
from colorama import Fore
import json

# Generar una clave para encriptación
def generar_clave():
    return Fernet.generate_key()

# Encriptar contraseña
def encriptar_contraseña(clave, contraseña):
    fernet = Fernet(clave)
    return fernet.encrypt(contraseña.encode()).decode()

# Desencriptar contraseña
def desencriptar_contraseña(clave, contraseña_encriptada):
    fernet = Fernet(clave)
    return fernet.decrypt(contraseña_encriptada.encode()).decode()

# Procesar los datos obtenidos desde la API
def obtener_usuarios_api():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Validar si la contraseña desencriptada coincide con la original
def validar_contraseña(contraseña_original, clave, contraseña_encriptada):
    contraseña_desencriptada = desencriptar_contraseña(clave, contraseña_encriptada)
    return contraseña_original == contraseña_desencriptada


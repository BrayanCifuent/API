
import requests
from auxiliares.constantes import URL_BASE

def obtener_usuarios():
    url = f"{URL_BASE}/users"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as error:
        print(f"Error al obtener los usuarios desde la API: {error}")
        return []
    


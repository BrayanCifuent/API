
import http.client
import json
def manejar_opcion_buscar_google():
    """Permite al usuario buscar en Google usando la API de Serper."""
    query = input("Ingrese el término o nombre que desea buscar en Google: ")  # Solicitar término de búsqueda
    buscar_en_google(query)  # Pasar el término como argumento

def buscar_en_google(query):
    """Realiza la búsqueda en Google a través de la API de Serper."""
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': 'e273b08557ea38dfc05855ce74110b4f64808ccc',  
        'Content-Type': 'application/json'
    }

    try:
        # Enviar la solicitud POST
        conn.request("POST", "/search", payload, headers)
        res = conn.getresponse()

        if res.status == 200:
            data = res.read()
            response_json = json.loads(data.decode("utf-8"))
            
            # Verificar si hay resultados y mostrarlos
            if 'organic' in response_json and len(response_json['organic']) > 0:
                print("\nResultados de búsqueda en Google (SOLO LOS PRIMEROS 5 RESULTADOS):")
                for i, resultado in enumerate(response_json['organic'][:5]):  # Mostrar los primeros 5 resultados
                    print(f"{i+1}. {resultado['title']} (URL: {resultado['link']})")

            else:
                print("❌ No se encontraron resultados en Google.")
        else:
            print(f"❌ Error: No se pudo obtener la búsqueda. Status: {res.status}")
    except Exception as e:
        print(f"❌ Ocurrió un error al realizar la búsqueda: {e}")
    finally:
        conn.close()

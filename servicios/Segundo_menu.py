import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from negocio.crud import *
from negocio.procesamiento import *
def maincrud():
    while True:
        mostrar_menu()
        opcion = leer_opcion()


        if opcion == 1:
            print(Fore.CYAN + "\nObteniendo todos los usuario desde la API...")
            usuarios = obtener_usuario()
            if usuarios:
                print(Fore.GREEN + f"{len(usuarios)} usuario obtenidos.")
    
            else:
                print(Fore.RED + "No se pudieron obtener los usuario desde la API.")
        
        elif opcion == 2:
            crear_usuario_api()
        
        elif opcion == 3:
            usuario_id = int(input(Fore.YELLOW + "\nIngrese el ID del usuario a actualizar: "))
            actualizar_usuario_api(usuario_id)
        
        elif opcion == 4:
            usuario_id = int(input(Fore.YELLOW + "\nIngrese el ID del usuario a eliminar: "))
            eliminar_usuario_api(usuario_id)
        

        
        elif opcion == 6:
            print(Fore.GREEN + "\nSaliendo del programa...")
            break

if __name__ == "__main__":
    agregar_usuario_api_a_bd()
    maincrud()


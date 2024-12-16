# datos/datos.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mysql.connector


# Conectar a la base de datos MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",  # Cambia si tu base de datos está en otro servidor
        user="root",       
        password="",  # Cambia por tu contraseña de MySQL
        database="gestion_empleados"   # Nombre de la base de datos que creaste
    )

# Función para insertar los datos de publicaciones, comentarios, etc.
def almacenar_datos_db(tabla, datos):
    db = conectar_bd()
    cursor = db.cursor()
    if tabla == "posts":
        query = """INSERT INTO posts (user_id, title, body) VALUES (%s, %s, %s)"""
        for item in datos:
            cursor.execute(query, (item['userId'], item['title'], item['body']))
    elif tabla == "comments":
        query = """INSERT INTO comments (post_id, name, email, body) VALUES (%s, %s, %s, %s)"""
        for item in datos:
            cursor.execute(query, (item['postId'], item['name'], item['email'], item['body']))
    # Agregar más casos según los datos
    db.commit()
    db.close()

def almacenar_usuarios_db(usuarios):
    for usuario in usuarios:
        db = conectar_bd()  # Conexión a la base de datos
        cursor = db.cursor()

        # Asegúrate de obtener correctamente los datos de los usuarios
        email = usuario.get('correo')
        nombre = usuario.get('nombre')

        # Verificar si el email ya existe en la base de datos
        cursor.execute("SELECT COUNT(*) FROM usuariosT WHERE email = %s", (email,))
        if cursor.fetchone()[0] == 0:  # Si no existe el email
            cursor.execute("INSERT INTO usuariosT (name, email, username, phone, website) VALUES (%s, %s, %s, %s, %s)", 
                           (nombre, email, usuario.get('username'), usuario.get('phone'), usuario.get('website')))
            print(f"Usuario {nombre} insertado en la base de datos.")
        else:
            print(f"El usuario con email {email} ya existe en la base de datos.")
        
        # Guardar cambios y cerrar la conexión
        db.commit()
        db.close()



# Función para obtener los datos de la base de datos
def obtener_datos_db(tabla):
    db = conectar_bd()
    cursor = db.cursor(dictionary=True)
    query = f"SELECT * FROM {tabla}"
    cursor.execute(query)
    datos = cursor.fetchall()
    db.close()
    return datos

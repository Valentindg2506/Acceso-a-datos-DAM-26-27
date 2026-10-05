import mysql.connector


mascotas = [
    {
        "nombre": "Toby",
        "edad": 3,
        "vacunas": ["rabia", "moquillo"]
    },
    {
        "nombre": "Luna",
        "edad": 5,
        "vacunas": ["rabia"]
    }
]


# PASO 2 - Averiguar el tipo de cada dato

print("--- TIPOS DE DATOS ---")

for clave in mascotas[0].keys():
    print(clave, type(mascotas[0][clave]))


# PASO 3 - Conectarse a la base de datos

conn = mysql.connector.connect(
    host="localhost",
    user="desfase",
    password="desfase",
    database="desfase"
)

cursor = conn.cursor()


# PASO 4 - Borrar las tablas si ya existen

cursor.execute("DROP TABLE IF EXISTS mascotas_vacunas")
cursor.execute("DROP TABLE IF EXISTS mascotas")


# PASO 5 - Crear la tabla mascotas

cursor.execute("""
    CREATE TABLE mascotas (
        Identificador INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        edad INT
    )
""")


# PASO 6 - Crear la tabla de vacunas

cursor.execute("""
    CREATE TABLE mascotas_vacunas (
        Identificador INT AUTO_INCREMENT PRIMARY KEY,
        mascotas_id INT,
        valor VARCHAR(100),

        FOREIGN KEY (mascotas_id)
        REFERENCES mascotas(Identificador)
    )
""")


# PASO 7 - Guardar las mascotas y sus vacunas

for mascota in mascotas:

    cursor.execute(
        "INSERT INTO mascotas (nombre, edad) VALUES (%s, %s)",
        (
            mascota["nombre"],
            mascota["edad"]
        )
    )

    mascota_id = cursor.lastrowid

    for vacuna in mascota["vacunas"]:

        cursor.execute(
            "INSERT INTO mascotas_vacunas (mascotas_id, valor) VALUES (%s, %s)",
            (
                mascota_id,
                vacuna
            )
        )


conn.commit()


# PASO 8 - Recuperar los datos

mascotas_recuperadas = []

cursor.execute(
    "SELECT Identificador, nombre, edad FROM mascotas"
)

filas_mascotas = cursor.fetchall()


for fila in filas_mascotas:

    mascota_id = fila[0]
    nombre = fila[1]
    edad = fila[2]

    cursor.execute(
        "SELECT valor FROM mascotas_vacunas WHERE mascotas_id = %s",
        (mascota_id,)
    )

    filas_vacunas = cursor.fetchall()

    vacunas = []

    for fila_vacuna in filas_vacunas:
        vacunas.append(fila_vacuna[0])

    mascota = {
        "nombre": nombre,
        "edad": edad,
        "vacunas": vacunas
    }

    mascotas_recuperadas.append(mascota)


print("\n--- MASCOTAS RECUPERADAS ---")
print(mascotas_recuperadas)


cursor.close()
conn.close()
